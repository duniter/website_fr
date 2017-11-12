Title: 3. Récupération du code source
Order: 1
Date: 2017-10-31
Slug: chapitre-3-source
Authors: cgeek

Duniter est un logiciel libre, son code source est donc librement disponible.

L'objectif de ce chapitre est de récupérer ce code afin de pouvoir l'exécuter puis le modifier.

## Copie des sources

À l'aide d'un terminal (celui de votre système ou celui présent dans VSCode > Afficher > Terminal intégré), récupérez le code source de Duniter présent sur la branche de développement :

    git clone https://github.com/duniter/duniter.git -b dev

Comme vous pouvez le remarquer, nous utilisons ici la branche `dev`. En effet la branche `master` constitue plutôt la branche stable sur laquelle sont basées les versions de production du logiciel, tandis que la branche `dev` est utilisée pour les développements en cours.

## Installation des dépendances

Duniter repose sur plusieurs bibliothèques de code tierces, ou *dépendances*. Pour que le code fonctionne il faut donc les installer :

    yarn

> <span class="icon">![](/fr/images/icons/warning.png)</span> Attention pour les habitués de NodeJS : **ne remplacez pas `yarn` par `npm`**, car ce dernier ne permet pas d'avoir rigoureusement les mêmes versions des dépendances d'un poste à l'autre, or sans cette assurance nous ne pouvons pas garantir que le code fonctionnera comme attendu sur votre poste.

## Exécuter les tests automatisés

À ce stade, les tests automatisés devraient passer avec succès :

    yarn test

Patientez, les tests peuvent prendre jusqu'à 2-3 minutes. Finalement, vous obtenez :

      687 passing (2m)

    Done in 119.39s.

Il se peut que quelques tests échouent en fonction des performances de votre machine, certains tests y étant sensibles. S'il n'y en a qu'une dizaine ou moins qui échouent, vous pouvez considérer que Duniter fonctionne sur votre machine et que le code source est correctement récupéré.

### Couverture du code

La commande que nous venons d'exécuter a créé un dossier `coverage`, qui contient des informations très importantes : celles de la *couverture du code*, c'est-à-dire une information sur les lignes qui ont été exécutées durant les tests automatisés. Ainsi une ligne est dite *couverte* si au moins une exécution a été réalisée par l'un des tests automatisés. Cela permet d'être un peu plus confiant dans le fait que cette ligne de code s'exécute correctement.

Vous pouvez visualiser et étudier la couverture du code est ouvrant le fichier `coverage/index.html` dans votre navigateur :

![](/fr/images/tuto-dev/coverage.png)

> Passer à la suite du tutoriel : [Chapitre 4. Démarrage](../chapitre-4-demarrage).
