Title: Commandes Duniter
Order: 9
Date: 2017-04-08
Slug: commandes
Authors: cgeek

Voici un guide des différentes commandes de l'exécutable `duniter` en ligne de commande.

## Initialiser son nœud

### `duniter wizard key`

Permet de configurer le trousseau cryptographique utilisé par votre nœud. C'est à travers ce trousseau que votre nœud peut être identifié et ses réponses authentifiées, vérifiées.

Ce trousseau est composé d'une clé privée et d'une clé publique Ed25519.

    duniter wizard key
    ? Modify you keypair? Yes
    ? Key's salt *****************
    ? Key's password ********************

### `duniter wizard network`

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

