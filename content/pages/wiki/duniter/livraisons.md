Title: Livraisons
Order: 9
Date: 2017-05-10
Slug: livraisons
Authors: cgeek

> Cette page est un guide à destination des développeurs.

Duniter est livré sous la forme de différents binaires pour les environnements Linux et Windows :

##### Duniter Desktop

* Pour Debian (.deb)
* Pour Linux (archive tar.gz)
* Pour Windows (.exe)

##### Duniter Server

* Pour Debian (.deb)
* Pour Debian ARM (.deb)

La réalisation de ces livrables ainsi que leur mise à disposition est totalement automatisée. Les sections suivantes décrivent cette procédure.

## Pré-requis

N'importe qui peut réaliser la livraison de Duniter, c'est-à-dire produire et mettre à disposition les livrables précédemment cités, sous réserve de réunir les conditions suivantes :

* Être administrateur de l'organisation [Duniter sur GitHub](https://github.com/duniter)
* Disposer d'une machine Linux avec :
    * 4Go de RAM minimum
    * Bash
    * Node.js v6+
    * VirtualBox
    * Vagrant
    * Git

### Création d'un token GitHub

Pour créer la release GitHub et téléverser les livrables, les scripts de livraison s'attendent à trouver un jeton d'authentification dans le répertoire `~/.config/duniter/.github`.

Pour obtenir un tel jeton, rendez-vous à l'adresse https://github.com/settings/tokens puis générez un nouveau jeton en cochant la case « public_repo ».

Copiez alors le jeton généré, par exemple `b23ab3cbe624a8552545900d781a1779b928aa90`, puis enregistrez ce jeton :

    echo -n 'b23ab3cbe624a8552545900d781a1779b928aa90' > ~/.config/duniter/.github

## Procédure

### 1. Cloner Duniter et installer ses modules

    git clone git@github.com:duniter/duniter.git
    cd duniter
    npm install

### 2. Créer une nouvelle version

Cette opération se réalise sur n'importe quel branche, selon le besoin. Mais il est important de merger *ensuite* ces changements sur la branche `master`, notamment car l'installation via le script `install.sh` pointe sur cette branche. Il faut donc qu'elle soit à jour.

Considérons le cas le plus simple où la nouvelle version se fait sur la branche `master`. Lancez le script de changement de version, par exemple pour passer en version `1.2.3` :

    ./release/new_version.sh 1.2.3

Poussez les modifications sur le dépôt :

    git push origin master --tags

A ce stade, le code source de Duniter est monté en version, et un nouveau tag a été ajouté au dépôt. GitHub est au courant, et reflète une entrée dans les releases à cette occasion. Toutefois la release n'existe pas encore.

### 3. Créer la pré-release

Cette fois, nous allons créer la release avec le status *pre-release*. Ce statut permet de produire la release sans que celle-ci soit visible officiellement jusqu'au moment où l'on décidera que « tout est bon ».

Pour produire la pre-release et l'ensemble des livrables (hors ARM), toujours pour notre version d'exemple `1.2.3` :

    ./release/new_prerelease.sh 1.2.3

Cette procédure **est longue** et se résume en 3 étapes :

* Création de la pré-release sur GitHub
* Production des livrables
* Téléversement des livrables produits, sur GitHub

La 1ère étape est quasi-instantannée, mais la production et le téléversement sont longs : le script va produire des machines virtuelles Ubuntu et Windows afin d'y réaliser les livrables finaux. Puis, le téléversement peut prendre du temps selon le débit disponible sur votre connexion Internet.

### 4. Valider la release

Vous pouvez alors consulter les livrables [sur la page releases du dépôt GitHub](https://github.com/duniter/duniter/releases). Après avoir contrôlé que l'ensemble des fichiers sont bien présents, il est possible de valider la release via :

    ./release/set_release.sh 1.2.3 rel

La *pre-release* passera alors en *release*, et les utilisateurs seront alertés du changement via Duniter UI (dont disposent Duniter Desktop ou Duniter Server démarré en `webstart`). La page d'accueil https://duniter.org/fr affichera également cette nouvelle version.

### 5. Le build ARM

A tout moment, il est possible de réaliser cette opération sur ARM : si la release ou pre-release GitHub existe déjà, elle ne sera pas davantage touchée. Sinon elle sera créée.

Réaliser les opérations 1., 3. et 4. sur ARM (pas la 2., puisque le tag existe déjà) produira un résultat strictement identique, *excepté* le fait que seul le livrable ARM sera produit.

Une bonne pratique est donc de démarrer les étapes 1., 2. et 3. sur un poste Linux 64bits, *puis* de lancer les étapes 1., 3. et 3. sur ARM en parallèle. Il existera alors 2 machines apportant leur concurrence à la construction de la release.
