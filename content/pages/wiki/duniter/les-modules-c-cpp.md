Title: Les modules C/C++
Order: 9
Date: 2017-05-22
Slug: les-modules-c-cpp
Authors: cgeek

Duniter est écrit à plus de 96% en JavaScript, exécuté par le moteur [Node.js](https://nodejs.org). Toutefois certaines parties gourmandes en calcul nécessitent l'utilisation des langages C/C++ pour une exécution rapide. Ces parties ont été externalisées dans des modules à part, dont vous trouverez la liste ci-dessous.

## [wotb](https://github.com/duniter/wotb)

Module qui stocke et traite les données de la WoT. Il associe à chaque membre un entier, puis stocke une matrice des membres avec leurs liens.

### Fonctionnalités

Ce module permet : 

* de faire du calcul de distance entre membres
* de connaître les chemins possibles d'un membre à un autre

### Auteurs

Écrit initialement par cgeek en C, puis refactorisé par mmpio en C++.

### Tester

Tout d'abord, procéder à la copie des sources et à la compilation : 

    git clone https://github.com/duniter/wotb.git && cd wotb
    npm install --build-from-source

#### En JavaScript

C'est le plus haut niveau, le plus complet. Ce niveau englobe tous les appels que fera finalement Duniter à ce module.

    npm test
    
#### En C++

Le C++ se décompose en deux parties :

1) le code métier du module C++
2) l'enrobage qui fait le lien entre JavaScript et le coder métier

Tout le code du point 1) se trouve dans le fichier `functions.cc`.

Tout le code du point 2) se trouve dans le dossier `wotcpp/`.

Il  est possible de travailler indépendamment sur 2), en se positionnant dans le dossier `wotcpp/` puis en utilisant CMake. Il est possible de tester le module à travers le fichier `main.cpp`.

## [naclb](https://github.com/duniter/naclb)

Module d'enrobage permettant d'utiliser la librairie NaCl en C++ dans un contexte Node.js (donc JavaScript). Permet de réaliser les opérations de crypto à la vitesse du C++, plutôt que du JS.

Ce module diminue le contenu initial de la librairie NaCl, certaines parties n'ayant pas été compilables aisément, elles ont été tout bonnement supprmées. Aucun ajout ni aucune modification n'ont été faites en dehors de ces suppressions à la librairie NaCl.

### Auteurs

Écrit par cgeek en C++.

### Tester

Tout d'abord, procéder à la copie des sources et à la compilation : 

    git clone https://github.com/duniter/naclb.git && cd naclb
    npm install --build-from-source

#### En JavaScript

Le module ne se teste qu'en JavaScript, bien qu'il pût être aussi testé en C++.

    npm test
    
## [node-scrypt](https://github.com/c-geek/node-scrypt)

Fork de https://github.com/barrysteyn/node-scrypt permettant une compilation correcte de Duniter pour Windows. 

## [node-sqlite3](https://github.com/mapbox/node-sqlite3)

Module externe donnant accès à une base de données SQLite.
