Title: Configurer un nœud Duniter
Order: 9
Date: 2017-09-22
Slug: configurer
Authors: elois

Ce document est un petit tutoriel pour configurer votre nœud Duniter fraichement installé,  c'est la suite logique du [tutoriel d'installation](https://duniter.org/fr/wiki/duniter/installer)

## Sommaire

* [Duniter versions 1.6.x (avec WS2P)](#version-16x)
    * [En ligne de commande](#en-ligne-de-commande)
    * [Via l'interface d'administration web](#via-linterface-dadministration-web)

----

# Version 1.6.x

## En ligne de commande

### Configurer le trousseau de clés cryptographiques

Tout les nœuds duniter ont un trousseau de clés, qu'ils utilisent pour signer les informations qu'il transmettent sur le réseau. Il y a deux types de nœuds duniter :

1. les nœud membres : Si le trousseau de clé du nœud correspond a une identité membre, alors le nœud est de type "membre", et 
va automatiquement prendre part au calcul des blocs.

2. Si le trousseau de clé du nœud ne correspond pas à une identité membre, alors le nœud est de type "miroir", il ne pourra pas écrire de bloc, mais sera quand même utile pour la résilience du réseau ainsi que pour répondre aux requêtes des clients.

Par défaut se trousseau est aléatoire, et le nœud duniter est donc un nœud miroir. Vous pouvez modifier le trousseau de clés du noeud avec cette commande :

    duniter wizard key

Attention le trousseau de clés renseigner via cetet commande sera stocké en clair sur le disque !
Pour éviter cela vous pouvez choisir de ne renseigner le trousseau de clés a utiliser qu'au lancement du nœud afin que votre trousseau de clés reste seulement en mémoire vive, pour cela ajoutez l'option `--keyprompt` a la commande de lancement du nœud.
    
### Configurer le réseau

#### BMA (facultatif)

    duniter config --bma # Activation de BMA
    duniter wizard network # Configuration du réseau BMA

#### WS2P privé
    
Choisir la liste des nœuds préférés et des nœuds invités.
    
Ajouter des noeuds préférés (via leur clé publique) :
    
    duniter config --ws2p-prefered-add <pubkey> 
    
Supprimer des noeuds de la liste des préférés : 
    
    duniter config --ws2p-prefered-rm  <pubkey>
    
Ajouter des noeuds à la liste des invités (via leur clé publique) :
    
    duniter config --ws2p-privileged-add <pubkey> 
    
Supprimer des noeuds de la liste des invités: 
    
    duniter config --ws2p-privileged-rm <pubkey>
    
Voir les listes : 

    duniter ws2p list-nodes
    duniter ws2p list-prefered
    duniter ws2p list-privileged
    
#### WS2P public (recommandé)
    
    Vous pouvez rendre l'accès a votre API WS2p public, plus il y a de nœuds avec ws2p public et plus le réseau est décentralisé.

##### Avec upnp

    duniter config --ws2p-public

#### SANS upnp
    
    duniter config --ws2p-public --ws2p-noupnp --ws2p-port 7778 --ws2p-host 37.187.192.109 --ws2p-remote-port 7778  --ws2p-remote-host 37.187.192.109

Les options “remote” correspondent par exemple à une box qui ferait un NAT vers votre machine, ou à un nginx/apache qui ferait un reverse proxy vers votre instance Duniter.

Vérifiez que la configuration ws2p correspond bien a ce que vous voulez :

    duniter ws2p show-conf

### Synchroniser votre nœud

Pour rejoindre le réseau d'une monnaie vous devez vous synchroniser avec un nœud déjà sur ce réseau :

    duniter sync DUNITER_NODE_HOST DUNITER_NODE_PORT

Pour la Ğ1, si vous ne connaissez aucun nœud vous pouvez choisir le noeud officiel `g1.duniter.org 10901`

### Lancement

Il existe 4 commandes différentes selon que vous voulez démoniser ou pas votre instance Duniter et selon que vous voulez ou pas utiliser la web-ui : 

    duniter start
    duniter direct_start
    duniter webstart
    duniter direct_webstart

le préfixe `direct_` annule la démonisation, mais vous devrez alors laisser votre terminal ouvert ou utiliser nohup ou screen ou similaire.

De plus les commandes `direct_start` et `direct_webstart` acceptent l'option `--keyprompt` (cf. partie trousseau de clés).

### Suivre les log

    tail -f .config/duniter/duniter-default/duniter.log

### Aller plus loin

Consultez le guide des [commandes duniter](https://duniter.org/fr/wiki/duniter/commandes).

## Via l'interface d'administration web

(wiki en cours de rédaction...)
