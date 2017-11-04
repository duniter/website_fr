Title: IV. Connexion au réseau Ğ1
Order: 1
Date: 2017-10-31
Slug: chapitre-4-connexion
Authors: cgeek

Maintenant que les sources de Duniter sont installées, nous allons faire en sorte d'initialiser les données de notre nœud local de développement afin de pouvoir explorer le code source du nœud en fonctionnement « normal » sur le réseau Ğ1.

Notez qu'il n'y a aucun danger à connecter votre nœud de développement sur le réseau Ğ1, vous ne perturberez en rien le réseau si vous faites de mauvaises manipulations avec votre nœud suite à une modification du code par exemple. Le réseau est robuste et, en cas d'anomalie avec votre nœud, les communications seront simplement coupées avec vous.

## Synchronisation

Pour initialiser votre nœud, il vous suffit de télécharger et d'appliquer la blockchain Ğ1 :

    node bin/duniter sync g1.duniter.org 443

Nous initions ici le téléchargement de la blockchain depuis le nœud `g1.duniter.org`, mais en réalité le téléchargement se fera en P2P en téléchargeant les blocs depuis l'ensemble du réseau Ğ1 afin d'optimiser le téléchargement. Indiquer le nœud `g1.duniter.org` permet juste de donner un point d'entrée sur le réseau, mais aussi d'indiquer que l'on souhaite la blockchain dont le bloc courant est celui de `g1.duniter.org`, ce qui permet d'identifier l'intégralité du reste de la blockchain.

> En effet, chaque bloc référençant sont précédent par une fonction de hachage, à partir d'un bloc donné on est capable de s'assurer du contenu de tous les blocs précédents. Ainsi il est possible de télécharger les blocs de la blockchain sur n'importe quel nœud du réseau tout en étant assuré de son contenu, une fois précisé le bloc le plus haut (aussi appelé `HEAD`) ! Ici, nous demandons à avoir le même `HEAD` que celui possédé par le nœud `g1.duniter.org`.

## Lancez votre nœud

À ce stade, votre nœud devrait pouvoir se lancer et se connecter au réseau Ğ1 et agir en tant que miroir (nœud passif du réseau) :

    node bin/duniter direct_start

Pour arrêter Duniter, terminez le processus (Ctrl+C).

Vous avez désormais un nœud prêt à fonctionner, et que vous pouvez même modifier ! Soit pour changer un comportement existant, ou ajouter une nouvelle fonctionnalité. Mais pour simplifier cette étape, le mieux est d'étudier la suite : [Chapitre 5 : Architecture](../chapitre-5-architecture).