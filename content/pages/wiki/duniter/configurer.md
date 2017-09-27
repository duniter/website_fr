Title: Configurer un nœud Duniter
Order: 9
Date: 2017-09-22
Slug: configurer
Authors: elois

Ce document est un petit tutoriel pour configurer votre nœud Duniter fraichement installé,  c'est la suite logique du [tutoriel d'installation](https://duniter.org/fr/wiki/duniter/installer).

## Sommaire

* [Duniter versions 1.6.x (avec WS2P)](#version-16x)
    * [En ligne de commande](#en-ligne-de-commande)
    * [Via l'interface d'administration web](#via-linterface-dadministration-web)

----

# Version 1.6.x

## En ligne de commande

### Configurer le trousseau de clés cryptographiques

Tout les nœuds duniter ont un trousseau de clés, qu'ils utilisent pour signer les informations qu'il transmettent sur le réseau. Il y a deux types de nœuds duniter :

**1. les nœuds membre :** Si le trousseau de clé du nœud correspond a une identité membre, alors le nœud est de type "membre", et 
va automatiquement prendre part au calcul des blocs.

**2. les nœuds miroir :** Si le trousseau de clé du nœud ne correspond pas à une identité membre, alors le nœud est de type "miroir", il ne pourra pas écrire de bloc, mais sera quand même utile pour la résilience du réseau ainsi que pour répondre aux requêtes des clients.

Par défaut ce trousseau est aléatoire, et le nœud duniter est donc un nœud miroir. Vous pouvez modifier le trousseau de clés du noeud avec cette commande :

    duniter wizard key

Attention le trousseau de clés renseigner via cette commande sera stocké en clair sur le disque !
Pour éviter cela vous pouvez choisir de ne renseigner le trousseau de clés a utiliser qu'au lancement du nœud afin que votre trousseau de clés reste seulement en mémoire vive, pour cela ajoutez l'option `--keyprompt` a la commande de lancement du nœud.
    
### Configurer le réseau


| les API                                              | BMA                                | WS2P Privé                                                                                                                                                                                                                                                                                                      | WS2P Public                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------------------------------------------|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Par défaut ?                                         | Désactivé                          | Activé                                                                                                                                                                                                                                                                                                          | Désactivé                                                                                                                                                                                                                                                                                                                                                                                                      |
| Rôle                                                 | API Client                         |  API inter-nœuds (La partie privée désigne les connexions que vous initiez, elles sont donc publiques pour les nœuds qui les reçoivent)                                                                                                                                                                         | API inter-nœuds public                                                                                                                                                                                                                                                                                                                                                                                         |
| Config minimale                                      | Automatique si upnp                | Automatique                                                                                                                                                                                                                                                                                                     | Automatique si UPnP Manuelle sans UpnP                                                                                                                                                                                                                                                                                                                                                                         |
| Activation                                           | `duniter config --bma`             | `duniter config --ws2p-private`                                                                                                                                                                                                                                                                                 | `duniter config --ws2p-public`                                                                                                                                                                                                                                                                                                                                                                                 |
| Désactivation                                        | `duniter config --nobma`           | `duniter config --ws2p-noprivate`                                                                                                                                                                                                                                                                               | `duniter config --ws2p-nopublic`                                                                                                                                                                                                                                                                                                                                                                               |
| Configurer votre point d'accès sans upnp             | `duniter wizard network`           | `duniter config --ws2p-noupnp --ws2p-port PORT --ws2p-host HOST --ws2p-remote-port REMOTE_PORT --ws2p-remote-host REMOTE_HOST` (*Les options “remote” correspondent par exemple à une box qui ferait un NAT vers votre machine, ou à un nginx/apache qui ferait un reverse proxy vers votre instance Duniter.*) | Les deux modes WS2P utilisent le même point d'accès                                                                                                                                                                                                                                                                                                                                                            |
| Nœuds autorisés a se connecter à votre point d'accès | tous                               | Aucun                                                                                                                                                                                                                                                                                                           | Tous, mais si vous recevez plus de demandes que le nombre max de connexions publiques que vous autorisés, les noeuds dont le trousseau de clé est dans votre liste `privileged` (=invités) seront prioritaires. Ajouter une clé : `duniter config --ws2p-privileged-add ` Supprimer une clé : `duniter config --ws2p-privileged-rm ` Voir votre liste d'invités(`privileged`),: `duniter ws2p list-privileged` |
| Nœuds auquels vous vous connecterez en priorité      | pas de notion de priorité dans BMA | Ceux dont le trousseau de clé est dans votre liste `prefered` (=préférés). Ajouter une clé: `duniter config --ws2p-prefered-add ` Supprimer une clé : `duniter config --ws2p-prefered-rm ` Voir la liste de vos invités : `duniter ws2p list-prefered`                                                          | Aucun, le WS2p public est uniquement récepteur de connexions.                                                                                                                                                                                                                                                                                                                                                  |
| Nombre maximal de connexions                         | pas de max                         | `duniter config --ws2p-max-private <count>`                                                                                                                                                                                                                                                                     | `duniter config --ws2p-max-public <count>`                                                                                                                                                                                                                                                                                                                                                                     |
| Vérifier votre configuration                         | `duniter wizard network`           | `duniter ws2p show-conf`                                                                                                                                                                                                                                                                                       | `duniter ws2p show-conf`                                                                                                                                                                                                                                                                                                                                                                                      |

#### Qu'est ce que l'UPnP ?

L’Universal Plug and Play (UPnP) est un protocole qui, s'il est activé sur votre box internet, permet aux programmes que vous utilisez de configurer eux même le réseau en "commandant" votre box.  
L'UPnP à l'avantage d'être pratique car il vous évite d'avoir a configurer vous même le réseau, mais en contrepartie vous devez faire confiance aux programmes que vous utilisez car un programme malveillant peut utiliser l'UPnP pour ouvrir votre réseau de manière non désirée.  
Si vous n'avez pas peur de la ligne de commande et que vous êtes exigeant sur la sécurité de votre réseau local, nous vous recommendons de désactiver l'UPnP.  
Si vous installez duniter sur un VPS ou un serveur dédié vous devrez de toute façon faire sans UPnP.

#### Note sur le WS2P public (recommandé)
    
Il faut nécessairement des nœuds avec ws2p public pour que le réseau duniter fonctionne, et plus il y a de nœuds avec ws2p public, plus le réseau est décentralisé.  
Ce mode est facultatif ne serait-ce parce que techniquement il est parfois dificile voir impossible d'être accessible par l'extérieur (nœud derrière un routeur 4G par exemple).

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
