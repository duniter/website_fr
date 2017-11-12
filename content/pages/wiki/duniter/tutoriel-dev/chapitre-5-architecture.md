Title: 5. Architecture de Duniter
Order: 1
Date: 2017-10-31
Slug: chapitre-5-architecture
Authors: cgeek

## Introduction

Ce chapitre a pour but de visualiser l'architecture de Duniter sous différents angles, afin d'apporter une vue multidimensionnelle du code qui s'organise selon plusieurs axes principaux :

* le cycle d'exécution d'une commande
* l'organisation en modules
* le fonctionnement global pour un nœud « démarré »

Nous ferons également le lien avec les fichiers concernés.

> Ce chapitre est plutôt théorique. Toutefois, des exemples de code sont donnés et nous vons encourageons à les reproduire en modifiant le fichier `app/modules/reset.ts`, quitte à en retirer le contenu pour vos essais.

### Cycle d'exécution

Commençons par l'exécution de Duniter, par exemple la commande :

    node bin/duniter reset data

Ici, nous exécutons Duniter en faisant appel à NodeJS (`node`) et demandons d'interpréter le fichier `bin/duniter` (un fichier JavaScript, sans extension) et passons les arguments `reset data` qui sont des chaînes de caractères.

Le fichier `bin/duniter` est le point de départ de toute commande Duniter. C'est l'unique fichier d'entrée pour tout appel au logiciel. Voyons ce qu'il se passe alors :

::uml:: format="svg" alt="Cycle d'execution de Duniter"

@startuml

title Cycle d'execution de Duniter

== Initialisation ==

"duniter <cmd>" -> onConfig: Charge les modules :\n- Ceux par defaut\n * duniter-ui\n * ws2p\n * bma\n * crawler\n * keypair\n * prover\n * ...\n- Ceux ajoutes par l'utilisateur

onConfig -> Execution: Pour chaque module :\n- Charge sa configuration specifique,\navec acces aux options de la ligne\nde commande (--opt1 valeur1...)

== Execution de la commande ==

Execution -> Execution: Code specifique\nde la commande\n<cmd>
note left
  **Execute le code specifique correspondant a la commande <cmd>**


  Le code specifique dispose d'un acces a plusieurs objets :


  *<color #118888>server</color> : contient toute la logique du noeud, sa blockchain et un acces vers
  sa base de donnees
  *<color #118888>conf</color> : contient toute configuration collectee dans la phase "onConfig"
  *<color #118888>program</color> : acces a la commande <cmd>, ses eventuelles
    sous-commandes [sub] et les options passees (--opt1 <val1>...).


  Exemples de commandes :


  *<color #FF8888>reset data</color> : reinitialise les donnees
  *<color #FF8888>sync</color> : synchroniser la blockchain G1
  *<color #FF8888>direct_start</color> : demarrer le noeud
  *...


  Cette phase peut etre courte, mais peut aussi durer indefiniment. C'est le cas
  de la commande <color #FF8888>direct_start</color> qui n'a pas de fin programmee : la seule facon
  d'arreter la commande est de terminer le processus.


  Toute commande s'effectue dans une sous-phase specifique de l'Execution
  selon qu'elle necessite l'acces a la base de donnees ou non. Nous verrons
  cela dans un prochain schema.
end note

== Fin de la commande ==

Execution -> "duniter <cmd>" : Fin de la commande, affiche eventuellement une exception en cas d'erreur.

@enduml

::end-uml::

Nous pouvons voir ici que tout appel à Duniter déclenche 3 procédures dans le code : le chargement des modules, le chargement de la configuration et enfin l'exécution de la commande. Mais aussi d'un autre point de vue, déclenche 3 phases : l'initialisation, l'exécution, puis la fin (le retour) de la commande.

Dans notre exemple :

    node bin/duniter reset data
    
Le code finalement exécuté est celui de la commande `reset data` présent dans le fichier `app/modules/reset.ts`. Ce code est en charge de supprimer toutes les données du nœud, afin de le remettre à neuf par exemple.

Si l'on avait appelé une autre commande, comme :

    node bin/duniter sync g1.duniter.org 443

Alors le code appelé aurait été celui de la commande de synchronisation présent dans le fichier `app/modules/crawler/index.ts`. On aurait pu penser qu'il s'agirait du fichier sync.ts, mais ici le module crawler gère plusieurs commandes dont celle qui permet la synchronisation au réseau : or il est possible de regrouper plusieurs commandes dans un même fichier, pourquoi pas nommé de façon générique `index.ts`.

Enfin, la commande `node bin/duniter blabla` aurait retourné une erreur, car cette commande n'existe pas.

## Organisation en modules

Afin d'isoler au mieux chaque logique spécifique du code et de permettre d'ajouter des fonctionnalités à Duniter, ce dernier a été pensé pour intégrer une logique de *modules*. Ainsi, toutes les commandes et options disponibles sur Duniter le sont via la définition d'un module.

Un module peut agir à plusieurs niveaux :

* **Configuration** : le module peut charger des informations supplémentaires ou même redéfinir la configuration générale
* **Commandes** : le module peut définir une ou plusieurs commandes exécutables
* **Options** : le module peut définir de nouvelles options dans la ligne de commande (--option-m1, -O…)
* **Service** : le module peut définir un service, c'est-à-dire une portion de code utilisée quand une commande décide d'activer les services.

Un module peut agir aussi bien n'agir à aucun comme à tous les niveaux à la fois : les champs `config`, `cliOptions`, `cli`, `services` sont tous facultatifs.

::uml::

@startuml

title Definition d'un module

package "Module" {
  [config]
  [cliOptions]
  [cli]
  [service]
}

package "CLI Options" {
  [cliOptions] ---> [Option1\nvalue: '--opt1 <v1>'\ndesc: 'Prend une valeur']
  [cliOptions] ---> [Option2\nvalue: '--opt2, -o'\ndesc: 'Un booleen']
}

package "Config" {
  [config] --> [**onLoading** callback\nPermet de charger\nune configuration au\ndemarrage.]
  [config] --> [**beforeSave** callback\nPermet de modifier\nla configuration avant\npersistance.]
}

package "Service" {
  [service] ---> [neutral]
}

package "Sous-services" {
  [neutral] ---> [sous-service1]
  [neutral] ---> [...]
  [neutral] ---> [sous-serviceN]
}

package "Commandes" {
  [cli] ---> [Commande 1\nname: 'cmd1'\ndesc: 'commande 1'\nlogs: true\nonConfiguredExecute: callback?\nonDatabaseExecute: callback?]
  [cli] ---> [Commande 2\nname: 'cmd2'\ndesc: 'commande 2'\nlogs: true\nonConfiguredExecute: callback?\nonDatabaseExecute: callback?]
}

@enduml

::end-uml::

### Exemples

#### Configuration

Un module de configuration pourrait par exemple permettre de mettre à jour une configuration ancienne. Imaginons que la variable de configuration `keyring` ait été renommée en `keypair`, alors on pourrait définir en module s'occupant de migrer une ancienne configuration vers la nouvelle :

```ts
import {ConfDTO} from "../lib/dto/ConfDTO"

module.exports = {
  duniter: {

    config: {
      onLoading: async (conf:ConfDTO) => {
        if (conf.keyring) {
          // Migrate to `keypair`
          conf.keypair = conf.keyring
        }
      },
      beforeSave: async (conf:ConfDTO) => {
        // Remove old `keyring` name
        if (conf.keyring && conf.keypair) {
          delete conf.keypair
        }
      }
    }
  }
}
```

#### Commande

Un module pourrait définr la commande `nb-membres` qui affiche le nombre de membres actuels de la toile de confiance :

```ts
import {ConfDTO} from "../lib/dto/ConfDTO"
import {Server} from "../../server"

module.exports = {
  duniter: {

    cli: [{
      name: 'nb-membres',
      desc: 'Affiche le nombre de membres approximatif de la toile',
      logs: false,
      onDatabaseExecute: async (server:Server, conf:ConfDTO) => {
        const resultat = await server.dal.iindexDAL.query('' +
          'SELECT COUNT(*) as compte FROM i_index WHERE member'
        )
        console.log('Nombre de membres : %s', resultat[0].compte)
      }
    }]
  }
}
```

Exécution de la commande :

    bin/duniter nb-membres
    Nombre de membres : 402

Notez ici l'utilisation de `onDatabaseExecute:` : il s'agit d'une des deux phases possibles pour l'exécution d'une commande. L'autre est `onConfiguredExecute` :

::uml::

@startuml

title Moment d'execution d'un module

onConfig -> onConfiguredExecute : onConfiguredExecute defini ?

onConfiguredExecute -> onConfiguredExecute : execution de <cmd>
 
onConfiguredExecute -> onConfig

onConfig -> onDatabaseExecute : onDatabaseExecute defini ?

onDatabaseExecute -> onDatabaseExecute : execution de <cmd>

onDatabaseExecute -> onConfig

@enduml

::end-uml::

Comment choisir s'il vaut mieux utiliser `onConfiguredExecute` ou `onDatabaseExecute` ? La règle est simple : si vous avez besoin de réaliser des accès à la base de données, alors utilisez `onDatabaseExecute`. Sinon, préférez `onConfiguredExecute` car cela évitera d'attendre la connexion à la base de données et permettra donc une exécution plus rapide.

#### Options

Un module peut ajouter de nouvelles options à la ligne de commande. Toutefois il n'y a d'intérêt que si ces options se conjugent à une utilisation dans les autres niveaux (*Configuration*, *Commandes* et *Services*) car une option ne fait rien en elle-même, si ce n'est se rendre disponible.

```ts
import {ConfDTO} from "../lib/dto/ConfDTO"
import {Server} from "../../server"

module.exports = {
  duniter: {

    // Options du module
    cliOptions: [
      { value: '--tres-certifies', desc: 'Ne compter que les membres avec plus de 10 certifications vers eux.' }
    ],

    cli: [{
      name: 'nb-membres',
      desc: 'Affiche le nombre de membres de la toile',
      logs: false,
      onDatabaseExecute: async (server:Server, conf:ConfDTO, program:any) => {
        const requeteSQL = program.tresCertifies ?
          // Compter les membres avec plus de 10 certifications
          'SELECT COUNT(*) as compte FROM i_index i WHERE member AND 10 < (' +
          ' SELECT COUNT(*) FROM c_index c WHERE c.receiver = i.pub' +
          ')'
          :
          // Compter tous les membres
          'SELECT COUNT(*) as compte FROM i_index WHERE member'
        const resultat = await server.dal.iindexDAL.query(requeteSQL)
        console.log('Nombre de membres : %s', resultat[0].compte)
      }
    }]
  }
}
```

Exécution de la commande :

    bin/duniter nb-membres --tres-certifies
    Nombre de membres : 402

#### Service

Un module peut également fournir un *service*. C'est une entité qui fonctionne sans fin, et qui ne sera utilisé que si les services sont activés explicitement par une commande, comme la commande `direct_webstart` le fait :

```ts
{
  name: 'direct_start',
  desc: 'Start Duniter node with direct output, non-daemonized.',
  onDatabaseExecute: async (server:Server, conf:ConfDTO, program:any, params:any, startServices:any) => {
    const logger = server.logger;

    logger.info(">> Server starting...");

    await server.checkConfig();
    // Add signing & public key functions to PeeringService
    logger.info('Node version: ' + server.version);
    logger.info('Node pubkey: ' + server.conf.pair.pub);

    // Services
    await startServices();

    logger.info('>> Server ready!');

    return new Promise(() => null); // Never ending
  }
}
```

Ainsi **tous les services déclarés** par les modules seront démarrés simultanément lors de l'appel à `startServices()`.

Exemple de service : 

```ts
import {ConfDTO} from "../lib/dto/ConfDTO"
import {Server} from "../../server"
import * as stream from "stream"

module.exports = {
  duniter: {

    service: {
      neutral: (server:Server, conf:ConfDTO) => {
        return new MyService()
      }
    }
  }
}

/**
* Service d'exemple
*/
class MyService extends stream.Readable {

  constructor() {
    super({ objectMode: true })
    let i = 1
    setInterval(() => console.log("Le service tourne! (message#%s)", i++), 5000)
  }

  _read(){}
}
```

Et l'on pourra alors constater si l'on lance `node bin/duniter direct_start` des messages de log toutes les 5 secondes (5000 millisecondes) :

    Le service tourne ! (message#1)
    Le service tourne ! (message#2)
    Le service tourne ! (message#3)
    ...

## Fonctionnement général

Pour un nœud démarré par la commande `direct_start`, alors **tous les services de modules** fonctionnent de concert. Voici un petit aperçu : 

::uml::

@startuml

server <--> config
config <--> [**keypair**\nFournit un trousseau\ncryptographique au\nserveur par configuration.]
server <--> [**prover**\nProduit des nouveaux\nblocs et realise leur\npreuve de travail.]
[**peersignal**\nEmet periodiquement\nune nouvelle fiche de\npair a jour.] <--> server

package "BMA" {
  [**BMA server**\nServeur HTTP public qui recoit\net transmet les documents\nDuniter au serveur.] <---> server
  [**BMA crawler**\nSollicite les autres noeuds BMA\npour recuperer des documents\nde facon active.] <---> server
  [**BMA router**\nTransmet les documents valides\ntraites par le serveur au reste du\nreseau via BMA.] <---> server
}

package "WS2P" {
    [**WS2P**\nNouvelle couche reseau\nP2P visant a remplacer\nBMA pour la communication\ninter-noeuds.] <--> server
}

@enduml

::end-uml::

Comme on peut le voir, l'élément central est `server`. En effet, tous ces modules soient s'appuient sur, soit alimentent `server` d'une façon ou d'une autre.

Cela est tout à fait normal, puisqu'il s'agit de l'élément central qui contient toute la logique de la blockchain et l'accès aux données qu'elle contient (transactions, unités de monnaie, identités, certifications, ...).

Exemple de flux observables dans Duniter :

*Réception, traitement puis retransmission d'un document via BMA* :

::uml::

@startuml

[BMA HTTP] -> serveur : recoit
serveur -> [BMA router] : retransmet

@enduml

::end-uml::

*Réception, traitement puis retransmission d'un document via WS2P* :

::uml::

@startuml

[WS2P] -> serveur : recoit le bloc#2299
serveur -> [WS2P] : retransmet le bloc#2299

@enduml

::end-uml::

*Partage d'un signal de bloc empilé sur la blockchain* :

::uml::

@startuml

serveur -> [prover] : signal : bloc ajoute

@enduml

::end-uml::

Ce signal permet de notifier au module `prover` qu'un nouveau bloc a été ajouté, et donc de lui permettre de changer de stratégie : s'il était en train de réaliser la preuve de travail sur ce bloc, le signal lui permet d'arrêter son travail en cours et redémarrer une preuve sur un nouveau bloc. S'il était en attente et que ce bloc permet de débloquer l'attente (sortie de la fenêtre d'exclusion), même idée : le signal lui permet de démarrer une nouvelle preuve.

*Partage d'un signal de déconnexion* :

::uml::

@startuml

WS2P -> server : signal de deconnexion
server -> WS2P : signal de deconnexion (echo)

@enduml

::end-uml::

Ce signal, émis par l'une des connexions WS2P présentes, utilise l'objet `server` comme support pour partager ce signal avec tous les modules qui pourraient en avoir besoin, dont lui-même ! En effet, le module WS2P peut se servir de ce signal pour détecter un manque de connectivité (on vient de perdre une connexion !) et décider d'agir pour améliorer cette situation.

Il est à noter que seul `server` réalise de l'écho, ainsi le signal ne rebondira pas sur WS2P à nouveau en direction du serveur, menant à une boucle infinie.

### Démarrage du serveur

Et donc, quand on « démarre » Duniter, que se passe-t-il ?

    node bin/duniter direct_start

Alors, Duniter passe par les phases décrites plus tôt :

* Chargement des modules
* Chargement de la configuration
* Sur connexion de la base de données (`onDatabaseExecute`), lancement des services : 
    * Démarrage de l'écoute BMA
    * Établissement de connexions WS2P
    * Démarrage du service `prover` : 
        * Si le nœud n'est pas exclu de la preuve de travail, il commence la preuve d'un nouveau bloc
        * Sinon, le nœud attend qu'un bloc arrive par BMA ou WS2P

Voilà donc comment on obtient un nœud Duniter fonctionnel à ce jour.

> Passer à la suite du tutoriel : [Chapitre 6 : Code](../chapitre-6-code).
