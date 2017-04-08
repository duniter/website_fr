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
   
## Démarrer/Arrêter son nœud

Un nœud Duniter tourne généralement en tâche de fond. Duniter fourni plusieurs commandes afin d'être démarré/arrêté dans différends modes de fonctionnement.

### `start`

Démarre le nœud Duniter *sans interface graphique*, en tâche de fond. Le seul moyen de communiquer avec le nœud en tant qu'administrateur est de consulter ses logs avec `duniter logs`.

### `stop`

Stoppe un nœud Duniter qui tournerait en tâche de fond. Si aucun nœud ne tourne, la commande ne fait rien.

### `status`

Dit si le nœud est actuellement lancé en tâche de fond ou non.

### `restart`

Raccourci pour `stop` suivi d'un `start`. Si aucun nœud n'était lancé, la commande équivaut alors à un simple `start`.

### `webstart`

Démarre le nœud Duniter *avec interface graphique*, en tâche de fond.

Le nœud est alors accessible graphiquement à l'adresse [localhost:9220](http://localhost:9220).

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
