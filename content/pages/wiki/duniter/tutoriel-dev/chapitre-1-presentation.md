Title: 1. Présentation générale
Order: 1
Date: 2017-10-31
Slug: chapitre-1-presentation
Authors: cgeek

Duniter est *un logiciel*. Ce logiciel donne vie à la première crypto-monnaie libre appelée **Ğ1**.

La Ğ1 est une crypto-monnaie semblable au Bitcoin : elle utilise une blockchain que n'importe quel agent économique peut utiliser pour recevoir et envoyer des Ğ1 quand il le souhaite, sans demander d'autorisation à qui que soit et sans restriction sur le fait qu'il soit un individu, une association, une entreprise, un État ou autre chose. Par ailleurs, les transferts d’unités Ğ1 sont sant frais contrairement au Bitcoin. Il n'y a pas on non plus de limite sur le nombre d'utilisateurs ou de comptes.

La Ğ1 a aussi la particularité d'être **une monnaie libre** : ses nouvelles unités sont émises par chaque individu membre du réseau Ğ1, à parts égales, à la fois pour les membres actuels et les générations futures. La Ğ1 a été conçue de telle façon que chaque individu soit égal aux autres quant à son pouvoir de création monétaire en Ğ1, peu importe qu'il adopte la monnaie maintenant ou dans 20, 40, 80 ou 160 ans.

### Objectifs de Duniter Ğ1

Le but est de faire la démonstration qu'il est possible de réaliser et d'adopter dès maintenant une monnaie libre numérique, portée par un réseau informatique décentralisé. À notre connaissance, il s'agit d'une première.

Aussi, bien que la Ğ1 n'ait pas de limite géographique, le but *n'est pas* que tout individu vivant sur Terre puisse produire des Ğ1 ni de réaliser une monnaie remplaçant toutes les monnaies mondiales.

L'humble but de la Ğ1 est de faire une démonstration limitée dans l'espace (mais pas dans le temps !) du fait que la réalisation d'une monnaie libre numérique décentralisée est à notre portée.

### Comparaison Bitcoin/Duniter

Sachez que Bitcoin autorise au maximum à 144 utilisateurs quotidiens de produire de la monnaie par le mécanisme du « minage ». C'est-à-dire que parmi les centaines de milliers d'utilisateurs du Bitcoin, seuls 144 ont le privilège de créer de nouveaux bitcoins chaque jour. Tandis que la Ğ1 à travers Duniter autorise un maximum d'environ 10 millions de producteurs quotidiens, et que tous produisent systématiquement la même part en même temps. Il n'y a pas de privilégiés au sein du système monétaire.

Duniter est donc un Bitcoin qui améliore fortement la partie création monétaire. Duniter fait donc *plus* que Bitcoin, pas moins.

> Il n'y a pas besoin d'être « membre » de la Ğ1 pour posséder un portefeuille Ğ1 : il est possible de créer *immédiatement* son portefeuille pour recevoir puis envoyer de la monnaie.

### Multi-monnaies

Duniter est capable de faire fonctionner d'autres monnaies que la Ğ1, et fait notamment tourner une monnaie de test appelée Ğ1-Test. Toutefois le projet Duniter, qui donne naissance au logiciel du même nom, n'a pas vocation à soutenir d'autres monnaies que la Ğ1 et la Ğ1-Test pour des raisons d'efficacité et de moyens. Pour ceux qui souhaiteraient créer leur propre monnaie libre sur la base du logiciel Duniter, il leur faudra forker le projet et trouver leurs propres développeurs, puis adapter le logiciel en fonction de leurs propres buts.

> Toutefois la monnaie Ğ1 ayant à peine huit mois d'existence (06/11/2017), nous ne vous conseillons pas de réaliser votre propre monnaie basée sur Duniter aujourd'hui. Le logiciel va fortement évoluer au cours des deux-trois prochaines années pour répondre aux faits expérimentaux qui valideront ou invalideront les décisions techniques prises pour ce projet.
>
> Attendre quelques années avant de lancer votre propre monnaie semble une sage décision.

### Taille maximale de la Ğ1

* **Producteurs** : Duniter connaît aujourd'hui (2017) un maximum technique pour le nombre de *producteurs* simultanés d'unités Ğ1 d'environ dix millions. Ce maximum volontaire repose sur des données empiriques de graphes sociaux et n'empêche pas que celui-ci soit augmenté dans le futur.

* **Utilisateurs** : le nombre maximum de producteurs est à différencier du nombre maximum d'*utilisateurs* de la monnaie (individus, entreprises…). Ce maximum n'est pour le moment pas connu, bien que très largement supérieur au nombre de membres, et dépend largement des évolutions techniques à venir.

## Particularités du projet

Duniter a vu le jour dans le but de démontrer la possibilité de réaliser une monnaie libre à travers l'outil informatique. C'est son seul et unique but : une démonstration de faisabilité. Il n'est donc pas ici de question de réaliser un énième Altcoin (dérivé de Bitcoin) qui ne se distinguerait que par le déplacement d'un point-virgule dans le code.

### Pourquoi pas une monnaie papier ?

Il est tout à fait possible de réaliser une monnaie libre papier. Toutefois si l'on souhaite atteindre un nombre conséquent d'utilisateurs, mettons plusieurs milliers, alors l'outil informatique devient indispensable pour des raisons de coûts et d'efficacité. Si en plus on souhaite rendre cette monnaie robuste, alors il convient de décentraliser sa gestion informatique : d'où le fonctionnement P2P du réseau.

### La toile de confiance

Une monnaie libre suppose de pouvoir identifier les producteurs de la monnaie, et surtout de s'assurer 1 producteur = 1 **humain** unique et vivant. À cette fin, Duniter implémente un mécanisme d'identification des individus souhaitant produire la monnaie.

Ce mécanisme est appelé *toile de confiance*, concept largement inspiré par [OpenPGP](https://fr.wikipedia.org/wiki/OpenPGP). Il s'agit d'un système d'identification décentralisé semblable à un système de cooptation pourvu de nombreuses règles pour éviter les abus. Cette mécanique est la partie la plus complexe du projet Duniter, car c'est aussi sur elle que repose entièrement sa sécurité.

## Caractéristiques techniques

### Code
Duniter est un logiciel libre sous licence AGPL, écrit à 97 % en TypeScript, qui après transpilation en JavaScript est interprété par NodeJS.

### Topologie

Le réseau Duniter Ğ1 fonctionne sur la base de *nœuds* en pair-à-pair, donc sans entité centrale. Il est possible d'interagir avec ces nœuds via des programmes *clients* tels Sakia, Cesium ou Silkaj :

![image|690x467](/fr/images/tuto-dev/topologie.png)

### Sécurité

Duniter utilise des fonctions de cryptographie basées sur le schéma [Ed25519](https://fr.wikipedia.org/wiki/EdDSA), et réutilise des librairies écrites en C de [NaCl](http://nacl.cr.yp.to/).

Duniter utilise aussi des fonctions de hachage. Aujourd'hui la seule utilisée est [SHA256](https://fr.wikipedia.org/wiki/SHA-2), toutefois la fonction [RIPEMD-160](https://fr.wikipedia.org/wiki/RIPEMD-160) est envisagée pour permettre le paiement par adresse à l'instar du Bitcoin. Aujourd'hui, tout transfert de Ğ1 se fait à destination d'une clé publique Ed25519.

Duniter *ne manipule pas de nombres flottants* pour les montants. Uniquement des nombres entiers.

### Blockchain

La blockchain de Duniter repose sur deux principes :

* tout bloc est signé par son auteur qui ne peut être qu'un membre de la toile de confiance
* chaque nouveau bloc est émis par preuve de travail dont la difficulté est propre à chaque membre

### Performances

Le JavaScript n'étant pas adapté aux fonctions gourmandes en puissance de calcul comme la signature numérique, la vérification de signature, le hachage ou les calculs de distance de la toile de confiance, Duniter réalise donc ces opérations en C/C++.

## Un dernier mot

Duniter n'impressionnera pas par le côté incroyablement pointu ou abscons de son code : le logiciel ressemble à s'y méprendre à n'importe quelle application de gestion, avec un code relativement lisible et aux noms de variables explicites (quand nous avons le temps).

Bien sûr, Duniter n'est pas une application centralisée et opère sur une blockchain en P2P, avec de la cryptographie asymétrique, de la preuve de travail à niveau personnalisé et de la toile de confiance. Des concepts pas manipulés tous les jours dans l'industrie logicielle, néanmoins tout à fait compréhensibles.

Avec un peu d'investissement personnel, il n'y a rien d'insurmontable. De plus, les développeurs répondent toujours présents sur le [Forum Duniter](https://forum.duniter.org), section Dev, pour vous aider.

> Passer à la suite du tutoriel : [Chapitre 2. Installation des outils](../chapitre-2-outils).
