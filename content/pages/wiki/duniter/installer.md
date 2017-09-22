Title: Installer un nœud Duniter
Order: 9
Date: 2017-06-19
Slug: installer
Authors: cgeek

Ce document est un petit guide pour installer et déployer votre propre instance Duniter pour :

* soit participer à l'écriture de la blockchain (vous devez être membre)
* soit avoir un nœud miroir, qui réplique la blockchain et en conserve une copie

## Sommaire

* [Version Bureau](#version-bureau)
    * [GNU/Linux](#gnulinux)
        * [Ubuntu 64 bits](#ubuntu-64-bits)
        * [Debian 64 bits](#debian-64-bits)
        * [Autres distributions](#autres-distributions)
    * [Windows](#windows)
    * [MacOS](#macos)
* [Version Serveur](#version-serveur)
    * [GNU/Linux](#gnulinux_1)
        * [Ubuntu/Debian package (64 bits)](#ubuntudebian-package-64-bits)
        * [YunoHost](#yunohost)
        * [Compilation manuelle](#compilation-manuelle)
        * [Docker](#docker)
  * [Windows](#windows-1)

----

# Version Bureau

Une machine de bureau vous facilitera la tâche pour gérer votre instance Duniter grâce à son interface graphique.

Votre instance fonctionnera tant que votre machine et que le logiciel ne sont pas éteints. Si vous fermez le logiciel ou éteignez votre machine, Duniter sera en mesure de se resynchroniser avec le réseau une fois la machine et Duniter redémarrés.

## GNU/Linux

### Ubuntu 64 bits

1. Allez sur la [page de la dernière version publiée](https://github.com/duniter/duniter/releases/latest) et téléchargez le fichier `duniter-desktop` qui se termine par l'extension `.deb`.
  <br>
  <img src="../../../images/wiki/duniter/installer/ubuntu_file.png" width="500" height="106">

2. Procédez à l'installation en double-cliquant sur le fichier téléchargé (`.deb`)
  > Note : si l'installation échoue, vous avez possiblement un soucis avec le centre logiciel Ubuntu. Préférez alors l'installation en ligne de commande avec `dpkg`. Exemple : `sudo dpkg -i duniter-desktop-v1.3.9-linux-x64.deb`.

3. Utilisez ensuite le Dash Ubuntu et cherchez "Duniter", puis cliquez sur l'icône Duniter pour lancer le logiciel :
  <img src="../../../images/wiki/duniter/installer/ubuntu_dash.png" width="536" height="246">

### Debian 64 bits

1. Allez sur la [page de la dernière version publiée](https://github.com/duniter/duniter/releases/latest) et téléchargez le fichier `duniter-desktop` qui se termine par l'extension `.deb`.

2. Procédez à l'installation à l'aide d'un clic droit sur le fichier téléchargé, option `GDebi` (ou préférez l'installation avec `dpgk`, comme mentionné dans l'installation Ubuntu ci-dessus).
  <img src="../../../images/wiki/duniter/installer/deb_gdebi.png" width="460" height="202">

3. Utilisez Gnome Shell et cherchez "Duniter" puis cliquez sur son icône pour le lancer.
  <img src="../../../images/wiki/duniter/installer/deb_gnome.png" width="690" height="428">

> Note : vous pouvez aussi lancer Duniter avec la commande `duniter-desktop`. Lancer via cette commande ou via l'icône est équivalent.

### Autres distributions

#### Archive `.tar.gz`

1. Allez sur la [page de la dernière version publiée](https://github.com/duniter/duniter/releases/latest) et téléchargez le fichier `duniter-desktop` qui se termine par l'extension `.tar.gz`.

2. Décompressez le fichier téléchargé, par exemple avec la commande : `tar zxvf duniter-*.tar.gz`

3. **Placez-vous dans le répertoire décompressé**, puis lancez Duniter avec la commande `./nw`.

## Windows

1. Allez sur la [page de la dernière version publiée](https://github.com/duniter/duniter/releases/latest) et téléchargez le fichier `duniter-desktop` qui se termine par l'extension `.exe`.

2. Procédez à l'installation en double-cliquant sur le fichier `.exe` téléchargé.
  <img src="../../../images/wiki/duniter/installer/win_fichier.png" width="591" height="39">
  > Il se peut que le fichier téléchargé n'ai pas l'extension `.exe`. C'est Windows qui a retiré l'extension lors du téléchargement pour vous protéger. Vous pouvez contourner ce problème en renommant le fichier téléchargé et en ajoutant `.exe` à la fin du nom de fichier.

3. Suivez la procédure d'installation.
  <br>
  <img src="../../../images/wiki/duniter/installer/win_install.png" width="503" height="387">

4. Duniter est maintenant installé, par défaut celui-ci est lancé à la fin de l'installation. Vous pourrez aussi le lancer via le menu "Démarrer > Programmes > Duniter > Duniter".
  <br>
  <img src="../../../images/wiki/duniter/installer/win_programme.png" width="271" height="58">

## MacOS

Il n'existe pas de version pour MacOS. Toutefois, vous pouvez toujours compiler la version Serveur ci-dessous.

# Version Serveur

Pour les utilisateurs les plus avancés, une version serveur vous permet d'avoir un nœud allumé 100% du temps, en l'installant sur une machine elle-même toujours allumée.

Vous pourrez contrôler votre instance à l'aide d'outils en ligne de commande, mais vous aurez également accès à l'interface graphique via un navigateur web.

> Lorsque vous en aurez fini avec l'installation, vous pourrez consulter [la documentation des commandes Duniter](https://duniter.org/fr/wiki/duniter/commandes/).

## GNU/Linux

### Ubuntu/Debian package (64 bits)

1. Allez sur la [page de la dernière version publiée](https://github.com/duniter/duniter/releases/latest) et téléchargez le fichier `duniter-server` qui se termine par l'extension `.deb` (choisissez bien entre la version x64 ou la version ARM).

2. Procédez à l'installation en lançant `dpkg -i` suivi du nom du fichier téléchargé. Ceci requiert des privilèges administrateur.
                
        dpkg -i [downloaded_file_name].deb

3. Démarrez votre nœud en tâche de fond avec :

        duniter start
        
4. Consultez [les commandes Duniter](https://duniter.org/fr/wiki/duniter/commandes/) pour manipuler votre nœud.

### YunoHost

Un [paquet YunoHost](https://github.com/duniter/duniter_ynh) est disponible.

### Compilation manuelle

Duniter peut être compilé sur la majorité des machines Linux (32 bits ou 64 bits) en cinq étapes (les deux premières ne sont à réaliser qu'une seule fois) :

**1. Installation de  Node.js**

un outil vous permet d'installer la version de Node.js que vous souhaitez, en changer quand vous voulez et sans conflit avec une version précédente : il s'agit de [nvm](https://github.com/creationix/nvm).

Vous pouvez installer nvm avec la commande suivante :

    curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.4/install.sh | bash
    
Fermez puis rouvrez votre terminal, comme indiqué. Puis, installez Node.js (choisissez la version 6) :

    nvm install 6

Vous aurez alors la dernière version de la branche 6.x de Node.js prête à l'emploi.

**2. Installation de  [yarn](https://yarnpkg.com/)**

Yarn est un gestionnaire de dépendances plus rapide et plus fiable que celui intégré de base dans npm, cela vous évitera des erreurs dues a des conflits de version par exemple.
le plus propre est d'ajouter leur dépôt puis d'installer le paquet `yarn` :

    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
    sudo apt-get update && sudo apt-get install yarn

**3. Téléchargement de  Duniter**

Allez sur la [page de la dernière version publiée](https://github.com/duniter/duniter/releases/latest) et téléchargez le fichier `Source code (tar.gz)`.

**4. Lancer l'installation depuis le dossier décompressé `duniter/` :**
  > N.B. : **ne lancez pas ces commandes en tant que `root`.** [Cela ne fonctionnera pas, nous le savons](https://github.com/duniter/duniter/issues/412).

        cd duniter
        yarn 

**5. Utiliser [les commandes Duniter](https://duniter.org/fr/wiki/duniter/commandes/)** en préfixant `duniter` par `bin/`. Exemple : 

        bin/duniter --version

### Docker

Non disponible.

## Windows

Il n'y a pas de version spécifique pour Serveur Windows. Utilisez simplement la version [Duniter pour Bureau Windows](#windows).
