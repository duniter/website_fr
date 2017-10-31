Title: II. Installation des outils
Order: 1
Date: 2017-10-31
Slug: chapitre-2-outils
Authors: cgeek

Nous n'utiliserons ici que des logiciels libres afin que n'importe qui puisse réaliser librement ce tutoriel :

* [Git](https://git-scm.com/)
* [NodeJS v6 ou supérieur](https://nodejs.org)
* [Yarn](https://yarnpkg.com/lang/en/docs/install/)
* [VSCode](https://code.visualstudio.com/)

Voilà, c'est tout. Nous vous laissons le soin d'installer ces logiciels par vous-même.

> Si vous utilisez un Linux/Mac, nous vous conseillons d'installer NodeJS via [NVM](https://github.com/creationix/nvm#installation).

## Outils de compilation

Il reste toutefois à installer quelques outils de compilation propres à votre système d'exploitation.

### Linux

Sous Ubuntu :

    sudo apt-get install build-essential

Sous Debian :

    sudo apt-get install build-essentials

Autre distribution : installer `gcc`, `g++`, `make` et `python2`.

### Windows

#### .NET Framework 4.5

Rendez-vous à l'adresse : [https://www.microsoft.com/fr-fr/download/details.aspx?id=30653](https://www.microsoft.com/fr-fr/download/details.aspx?id=30653)

#### Outils de compilation

Lancez un invité de commande **avec les droits administrateur** puis lancez la commande :

    npm install --global --production windows-build-tools

Cette commande peut durer 1h ou plus en fonction des composants déjà installés sur votre système.

## Fin de l'installation

Pour terminer correctement l'installation, nous vous conseillons de *fermer vos terminaux et relancer VSCode* si vous l'aviez ouvert. En effet certaines variables d'environnement ont été mises à jour par les installations précédentes, et ne seront disponbiles qu'après redémarrage des logiciels.

Vous pouvez ensuite passer au chapitre suivant : [Chapitre III. Récupération du code source](../chapitre-3-source).
