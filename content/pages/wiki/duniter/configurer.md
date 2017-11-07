Title: Configurer un nœud Duniter
Order: 9
Date: 2017-09-22
Slug: configurer
Authors: elois

Ce document est un petit tutoriel pour configurer votre nœud Duniter fraichement installé,  c'est la suite logique du [tutoriel d'installation](https://duniter.org/fr/wiki/duniter/installer).

## Sommaire

* [Duniter versions 1.6.x (avec WS2P)](#version-16x)
    * [En ligne de commande](#en-ligne-de-commande)
        * [Configurer le trousseau de clés cryptographiques](#configurer-le-trousseau-de-clés-cryptographiques)
            * [Avoir plusieurs nœuds avec le même trousseau de clés](#avoir-plusieurs-nœuds-avec-le-même-trousseau-de-clés)
        * [Configurer le réseau](#configurer-le-réseau)
            * [Les API](#les-api)
                * [Configurer WS2P](#configurer-ws2p)
                    * [WS2P privé](#ws2p-privé)
                      * [WS2PTOR](#ws2ptor-privé)
                    * [WS2P public](#ws2p-public)
                      * [Définir un patch pour votre point d'accès ws2p](#définir-un-patch-pour-votre-point-daccès-ws2p)
                * [Configurer BMA](#configurer-bma)
                * [Qu'est ce que l'UPnP ?](#quest-ce-que-lupnp-)
                * [Note sur le WS2P public (recommandé)](#note-sur-le-ws2p-public-recommandé)
        * [Checker votre configuration](#checker-votre-configuration)
        * [Synchroniser votre nœud](#synchroniser-votre-nœud)
        * [Lancement](#lancement)
        * [Suivre les log](#suivre-les-log)
        * [Aller plus loin](#aller-plus-loin)
    * [Via l'interface d'administration web](#via-linterface-dadministration-web)

----

# Version 1.6.x

## En ligne de commande

### Configurer le trousseau de clés cryptographiques

Tout les nœuds duniter ont un trousseau de clés cryptographiques, qu'ils utilisent pour signer les informations qu'il transmettent sur le réseau. Il y a deux types de nœuds duniter :

**1. les nœuds membre :** Si le trousseau de clé du nœud correspond a une identité membre, alors le nœud est de type "membre", et 
va automatiquement prendre part au calcul des blocs.

**2. les nœuds miroir :** Si le trousseau de clé du nœud ne correspond pas à une identité membre, alors le nœud est de type "miroir", il ne pourra pas écrire de bloc, mais sera quand même utile pour la résilience du réseau ainsi que pour répondre aux requêtes des clients.

Par défaut ce trousseau est aléatoire, et le nœud duniter est donc un nœud miroir. Vous pouvez modifier le trousseau de clés du noeud avec cette commande :

    duniter wizard key

Attention le trousseau de clés renseigner via cette commande sera stocké en clair sur le disque !
Pour éviter cela vous pouvez choisir de ne renseigner le trousseau de clés a utiliser qu'au lancement du nœud afin que votre trousseau de clés reste seulement en mémoire vive, pour cela ajoutez l'option `--keyprompt` a la commande de lancement du nœud.

#### Avoir plusieurs nœuds avec le même trousseau de clés

  Il est possible d'avoir plusieurs nœuds membre avec votre trousseau de clés membre mais dans ce cas vous devez attribuer un identifiant unique a chacun de vos nœuds, cet identifiant unique est nommé **préfixe** car sont unique rôle est de préfixer le nonce des blocs que vous calculez afin d'éviter que deux de vos nœuds ne calculent la même preuve.
  
Sur votre 1er nœud : Vous n'avez rien a faire, le préfixe vaut `1` par défaut.

Sur votre 2ème nœud : 

    duniter config --prefix 2

Sur votre 3ème nœud :

    duniter config --prefix 3

etc

Le préfixe doit être un entier compris entre `1` et `899`.

### Configurer le réseau

#### Les API

  En version `1.6.x` il existe deux API (Application Programming Interface) permettant a votre nœud duniter de communiquer a  vec d'autres programmes.

1. WS2P (WebSocketToPeer) : Cette API est dédiée a la communication inter-nœuds, c'est a dire entre votre nœud duniter et les autres nœud de la même monnaie. **WS2P est activée par défaut** sur votre nœud duniter.
2. BMA  (Basic Merkled Api) : Cette vielle API est dédiée a la communication avec les logiciels clients (Cesium, Sakia, Silkaj), elle peut également être utilisée par n'importequel programme externe souhaitant requêter le réseau (un site web qui voudrais vérifier la présence d'une transaction en blockchain par exemple). BMA est veillissante, nous projettons de développer une nouvelle API client qui la remplacera. **BMA est désactivée par défaut**  sur votre nœud duniter.

#### Configurer WS2P

##### notion de WS2P Public et WS2P Privée

WS2p Privé = connexions WS2p sortantes.  
WS2p public = connexions WS2p entrantes.

Une connexion WS2p entre deux nœuds duniter à toujours un sens, elle est initiée par l'un des nœuds qui est donc l'initiateur et l'autre est l'accepteur. Les connexions que votre nœud duniter initie avec d'autres nœuds duniter sont sortantes, elles dépendent de votre configuration WS2p privée. En revanche, les connexions que votre nœud duniter accepte d'un autre nœud sont entrantes, elles dépendent de votre configuration WS2P publique.

##### WS2P privé

Ce mode est activé par défaut et configuré automatiquement. Vous pouvez le désactiver avez la commande suivante :

    duniter config --ws2p-noprivate

Et pour le réactiver : 

    duniter config --ws2p-private


Les seules configurations possibles sont de définir un nombre maximal de connexions WS2P sortantes et une liste de clés préférés, votre nœud se connectera en priorité aux nœuds duniter dont la clé publique fait partie de votre liste de clés préférés.

pour modifier le nombre maximal de connexions WS2p sortantes :

    duniter config --ws2p-max-private <count>

Pour ajouter un clé a votre liste de clés préférés :

    duniter config --ws2p-prefered-add <pubkey>
    
Pour supprimer une clé de votre liste de clés préférés :

    duniter config --ws2p-prefered-rm <pubkey>
    
Pour consulter la liste de vos clés préférés :
    
    duniter ws2p list-prefered

Si vous le souhaitez vous pouvez transformer cette liste de clés préférés en liste de clés autorisés, et ainsi interdire a votre noeud de se connecter à un autre noeud dont la clé ne se trouverai pas dans votre liste, il suffit pour cela d'activer l'option `--ws2p-prefered-only` :

    duniter config --ws2p-prefered-only

Il n'existe pas encore de commande pour désactiver cette option, il vous faudra modifier manuellement votre fichier de configuration et remplacer `true` par `false` dans la ligne `"ws2pPreferedOnly": true`

###### WS2PTOR Privé

Pour demander a votre noeud duniter de passer par Tor dans les connexions privés qu'il établi avec d'autres noeuds il vous suffit de définir un proxy tor et de choisir la politique a adopter vis à vis des points d'accès ws2p normaux (option `--reachnig-clear-ep`) :

    duniter config --tor-proxy localhost:9050 --reachnig-clear-ep tor

Vous devrez en plus installer le *Tor Browser* ou *Tor Standalone* sur la même machine. Par défaut Tor écoute sur localhost sur le port 9050, si vous changez votre configuration de tor vous devrez évidemment mofidier la configuration de Duniter en conséquence.

Vous pouvez également opter pour un neoud mixte, qui contactera en clair les points d'accès classiques et qui ne se servira donc de Tor que pour contacter les point d'accès en .onion : 

    duniter config --tor-proxy localhost:9050 --reachnig-clear-ep clear

Enfin 3ème choix, vous pouvez décider de ne contacter que les points d'accès en .onion, les points d'accès en clair ne seront jamais contacter :

    duniter config --tor-proxy localhost:9050 --reachnig-clear-ep none

/!\ Chaque fois que vous modifiez l'une de ses 2 options vous devez répéter l'autre en même temps sinon elle est réinitialisée !

Enfin pour réinitialiser votre config Tor et revenir a un noeud parfaitement classique : 

    duniter --rm-proxies

Vous pouvez aussi décider d'encapsuler Duniter dans une VM Tor comme whonix, dans ce cas vous devez informer duniter qu'il sera capable de contacter les points d'accès en .onion en activant l'option `--force-tor` :

    duniter config --force-tor --reachnig-clear-ep tor|none

##### WS2P Public

Ce mode est désactivé par défaut, pour qu'il fonctionne vous devez configurer un point d'accès que les autres nœuds duniter pourront utilisé pour vous joindre.

Tout d'abord activez le mode WS2p public

    duniter config --ws2p-public
    
###### Point d'Accès
    
Pour que le WS2P Public fonctionne vous devez configurer un point d'accès que les autres nœuds duniter pourront utilisé pour vous joindre. il y a deux cas possibles : 

1. Vous souhaitez utiliser l'UPnP (activé par défaut) et alors vous n'avez rien a faire, duniter vas commander automatiquement votre box pour configurer un point d'accès.

2. Vous n'avez pas l'UPnP ou ne souhaitez pas l'utiliser, vous devez alors configurer manuellement un point d'accès : 

    duniter config --ws2p-noupnp --ws2p-port PORT --ws2p-host HOST --ws2p-remote-port REMOTE_PORT --ws2p-remote-host REMOTE_HOST
    
*Les options “remote” correspondent par exemple à une box qui ferait un NAT vers votre machine, ou à un nginx/apache qui ferait un reverse proxy vers votre instance Duniter.*
Si votre nœud duniter est connecté a internet par l'intermédiaire d'une box, vous devrez configurer une redirection de port sur votre box en redirigeant le port de votre choix vers la machine qui éxécute votre nœud duniter. De plus, afin que l'ip locale de cette machine ne change pas, vous devez demander a votre box de lui attribuée un bail DHCP permanent.

###### Point d'Accès WS2PTOR

il vous suffit d'indiquer l'adresse .onion de votre hidden service dans l'option `--ws2p-remote-port` et Duniter ce configurera automatiquement en mode WS2PTOR.

###### Nombre maximal de connexions WS2p Publiques

Pour modifier le nombre maximal de connexions WS2p entrantes :

    duniter config --ws2p-max-public <count>

###### Liste des clés invitées/privilégiées 

De la même façon que vous pouvez définir des clés préférés pour vos connexions WS2p sortantes, vous pouvez définir des clés invitées qui seront alors privilégiées. C'est a dire que si vous recevez plus de demande de connexion que le nombre maximal que vous avez configuré, les connexions initiés par des nœuds dont la clé publique fait partie de vos clés privilégiées seront prioritaires.

Pour ajouter un clé a votre liste de clés privilégiées  :

    duniter config --ws2p-privileged-add <pubkey>

Pour supprimer une clé de votre liste de clés privilégiées :

    duniter config --ws2p-privileged-rm <pubkey>

Pour consulter la liste de vos clés privilégiées :

    duniter ws2p list-privileged

Si vous le souhaitez vous pouvez transformer cette liste de clés privilégiées en liste de clés autorisés, et ainsi refuser toute connexion d'un autre noeud dont la clé ne se trouverai pas dans votre liste, il suffit pour cela d'activer l'option `--ws2p-privileged-only` :

    duniter config --ws2p-privileged-only

Il n'existe pas encore de commande pour désactiver cette option, il vous faudra modifier manuellement votre fichier de configuration et remplacer `true` par `false` dans la ligne `"ws2pPrivilegedOnly": true`.
    
##### Checker votre configuration WS2p

    duniter ws2p show-conf
    
##### Définir un patch pour votre point d'accès ws2p

    duniter config --ws2p-remote-path <path>
    
A n'utiliser que si vous souhaitez placer votre noeud duniter derrière un reverse proxy.
Cette option vous permet de rajouter un chemin pour votre point d'accès ws2p public.
Votre point d'accès ws2p sera alors : `ws://host:port/patch`

Notez que ws:// est a remplacé par wws:// si vous réglez le remote port sur 443.

#### Configurer BMA

la seule chose que vosu devez configurer c'est un point d'accès. Répondez au questions de la commande interactive suivante :

    duniter wizard network
    
Voici un exemple avec ma propre configuration chez moi :

    2017-10-01T19:02:09+02:00 - debug: Plugging file system...
    2017-10-01T19:02:09+02:00 - debug: Loading conf...
    2017-10-01T19:02:10+02:00 - debug: Configuration saved.
    ? IPv4 interface eth0 192.168.0.11
    ? IPv6 interface None
    ? Port 10901
    ? Remote IPv4 81.64.137.147
    ? Remote port 10901
    ? Does this server has a DNS name? No
    2017-10-01T19:02:33+02:00 - debug: Configuration saved.
    
Je suis en filaire, sinon en wifi il faut choisir l'option wlan0.
Max box ne supporte hélas pas l'ip v6, donc pas d'interface Ipv6 : None
Je n'utilise pas l'UPnP donc je défini manuellement un port (ici 10901).
Remote IPv4 correspond a l'ip publique de ma box, vous pouvez la connaitre en visitant le site https://www.monip.org/
Ici je n'ai pas configuré de domaine DNS pointant sur mon nœud duniter.

Si comme moi vous n'utilisez pas UPnP, vous devez configurer manuellement une redirection de port sur votre box.

#### Qu'est ce que l'UPnP ?

L’Universal Plug and Play (UPnP) est un protocole qui, s'il est activé sur votre box internet, permet aux programmes que vous utilisez de configurer eux même le réseau en "commandant" votre box.  
L'UPnP à l'avantage d'être pratique car il vous évite d'avoir a configurer vous même le réseau, mais en contrepartie vous devez faire confiance aux programmes que vous utilisez car un programme malveillant peut utiliser l'UPnP pour ouvrir votre réseau de manière non désirée.  
Si vous n'avez pas peur de la ligne de commande et que vous êtes exigeant sur la sécurité de votre réseau local, nous vous recommendons de désactiver l'UPnP.  
Si vous installez duniter sur un VPS ou un serveur dédié vous devrez de toute façon faire sans UPnP.

#### Note sur le WS2P public (recommandé)
    
Il faut nécessairement des nœuds avec ws2p public pour que le réseau duniter fonctionne, et plus il y a de nœuds avec ws2p public, plus le réseau est décentralisé.  
Ce mode est facultatif ne serait-ce parce que techniquement il est parfois dificile voir impossible d'être accessible par l'extérieur (nœud derrière un routeur 4G par exemple).

### Checker votre configuration

Pour vérifier que votre configuration ne comporte pas d'erreur logique vous pouvez utiliser la commande `check-config` :

    $ duniter check-config
    2017-09-28T23:24:19+02:00 - debug: Plugging file system...
    2017-09-28T23:24:19+02:00 - debug: Loading conf...
    2017-09-28T23:24:19+02:00 - debug: Configuration saved.
    2017-09-28T23:24:19+02:00 - warn: Configuration seems correct.

SI vous obtenez le résultat **Configuration seems correct** c'est que votre configuration semble correcte.

### Synchroniser votre nœud

Pour rejoindre le réseau d'une monnaie vous devez vous synchroniser avec un nœud déjà sur ce réseau :

    duniter sync DUNITER_NODE_HOST DUNITER_NODE_PORT

Pour la Ğ1, si vous ne connaissez aucun nœud vous pouvez choisir le noeud officiel `g1.duniter.org 10901`

### Lancement

Il existe 4 commandes différentes selon que vous voulez daémoniser ou pas votre instance Duniter et selon que vous voulez ou pas utiliser la web-ui : 

    duniter start
    duniter direct_start
    duniter webstart
    duniter direct_webstart

le préfixe `direct_` annule la daémonisation, mais vous devrez alors laisser votre terminal ouvert ou utiliser nohup ou screen ou similaire.

De plus les commandes `direct_start` et `direct_webstart` acceptent l'option `--keyprompt` (cf. partie trousseau de clés).

### Suivre les log

    duniter logs

Équivaut à :

    tail -f ~/.config/duniter/duniter-default/duniter.log

### Aller plus loin

Consultez le guide des [commandes duniter](https://duniter.org/fr/wiki/duniter/commandes).

## Via l'interface d'administration web

(wiki en cours de rédaction...)
