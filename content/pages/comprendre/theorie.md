Title: La théorie
Order: 1
Date: 2015-08-11
Slug: theorie
Authors: cgeek

## Un système de crypto-monnaie

Duniter utilise le concept de crypto-monnaie introduit par Bitcoin : le principe est d'utiliser les possibilités offertes par la cryptographie comme la signature électronique afin de créer des devises numériques. Toutefois, Duniter a d'autres principes très différents de Bitcoin comme la *Toile de Confiance* et le *Dividende Universel*. En fait, Duniter a une référence théorique : la [Théorie Relative de la Monnaie (TRM)](http://trm.creationmonetaire.info). Cette théorie démontre qu'une monnaie qui vise à respecter les libertés économiques de chaque individu doit mettre en œuvre le Dividende Universel (ou Revenu de base par création monétaire). Ceci est la seule façon d'éviter les asymétries spatiale et temporelle dans l'émission de la monnaie.

## Une asymétrie spatio-temporelle

L'asymétrie spatio-temporelle se réfère à l'accès relatif des individus à la monnaie nouvellement créée. Concrètement, toutes les monnaies existantes (2015) sont à la fois spatialement et temporellement asymétriques pour leurs utilisateurs. Prenons par exemple le Bitcoin afin de comprendre pourquoi.
### Spatialement

Lorsque de nouveaux BTC sont créés, _seuls certains utilisateurs_ (les mineurs) sont crédités, tandis que les autres membres de la communauté ne reçoivent rien. **Nous pensons que ceci est la première injustice.** Cependant, certains pourraient dire :

> <div class="ui message">« Mais les mineurs utilisent de l’électricité et du temps pour obtenir ces BTC! »</div>

À cela, nous répondrions que ce travail _ne doit pas être récompensé par les BTC nouvellement créés_. Les nouveaux BTC devraient être répartis dans toute la communauté. Les mineurs devraient être récompensés d’une autre façon. Bien sûr, Bitcoin ne peut pas créer de la monnaie par le Revenu de Base puisque ses utilisateurs ne sont pas fortement identifiés. En possédant plusieurs portefeuilles, ces derniers pourraient bénéficier plusieurs fois de la création de monnaie.

Duniter se débarrasse de ce problème *dans sa conception* par l'identification de ses utilisateurs, ce qui permet de donner **le même montant à tout le monde**.

### Temporellement

Bitcoin a une limite prévue de 21 millions de BTC. Cela signifie que de moins en moins de monnaie est créée au fil du temps (jusqu'à plus du tout). Ainsi, une fois que les premiers arrivants auront exploité chaque BTC, comment feront les suivants pour obtenir des BTC ? La réponse est : tout comme les euros ou les dollars, pour obtenir de la monnaie, vous devrez forcément travailler pour ceux qui en possèdent déjà, ce qui ne permet pas de commencer son activité économique librement. **Nous pensons que c’est la seconde injustice.** Chaque membre d'une communauté monétaire devrait être égal face à l'émission de la monnaie et en obtenir la même quantité relative au cours du temps, _même s'il adopte le système en cours de route_. Duniter tend à corriger ce défaut en faisant croître le Dividende Universel en fonction du temps selon des règles précises permettant aux membres d’obtenir une quantité égale de monnaie sur la période d’une demie vie.

## Une solution

L’idée est la suivante: Bitcoin nous a enseigné _qu'il est possible_ de créer un système monétaire permettant à la fois de créer la monnaie numérique et de l'échanger sans autorité centrale. Que devons-nous changer de Bitcoin afin que nous ayons enfin un système symétrique ? Nous avons besoin d'y ajouter le Dividende Universel. Mais le dividende universel _implique_ d'avoir une communauté de personnes identifiées.

C’est ici qu’intervient la toile de confiance (ou Web of Trust, WoT). Ce concept, introduit en cryptographie avec le format OpenPGP, nous permet d'identifier les membres d'une manière décentralisée. Il fonctionne de cette façon : chacun crée une _identité personnelle_, liée à son certificat cryptographique, qui doit être confirmée par les autres membres en utilisant leur propre clé de chiffrement. C’est aussi simple que cela : **les gens définissent par eux-mêmes qui fait et qui ne fait pas partie de la communauté.**

> Duniter n'utilisera cependant pas OpenPGP pour ses fonctions cryptographiques mais plutôt les Courbes Elliptiques. Celles-ci sont beaucoup plus concises et il en résulte des avantages pratiques importants. Cela implique pour nous de définir notre propre processus de génération de toile de confiance, mais nous pensons que cela en vaut la peine.

### La Blockchain

Le mécanisme de blockchain de Bitcoin est important pour nous, pour deux raisons principales: **la synchronisation et la sécurité**. Duniter l’utilisera aussi pour bénéficier de ces deux caractéristiques. Cependant, la blockchain de Duniter est légèrement différente : tout comme Bitcoin elle sert à stocker les transactions, mais aussi la Toile de Confiance. Elle dispose également d'un mécanisme différent de _preuve de travail_ (Proof-of-Work = PoW) rendu possible par définition de la WoT, et permettant une économie d'énergie considérable.

#### La toile de confiance (WoT)

La toile de confiance Duniter être inscrite dans notre document commun : la blockchain. De la même manière que les transactions de Bitcoin sont écrites dans la blockchain de Bitcoin, l'identité de chaque personne y est également inscrite. Ainsi, la blockchain constitue un _référentiel d'espace-temps_, où _l'espace_ est représenté par les individus et _le temps_ fourni par les unités de la blockchain : les blocs.

Nous sommes donc en mesure de définir la **WoT(t)** : la communauté à un instant t, qui est la condition *sine qua non* du Dividende Universel.

#### Les transactions

La blockchain stocke également les _transactions_ : ce sont les documents qui permettent de transférer la monnaie d'un compte à un autre. Pour cette partie, Duniter ressemble vraiment à Bitcoin : les transactions ont des entrées (les comptes débités) et des sorties (les comptes crédités). La particularité de Duniter est que la monnaie débitée peut soit provenir :

* d'une autre transaction [comme Bitcoin]
* d'un Dividende Universel [spécifique à Duniter]

Comme vous pouvez le voir, aucune _transaction de génération_ n'existe dans Duniter, contrairement au Bitcoin par exemple. Ce type d'opération est remplacé par le _dividende universel_.

Par ailleurs, un compte peut être créé n'importe quand et est *totalement indépendant de la toile de confiance*. Un compte peut devenir membre afin de produire le Dividende Universel, mais cela n'est pas une condition requise pour utiliser la monnaie. Cela nous conduit à un fait important: **les entreprises sont également en mesure d'utiliser la monnaie, mais pas de la créer**. Seuls les individus sont en mesure de le faire. Ceci est un point très important.

Et donc, une entreprise peut tout à fait se créer un compte « porte-monnaie », qui ne fait rien d'autre que recevoir de la monnaie et en envoyer. De même, un individu peut très bien avoir plusieurs comptes : un pour créer la monnaie via le Dividende Universel, puis un autre pour les paiements réguliers, un autre pour l'épargne, un autre pour servir de pot commun, etc.

#### La preuve de travail

Comme tout système de crypto-monnaie P2P, Duniter a une façon de synchroniser ses pairs pour la rédaction de son document commun : la blockchain. Celle-ci est écrite de façon régulière grâce à une *preuve de travail*, tout comme Bitcoin. Cependant, Duniter bénéficie d'un environnement très différent de celui d'autres altcoins : il possède une **toile de confiance**, où chaque membre est supposé représenter un unique être humain vivant.

Cette différence peu paraître minime, mais elle a pourtant un impact énorme : alors que Bitcoin doit proposer une **course généralisée** basée sur la puissance de machines, Duniter a la possibilité de créer un cadre *qui n'est pas une course*. Concrètement, Duniter propose plutôt *une mini-loterie* où, chaque fois que quelqu'un gagne, il se voit exclut de celle-ci pendant un certain temps. De plus, ceux qui gagnent plus souvent la course que les autres se voient handicapés, de façon à laisser les autres gagner un minimum.

Cela est rendu possible car la Toile de Confiance rend possible **la course personnalisée** : en posant comme principe que seuls les membres peuvent calculer de nouveaux blocs, et en rendant très dangereux le fait de calculer à plusieurs, ce mécanisme permet ainsi une rotation dans l'écriture de la blockchain tout en gardant l'avantage de synchronisation apporté par la preuve de travail.

Mais de plus, les participants peuvent s'accorder pour abaisser le niveau de difficulté de cette mini-loterie, ce qui se traduit par une diminution *directe* de la consommation en électricité dont le niveau dépend principalement de la volonté des participants, et de leur nombre. Qui plus est, n'ayant aucune création monétaire à gagner à cette loterie, on peut supposer qu'injecter une forte puissance de calcul n'est pas très intéressant en termes économiques.

On pourrait donc dire que Duniter utilise une preuve de travail « écologique », ou à défaut qui peut tendre vers une très basse consommation relativement à Bitcoin.

### Pour résumer

La blockchain de Duniter peut être comparée à la blockchain de Bitcoin : un grand livre retraçant l'histoire de la Toile de Confiance, ainsi que les transactions réalisées par ses utilisateurs. Avec la blockchain, nous avons le **référentiel fondamental** de la Théorie Relative de la Monnaie : les humains, ainsi que le flux des transactions émises par les utilisateurs de la monnaie.

## Une économie libre

Le but de tout cela est de permettre aux gens de participer à une économie libre grâce à une monnaie libre. Qu'est-ce qu'une économie libre ? La [Théorie Relative de la Monnaie](http://trm.creationmonetaire.info/) la définit à travers 4 libertés économiques :

*   **La liberté de choisir son système monétaire** : parce que la monnaie     ne devrait pas être imposée
*   **La liberté d'accès aux ressources** : parce que nous devrions tous     avoir accès aux ressources économiques et monétaires
*   **La liberté d'estimer et de produire de la valeur** : parce que la     valeur est une notion relative à chaque individu, dans l'espace et le     temps
*   **La liberté d'échanger dans la monnaie** : parce que nous ne devrions     pas être limités par le stock de monnaie disponible

Ces quatre libertés économiques doivent être comprises ensemble, pas exclusivement. De plus, la «_liberté_» doit être comprise comme «_non-nuisance_». Donc ici, la liberté ne signifie pas le droit de prendre toutes les ressources (comme une source d'eau dans un désert) et qu'il n'y en ait plus à la disposition des autres. Maintenant vous comprenez quel est l'objectif : une _économie libre_ à travers des _monnaies libres_.
