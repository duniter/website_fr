Title: 4. Démarrage
Order: 1
Date: 2017-10-31
Slug: chapitre-4-demarrage
Authors: cgeek

Maintenant que les sources de Duniter sont installées, nous allons exécuter quelques commandes afin de mettre votre nœud local de développement sur pied :

* initialiser les données en se synchronisant sur le réseau Ğ1
* démarrer le nœud

Notez qu'il n'y a aucun danger à connecter votre nœud de développement sur le réseau Ğ1, vous ne perturberez en rien le réseau si vous faites de mauvaises manipulations avec votre nœud suite à une modification du code par exemple. Le réseau est robuste et, en cas d'anomalie avec votre nœud, les communications seront simplement coupées avec lui.

Ensuite, nous expérimenterons le démarrage du nœud dans l'éditeur VSCode en mode debug afin de voir le lien avec le code source.

## Synchronisation

Pour initialiser votre nœud, il vous suffit de télécharger et d'appliquer la blockchain Ğ1 :

    node bin/duniter sync g1.duniter.org 443

Nous initions ici le téléchargement de la blockchain depuis le nœud `g1.duniter.org`, mais en réalité le téléchargement se fera en P2P depuis l'ensemble du réseau Ğ1 afin d'optimiser la procédure. Indiquer le nœud `g1.duniter.org` permet juste de donner un point d'entrée sur le réseau, mais aussi d'indiquer que l'on souhaite la blockchain dont le bloc courant est celui de `g1.duniter.org`, ce qui permet d'identifier l'intégralité du reste de la blockchain.

> En effet, chaque bloc référençant son précédant par une fonction de hachage, à partir d'un bloc donné on est capable de s'assurer du contenu de tous les blocs précédents. Ainsi il est possible de télécharger les blocs de la blockchain sur n'importe quel nœud du réseau tout en étant assuré de son contenu, une fois précisé le bloc le plus haut (aussi appelé `HEAD`) ! Ici, nous demandons à avoir le même `HEAD` que celui possédé par le nœud `g1.duniter.org`.

## Lancez votre nœud

À ce stade, votre nœud devrait pouvoir se lancer et se connecter au réseau Ğ1 et agir en tant que miroir (nœud passif du réseau) :

    node bin/duniter direct_start

Pour arrêter Duniter, terminez le processus (Ctrl+C).

Vous avez désormais un nœud prêt à fonctionner, et que vous pouvez même modifier ! Soit pour changer un comportement existant, ou ajouter une nouvelle fonctionnalité. Mais avant cela, voyons comment « déboguer » le code source.

## Débogage dans VSCode

Le débogage nécessite une configuration de VSCode pour le projet. Afin de faciliter la prise en main initiale, un dossier « de base » a été initié, que vous pouvez copier pour votre utilisation :

    cp -r doc/.vscode .vscode

À partir de là, à l'aide de la combinaison de touches Ctrl+Shift+D, vous pouvez sélectionne la configuration de débogage souhaitée :

![](/fr/images/tuto-dev/debug_selection.png)

Vous pouvez sélectionner la configuration `MOCHA ALL TESTS` dans un premier temps, puis appuyer sur la touche `F5`. VSCode devrait alors lancer les tests automatisés de Duniter, ce qui peut durer plusieurs minutes :

![](/fr/images/tuto-dev/debug_tests_done.png)

### Point d'arrêt

À tout moment, vous pouvez placer un point d'arrêt dans le code. **C'est votre meilleure arme pour étudier et comprendre le fonctionnement du code**, apprenez à placer des points d'arrêt aux endroits qui vous intéressent.

Par exemple, plaçons un point d'arrêt dans le fichier `app/modules/daemon.ts` :

![](/fr/images/tuto-dev/debug_direct_start.png)

Puis lançons le débogage sur `direct_start` :

![](/fr/images/tuto-dev/debug_direct_start_launcher.png)

Alors, VSCode lance `node bin/duniter direct_start` en mode debug, et nous permet d'atterir dans le code dont l'exécution est suspendue au point d'arrêt :

![](/fr/images/tuto-dev/debug_point_suspendu.png)

Nous avons ici une foule d'informations disponibles ! Nous pouvons placer le curseur de la souris sur une variable pour avoir son contenu, nous déplacer dans la pile des appels, ajouter des espions, etc. Ce sont là des informations extrêmement précieuses, notamment quand le code devient plus complexe.

### Modifier le code

Une subtilité à retenir est que le code source est écrit en TypeScript, mais l'exécution se fait en JavaScript via NodeJS. Donc, si l'on modifie un fichier de code source comme `daemon.ts` par exemple, il nous faut réaliser une étape de *transpilation* de TypeScript vers JavaScript.

La façon manuelle de le faire dans Duniter est avec yarn :

    yarn tsc
    yarn tsc v1.0.1
    $ tsc
    Done in 6.59s.

`tsc` est la commande « TypeScript Compiler », c'est notre transpilation. Quand la commande est terminée, `tsc` nous indique si l'opération s'est bien passée ou si des erreurs de transpilation sont apparues.

Toutefois cette opération est fastidieuse à la longue. Nous disposons d'une commande de « surveillance » des fichiers TypeScript et qui lance automatiquement la transpilation pour tout fichier `.ts` modifié :

    yarn tscw

Ce qui signifie « TypeScript Compiler Watch ». Dès lors, nous pouvons modifier n'importe quel fichier et la modification sera impactée à l'exécution.

**Sans `yarn tsc` ou `yarn tscw`, vous tomberez sur des erreurs de point d'arrêt refusant de suspendre le code ou d'obtenir un comportement de Duniter différent du code source**. Le plus simple est d'avoir un terminal à part, où `yarn tscw` s'exécute tranquillement. Ainsi, il est possible de modifier le code source sans se soucier de la transpilation suite à une modification du code.

> Passer à la suite du tutoriel : [Chapitre 5 : Architecture](../chapitre-5-architecture).
