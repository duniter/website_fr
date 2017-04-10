Title: Commandes Duniter
Order: 9
Date: 2017-04-08
Slug: commandes
Authors: cgeek

Voici un guide des différentes commandes de l'exécutable `duniter` en ligne de commande.

## Initialiser son nœud

### `wizard key`

Permet de configurer le trousseau cryptographique utilisé par votre nœud. C'est à travers ce trousseau que votre nœud peut être identifié et ses réponses authentifiées, vérifiées.

Ce trousseau est composé d'une clé privée et d'une clé publique Ed25519.

    duniter wizard key
    ? Modify you keypair? Yes
    ? Key's salt *****************
    ? Key's password ********************

### `wizard network`

Permet de configurer la connectivité réseau de votre nœud : à la fois celle locale (interface réseau et port de la machine sur lequels se connecter) et distance (déclaration de votre nœud sur *comment* le contacter depuis l'Internet).

    duniter wizard network
    ? IPv4 interface: eth0 192.168.1.667
    ? IPv6 interface: eth0 2a01:e35:8ae7:8bb0:3de1:ee66:a6ba:a438  (Global)
    ? Port: 10900
    ? Remote IPv4: 88.174.120.187
    ? Remote port: 10900
    ? UPnP is available: use automatic port mapping? (easier) Yes
    ? Does this server has a DNS name? Yes
    ? DNS name: cgeek.fr

Bien évidemment, il faut mettre ici vos propres valeurs, et donc ne pas mettre "192.168.1.667", ni "2a01:e35:8ae7:8bb0:3de1:ee66:a6ba:a438" ou encore "cgeek.fr".

### `sync`

Pour un nœud tout neuf ou dont les données ont été effacées (par exemple suite à l'utilisation de `reset data`), il convient d'initialiser son nœud en synchronisant une blockchain existante. Cette opération téléchargera la blockchain puis en extraira toutes les données de la monnaie : toile de confiance, unités de monnaie existantes, transactions.

Synchroniser son nœud avec le réseau Ğ1 (monnaie Duniter) :

    duniter sync g1.duniter.org 443
    Progress:

    Download: [||||                ] 23 %
    Apply:    [                    ] 0 %

Cette commande prend du temps. Soyez patients.

#### Option `--nointeractive`

Désactive l'affichage avec barres de progression au profit d'une sortie classique de commande.

    duniter sync g1.duniter.org 443
    2017-04-10T08:31:42+02:00 - info: Try with g1.duniter.org:10901 4aCqwi
    2017-04-10T08:31:42+02:00 - info: Sync started.
    2017-04-10T08:31:42+02:00 - info: Getting remote blockchain info...
    2017-04-10T08:31:42+02:00 - info: Connecting to g1.duniter.org...
    2017-04-10T08:31:42+02:00 - info: Peers...

#### Option `--nopeers`

Désactive le téléchargement P2P ainsi que le téléchargement du listing des nœud du réseau.

    duniter sync g1.duniter.org 443
    2017-04-10T08:32:26+02:00 - info: Try with g1.duniter.org:10901 4aCqwi
    2017-04-10T08:32:26+02:00 - info: Sync started.
    2017-04-10T08:32:26+02:00 - info: Getting remote blockchain info...
    2017-04-10T08:32:26+02:00 - info: Connecting to g1.duniter.org...
    2017-04-10T08:32:26+02:00 - info: Downloading Blockchain...
    2017-04-10T08:32:26+02:00 - debug: dl starts from 0
    2017-04-10T08:32:26+02:00 - info: Getting chunck #36/36 from 9000 to 9023 on peer g1.duniter.org:10901
    2017-04-10T08:32:26+02:00 - info: GOT chunck #36/36 from 9000 to 9023 on peer g1.duniter.org:10901

#### Option `--cautious`

Force la vérification minutieuse de la validité de chaque bloc par rapport au règles du protocole.

    duniter sync g1.duniter.org 443 --cautious

#### Option `--memory`

Réaliser la synchronisation en mémoire uniquement. La synchronisation ne sera donc pas stockée sur le disque dur. Cette option est utile pour une vérification rapide de l'intégrité de la blockchain quand combinée à l'option `--cautious`.

    duniter sync g1.duniter.org 443 --cautious --memory

## Démarrer/Arrêter son nœud

Un nœud Duniter tourne généralement en tâche de fond. Duniter fourni plusieurs commandes afin d'être démarré/arrêté dans différends modes de fonctionnement.

### `start`

Démarre le nœud Duniter *sans interface graphique*, en tâche de fond. Le seul moyen de communiquer avec le nœud en tant qu'administrateur est de consulter ses logs avec `duniter logs`.

    duniter start
    Starting duniter_default daemon...
    duniter_default daemon started. PID: 1328

### `stop`

Stoppe un nœud Duniter qui tournerait en tâche de fond. Si aucun nœud ne tourne, la commande ne fait rien.

    duniter stop
    Stopping duniter_default daemon...
    duniter_default daemon stopped.

### `status`

Dit si le nœud est actuellement lancé en tâche de fond ou non.

    duniter status
    Duniter is running using PID 1832.

### `restart`

Raccourci pour `stop` suivi d'un `start`. Si aucun nœud n'était lancé, la commande équivaut alors à un simple `start`.

    duniter restart
    duniter_default daemon is not running
    Starting duniter_default daemon...
    duniter_default daemon started. PID: 1913

### `webstart`

Démarre le nœud Duniter *avec interface graphique*, en tâche de fond.

Le nœud est alors accessible graphiquement à l'adresse [localhost:9220](http://localhost:9220).

    duniter webstart
    Starting duniter_default daemon...
    duniter_default daemon started. PID: 2878

#### Option `--webmhost`

Il est possible de remplacer l'interface `localhost` par l'interface de votre choix.

    duniter webstart --webmhost 192.168.1.35

Le nœud est alors accessible graphiquement à l'adresse http://192.168.1.35:9220.

#### Option `--webmport`

Il est possible de remplacer le port `9220` par le port de votre choix.

    duniter webstart --webmport 9330

Le nœud est alors accessible graphiquement à l'adresse http://localhost:9330.

### `webrestart`

Raccourci pour `stop` suivi d'un `webstart`. Si aucun nœud n'était lancé, la commande équivaut alors à un simple `webstart`.

Le nœud est alors accessible graphiquement à l'adresse [localhost:9220](http://localhost:9220).

    duniter webrestart
    Stopping duniter_default daemon...
    duniter_default daemon stopped.
    Starting duniter_default daemon...
    duniter_default daemon started. PID: 2938

## Administration
     
### `direct_start`

Démarre le nœud *en direct*, sans exécution en tâche de fond. Les logs de l'application apparaitront en direct dans la console.

Pour arrêter le nœud, réaliser la combinaison de touches `Ctrl^C`.

    duniter direct_start
    2017-04-10T11:12:28+02:00 - info: >> Server starting...
    2017-04-10T11:12:28+02:00 - info: Node version: 1.2.1
    2017-04-10T11:12:28+02:00 - info: Node pubkey: 2ny7YAdmzReQxAayyJZsyVYwYhVyax2thKcGknmQy5nQ
     
#### Option `--keyprompt`

Demande des identifiants secrets au démarrage de l'application qui généreront le trousseau cryptographique en mémoire. Ce trousseau sera ensuite utilisé pendant toute la durée d'exécution de l'application et disparaîtront à son arrêt.

Option utile pour ne pas stocker son trousseau dans un fichier.

    duniter direct_start --keyprompt
     
### `direct_webstart`

Identique à `direct_start`, mais démarre avec l'interface graphique chargée.

    duniter direct_webstart

### `reset data`

Supprime toutes les *données* du nœud : blockchain, identités, transactions, etc. Ne supprime pas la configuration.

    duniter reset data

### `reset all`

Supprime toutes les données et toute la configuration du nœud. Équivalent à avoir une nouvelle installation.

    duniter reset all

### `logs`

Affiche les dernières lignes de journaux de Duniter et affiche les nouvelles lignes en continu.

    duniter logs

### `config`

Permet de modifier une ou plusieurs valeurs de configuration par options.

    duniter config --option1 <valeur1> --option2 --option3 <valeur3>

Nécessite un redémarrage du nœud pour que la nouvelle configuration soit prise en compte.

#### Option `--upnp`

Active l'UPnP.

    duniter config --upnp

#### Option `--noupnp`

Désactive l'UPnP.

    duniter config --noupnp

#### Option `--cpu <pourcentage>`

Définit le pourcentage de CPU disponible.

    duniter config --cpu 0.5

Configure l'utilisation CPU à 50%.

#### Option `--ipv4 <adresse>`

Configure l'interface réseau IPv4 de la machine sur laquelle dialoguer.

    duniter config --ipv4 192.168.1.22

Configure l'écoute sur l'interface réseau `192.168.1.22`.

#### Option `--ipv6 <adresse>`

Configure l'interface réseau IPv6 de la machine sur laquelle dialoguer.

    duniter config --ipv6 "2a01:e35:8ae7:8bb0:2e0:4cff:feca:36"

Configure l'écoute sur l'interface réseau `2a01:e35:8ae7:8bb0:2e0:4cff:feca:36`.

#### Option `--port <numero>`

Configure le port de la machine sur lequel dialoguer pour chaque interface (IPv4, IPv6).

    duniter config --port 10901

Configure l'écoute sur le port machine `10901`.

#### Option `--remote4 <adresse>`

Configure l'adresse IPv4 distante de la machine.

    duniter config --ipv4 88.174.120.187

Configure le nœud pour qu'il se déclare disponible à l'adresse `88.174.120.187`.

#### Option `--remote6 <adresse>`

Configure l'adresse IPv6 distante de la machine.

    duniter config --ipv6 2a01:e35:8ae7:8bb0:2e0:4cff:feca:36

Configure le nœud pour qu'il se déclare disponible à l'adresse `2a01:e35:8ae7:8bb0:2e0:4cff:feca:36`.

#### Option `--remotep <adresse>`

Configure le port distant de la machine.

    duniter config --remotep 10901

Configure le nœud pour qu'il se déclare disponible sur le port `10901`.

#### Option `--addep <specification>`

Déclare une nouvelle interface de contact réseau inconnue de Duniter.

    duniter config --addep "ES_CORE_API g1.data.duniter.fr"

**Attention :** cette commande doit être exécutée sur un seul nœud : toutes les interfaces inconnues doivent être déclarées sur celui-ci, au risque de tomber dans une boucle infinie de création/suppression d'interfaces.

#### Option `--remep <specification>`

Supprime une interface de contact réseau inconnue de Duniter qui a été préalablement ajoutée.

    duniter config --remep "ES_CORE_API g1.data.duniter.fr"

**Attention :** cette commande doit être exécutée sur un seul nœud : toutes les interfaces inconnues doivent être déclarées sur celui-ci, au risque de tomber dans une boucle infinie de création/suppression d'interfaces.

#### Option `--autoconf`

Regénère la configuration réseau de façon automatique et génère une paire de clé aléatoirement si celle-ci n'existe pas.

    duniter config --autoconf

## Générer un bloc manuellement

### `gen-next`

Génère le prochain bloc à partir des données en piscine et du bloc courant, réalise la preuve de travail pour la difficulté demandée puis soumet le bloc résultant à un nœud.

    duniter gen-next g1.duniter.org 10901 74
    
Cette commande génère le prochain bloc, l'envoie au nœud `g1.duniter.org:10901` sur le port `10901` et calcule la preuve de travail avec une difficulté de `74` (empreinte débutant par 4 zéros).

#### Option `--show`

Affiche le bloc calculé *avant* la réalisation de la preuve de travail et la soumission au réseau. Permet de contrôler son contenu.

    duniter gen-next g1.duniter.org 10901 74 --show

#### Option `--check`

Modifie le comportement de la commande : celle-ci ne réalise plus de preuve de travail ni ne soumet le bloc au réseau. A la place, elle génère le bloc et vérifie si celui-ci est acceptable par un nœud.

    duniter gen-next --show --check

### `gen-root`

Génère le block#0 de façon automatique, en incluant un maximum de membres.

    gen-root duniter.org 10901 74
    

### `gen-root-choose`

Génère le block#0 en sélectionnant manuellement les membres à inclure

    gen-root duniter.org 10901 74
    ? Newcomers to add: 
     ◯ john
     ◯ dude404
     ◉ sinogeek
    ❯◉ deviantime
     ◯ kernel
     ◯ vivide

## Options transversales

Ces options, si utilisées, doivent être *systématiquement* fournies lors de futures commandes pour conserver leur application.

Car ces options permettent de redéfinir temporairement (le temps d'une commande) une variable globale de l'application.

#### Option `--home`

Permet de redéfinir le dossier où sont stockées les données de l'application. La valeur par défaut de cette option est `$HOME/.config/duniter/`

    duniter sync g1.duniter.org 10901 --home /tmp/duniter
    
Cette commande réalisera une synchronisation et stockera le résultat dans le dossier `/tmp/duniter/duniter_default`.

#### Option `--mdb`

Permet de redéfinir le dossier où sont stockées les données de l'application. La valeur par défaut de cette option est `duniter_default`.

    duniter sync g1.duniter.org 10901 --mdb g-one
    
Cette commande réalisera une synchronisation et stockera le résultat dans le dossier `$HOME/.config/duniter/g-one`.

Il est possible de combiner les 2 options :

    duniter sync g1.duniter.org 10901 --home /tmp/duniter --mdb g-one
    
Cette commande réalisera une synchronisation et stockera le résultat dans le dossier `/tmp/duniter/g-one`.

#### Option `--keyfile`

Permet de fournir le trousseau cryptographique via un ficher YAML.

    duniter start --keyfile /tmp/key.yml
    
Avec un fichier `key.yml` au format suivant:

```yaml
pub: "EfJ5xHtwjxvF3Bq4GMeuKkKe5nmodQcqkvgVPZZT6gCF"
sec: "2vyztEUMgSgcidmLPprbR5pPUUFbGnTG99mdEMPiiRD6wVAm76AvjDDp5PypzMsTvLKX8UrJ5sQbCUCmxTWRtr9d"
```

#### Options `--salt`, `--passwd`

Ces options permettent d'utiliser le trousseau cryptographique résultant de la valeur de ces deux options combinées.

    duniter start --salt abc --passwd def

#### Options `--keyN`, `--keyr`, `--keyp`

L'utilisation de `--salt` et `--passwd` présupposent d'autres paramètres cryptographiques nommés « N,r,p ». Leur valeur par défaut dans Duniter est « 4096,16,1 ».
 
Les options `--keyN`, `--keyr`, `--keyp` permettent de redéfinir précisément ces valeurs.

    duniter --salt abc --passwd def --keyN 4096 --keyr 16 --keyp 1
