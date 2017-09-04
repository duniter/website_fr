Title: Preuve de travail
Order: 9
Date: 2017-05-02
Slug: preuve-de-travail
Authors: cgeek, elois

## A quoi ça sert ?

La preuve de travail permet de sychroniser un réseau pair à pair (p2p) de machines devant partager une base de donnée commune.
Dans duniter cette base de données commune c'est notre grand livre de compte commun qui consigne toutes les transactions de la monnaie ainsi que les actes de la toile de confiance (certifications, adhésions, renouvellements, révocations, etc).
Comment fait t'on lorsque plusieurs machines souhaitent ajouter en même temps une nouvelle donnée (une nouvelle transaction par exemple) ? 
De plus, comment fait-on pour nous mettre d'accord sur le temps qui s'est écoulé ? Ce qui est essentiel pour savoir s'il est temps de créer le dividende universel ainsi que pour gérer les délais d'expiration des adhésions et certifications.

Et bien la preuve de travail permet de résoudre ces deux problèmes en même temps, et voici comment : 
1. N'importequ'elle machine peut écrire une nouvelle donnée (= un nouveau bloc), mais pour avoir le droit de l'écrire il faut résoudre un défi qui demande du *travail* à la machine, ce défi doit être suffisamment difficile pour qu'il n'y ai pas deux machines qui le résolvent en même temps. Il n'y a donc qu'une seula machine qui peut écrire en même temps, celle qui résout le défi demandé, bien.
2. La résolution de ce défi demande un certain temps de calcul qui est fonction de la puissance de calcul du réseau, nous avons donc la un moyen de définir l'écoulement du temps selon un référenciel commun. Il suffit ensuite de choisir uen convention, par exemple `1 bloc = 5 min` puis d'adapter la difficulté du défi pour que le réseau trouve bien en moyenne un bloc toutes les 5 min.

## Seul les membres peuvent calculer

Duniter a une différence fondamentale avec toutes les autres crypto-monnaies basées sur la preuve de travail : seul les membres de la toile de confiance ont le droit d'ajouter des blocs à la blockchain (le grand libre de comptes commun).
Chaque bloc est signé avec la clé privée du membre qui l'a ajouté, cela permet d'affecter une difficulté personnalisée a chaque membre ce qui change absolument tout, sans ce mécanisme la Ğ1 serait tout aussi asymétrique et non-libre que le bitcoin !

La difficulté personnalisée est en effet indispensable pour empêcher la course au calcul, ainsi que pour empêcher un supercalculateur de prendre le controle de toute la blockchain et donc de la monnaie. 
De plus, la difficulté personnalisée impose une rotation dans l'écriture des blocs qui permet a tous d'avoir la possibilité d'écrire dans la blockchain, même avec une brique internet ou un raspberry pi, ce qui rend les monnaies duniter considérablement plus économes en énergie !

## Comment ça marche ?

### L'empreinte (le hash)

Exemple d'empreinte valide :

```
00000276902793AA44601A9D43099E7B63DBF9EBB55BCCFD6AE20C729B54C653
```

On peut voir que cette empreinte démarre par 5 zéros : réaliser une telle empreinte demande beaucoup de *travail* de la part d'un ordinateur, d'où le fait qu'on appelle l'opération consistant à réaliser une telle empreinte « *preuve de travail* ».

### La difficulté commune

Afin de nous donner une mesure commune du temps, nous avons besoin d'une difficulté commune qui assure que la blockchain avance a un rythme régulier (1 bloc toutes les `avgGenTime` secondes, `avgGenTime` étant l'un des 20 paramètres qui décrivent une monnaie duniter).
Cette difficulté peut commencer à valeur arbitraire (`70` dans le code `v1.5.x`) puis agit comme un ressort, si l'intervalle entre deux blocs est inférieur à `avgGenTime` la difficulté commune augmente et inversement si l'intervalle entre deux blocs est supérieur à `avgGenTime` la difficulté commune diminue.

#### Comment s'applique la difficulté

la valeur numérique de la difficulté correspond directement à une plage d'empreintes possibles parmi toutes les empreintes possibles. Dans duniter `v1.5.x` l'empreinte d'un bloc c'est le hash hexadécimal sha256 du bloc. ce qui veut dire que chaque caractère de l'empreinte n'a que 16 valeurs possibles : les chiffres de 0 à 9 et les lettres de A à F.

Pour interpréter une difficulté il faut éffectuer la division euclidienne de cette difficulté par 16. Exemple avec `70` :

70 // 16 = **4** reste **6**. Donc les empreintes valident sont celles qui comment par **4** zéros et dont le 5ème caractère est entre 0 et 5 (car 5=**6**+1). On écrire alors que les empreintes valident commençent par : `0000[0-5]`

> Oui mais l'empreinte d'un bloc sera toujours la même pour un bloc donné et n'a aucune raison de commencer par une suite particulière, donc comment fait t'on pour trouver un bloc qui a comme par hasard uen empreinte qui respecte la difficulté ?

Bien vu, il faut effectivement faire varier le contenu du bloc pour obtenir une empreinte différente, c'est le rôle du Nonce.
Lorsque qu'un membre veut ajouter un nouveau bloc à la blockchain, il fixe le contenu de ce bloc, puis rajoute un champ Nonce qu'il fait varier jusqu'a tomber par hasard sur une empreinte qui respecte la difficulté.

### Le Nonce

Il s'agit du champ du document `Block` permettant de faire varier l'empreinte finale du bloc, empreinte qui définit le niveau de la preuve de travail.

Exemples de valeurs de Nonce :

* 10100000112275
* 10300000288743
* 10400000008538
* 10700000079653
* 10300000070919

En réalité ces valeurs de `Nonce` suivent toutes un même schéma `XYY00000000000`. Le Nonce ne correspond pas aux nombres d'essais, mais plutôt à un espace de Nonce possible. La décomposition est la suivante :

* X correspond au numéro de pair. Par exemple celui qui a plusieurs nœuds avec la même clé personnelle et donc sont tous capable de calculer, chacun de ces nœuds va réaliser sa preuve avec un X différent, afin de ne pas calculer la même preuve justement. Car potentiellement, ils réalisent exactement le même prochain bloc (puisque l'émetteur est le même, le contenu possiblement identique, seul le Nonce peut varier), donc il faut avoir un Nonce qui les différencie.
* Y correspond au numéro de cœur du processeur. On peut voir par exemple que quelqu'un possède au moins 7 cores dans son CPU ici, car on lit le Nonce `107[...]`. Un serveur avec 99 cores pourrait réaliser une preuve `199[...]` par exemple.

Le reste du Nonce, la partie derrière XYY, est l'espace de Nonce du nœud pour chaque core du CPU. Ce qui fait donc un espace de 11 chiffres (`00000000000`) pour trouver un Nonce correct pour chaque core du CPU de la machine (CPU au sens large, ce peut-être un bi-CPU, on considère le nombre de cores résultants pour la PoW).

### La difficulté personnalisée

Nous avons expliquer plus haut que la difficulté personnalisée est **le nouveau concept fondamental** qui différencie les monnaies duniter des autres crypto-monnaie basés sur la « *preuve de travail* ». comme le bitcoin par exemple.  
Voici donc comment est calculée la difficulté personnalisée d'un membre :

La difficulté personnalisée d'un membre résulte de l'assemblage de deux contraintes distinctes qui un des rôles complémentaires : le **facteur d'exclusion** et le **handicap**. 

Soient `powMin` la difficulté commune, `exFact` le facteur d'exclusion d'un membre et `handicap` sont handicap. la difficulté personnalité `diff` de ce membre est :

    diff = powMin*exFact + handicap

#### Le facteur d'exclusion `exFact` d'un membre

Les membres qui n'ont jamais écris de bloc où qui n'ont pas écrit de bloc depuis longtemps ont un facteur d'exclusion de 1. Leur difficulté personnalisée sera donc égale a la somme `powMin + handicap`.  
Avant de lire la formule donnée plus bas vous devez comprendre le rôle de ce facteur d'exclusion : lorsqu'un membre ajoute un bloc a la blockchain, sont facteur d'exclusion saute subitement de 1 vers une valeur très élevée afin de faire grimper exponentionellement sa difficulté et l'exclure ainsi du calcul des prochains bloc et donc l'empecher de prendre le contrôle de la blockchain.
Le facteur d'exclusion du membre va ensuite chuter rapidement a chaque nouveau bloc dont il n'est pas l'auteur puis retomber à 1 au bout d'un nombre de bloc qui est en fait une proportion du nombre de membres calculant. (un tier dans le cas de la Ğ1, ce qui signifie que s'il y a 15 membres calculant vous êtes exclus pendant 5 blocs).

> heu attend c'est quoi le nombre de membres calculant ?

Très bonne question, il s'agit du nombre de membres que l'on considère comme étant actuellement en train de calculer le prochain bloc. En réalité il n'y a aucun moyen de savoir combien de membres sont réellement en train de calculer le prochain bloc car d'une part il est impossible d'avoir une vue complète du réseau et d'autres parts il existe des moyens de se rendre invisible du réseau. Il nous faut pourtant bien choisir une méthode, car sans considérer le nombre de membres calculants impossible de calibrer la difficulté personnalisée.
La méthode actuellement utilisée par Duniter est de regarder l'historique des X derniers blocs et considérer que le nombre de membres calculant c'est le nombre de membres ayant écrit au moins 1 bloc sur les X derniers blocs sans compter le tout dernier bloc.

> Et comment on choisi X ?

Gràçe au concept de **fenêtre courante**, X correspond alors a la taille de la fenêtre courante, voici comment cela fonctionne :
On nomme `issuersFrame` la taille de la fenêtre courante et `issuersCount` le nombre de membres ayant calculé au moins 1 bloc dans la fenêtre courante.  
Au commencement d'une blockchain, le tout premier bloc que l'on nomme le bloc #0 décrète que `issuersFrame=1` et `issuersCount=0`. Hé oui le tout dernier bloc étant exclu, il n'y a pour l'instant aucun membre dans la fenêtre courante.  
Ensuite, a chaque nouveau bloc on mesure la variation de `issuersCount`, des le second bloc (le bloc #1), l'auteur du bloc #0 entre dans la fenêtre courante, on écrira donc dans le bloc #1 `issuersCount=1`.  
`issuersFrame` varie alors de la façon suivante :  si `issuersCount` augmente de X (et X = 1 au maximum), alors `issuersFrame` augmentera de 1 unité pendant 5X blocs. Et inversement : si `issuersCount` diminue de Y (et Y = 2 au maximum : décalage de fenêtre + perte d’un auteur), alors issuersFrame diminuera de 1 unité pendant 5Y blocs. Les effets étant cumulatifs dans le temps. Ce qui fait que si un nouvel auteur apparaît au bloc `T` et un autre disparaît à `T+1`, `issuersFrame` augmentera de 1 unité à `T+1` puis diminuera de 1 unité à `T+2`, pour se stabiliser.  
Techniquement ce calcul est formalisé par les règles [BR_G05](https://github.com/duniter/duniter/blob/master/doc/Protocol.md#br_g05---headissuersframe) et [BR_G06](https://github.com/duniter/duniter/blob/master/doc/Protocol.md#br_g06---headissuersframevar) du protocole DUP.

> Revenons a notre difficulté personnalisée !

Nous avons dit que le facteur d'exclusion `exFact` augmente brutalement dés que le membre considéré trouve un bloc puis qu'il diminue rapidement pour retomber à 1 au bout d'un nombre de bloc égal au tier des calculateurs. Et bien, c'est parti voici comment est calculé `exFact` :

Soient `nbPreviousIssuers` la valeur du champ `issuersCount` du dernier bloc trouvé par le membre et `nbBlocksSince` le nombre de blocs trouvés par le reste du réseau depuis que le membre considéré a trouvé son dernier bloc.

    exFact = MAX [ 1 ; FLOOR (0.67 * nbPreviousIssuers / (1 + nbBlocksSince)) ]

La fonction FLOOR est une simple troncature, ainsi pour que exfact soit excluant il faut que le rapport `(0.67 * nbPreviousIssuers / (1 + nbBlocksSince))` soit supérieur un égal à 2. On voit bien que si `nbBlocksSince` est supérieur au tier des calculateurs = `0.33*nbPreviousIssuers` alors le rappart sera inférieur a 2 et donc le membre ne sera pas exclu du calcul du prochain bloc.  
A l'inverse, si le membre considéré est l'auteur du dernier bloc alors `nbBlocksSince=0` et le facteur d'exclusion vaut donc `0.67 * nbPreviousIssuers`, c'est d'autant plus grand que le nombre de calculateurs est élevé. Je vous laisse imaginer la difficulté vertigineuse que vous atteindrez en trouvant un bloc s'il y a des centaines de membres calculants !  Vous atteindrez une difficulté telle que même le plus grand des supercalcuteurs serait bloqué, et c'est bien le but du facteur d'exclusion : empecher les supercalculateurs et fermes de calcul de prendre le contrôle de la blockchain et donc de la monnaie.

En revanche, a tout instant t les deux tiers de membres calculants non exclus ont tous un facteur d'exclusion égal à 1, mais tous n'ont pas la même puissance de calcul, et donc si la difficulté personnalisée se limitait au facteur d'exclusion c'est toujours le tier des membres calculants les plus puissants qui écriraient des blocs et deux tiers restants seraient presques toujours exclus, en particulier les machines très modestes type rapsberry n'aurais aucune chance.

#### Le handicap

Le handicap est le second paramètre de la difficulté personnalisée, plus subtil il permet néanmoins d'améliorer considérablement le mécanisme de rotation en donnant un handicap aux membres ayant une machine puissante afin de donner leur chance aux machines les plus modestes et de diminuer le coût écologique de la monnaie.

Le calcul du handicap se base sur le nombre médian de blocs écrits par chaque membre au sein de la fenêtre courante. En gros, l'idée est de donner un handicap a la moitié haute de la fenêtre courante pour donner plus de chance a la moitié basse.

Soient `nbPersonalBlocksInFrame` le nombre de blocs écrits par le membre considéré dans la fenêtre courante et `medianOfBlocksInFrame` le nombre médian de blocs écrits par les membres au sein de la fenêtre courante.

Voici la formule :

    handicap = FLOOR(LN(MAX(1;(nbPersonalBlocksInFrame + 1) / medianOfBlocksInFrame)) / LN(1.189))

Démystifions cette formule, `(nbPersonalBlocksInFrame + 1) / medianOfBlocksInFrame)` est simplement le rapport entre le nombre de blocs calculés par le membre et la médiane. Par exemple si le membre a calculé 9 blocs dans la fenêtre courante alors que la médiane vaut 5 ce rapport vaudra (9+1)/5 = 2.
On s'assure via la fonction MAX que ce rapport vaut au moins 1.

Ensuite on prend le logarithme népérien de ce rapport pour éviter que l'handicap devienne excluant lorsque la fenêtre courante deviens très grande, c'est ce qui fait la subtilité de l'handicap, son rôle n'est pas d'exclure mais de niveller la difficulté de chacun en fonction de sa puissance pour que tout le monde ait a peu près les mêmes chances de calculer.

Si l'on veut que la handicap s'applique dés la médiane il faudrait ensuite diviser par `LN(1)`, le problème c'est qu'on a déjà niveller la rapport a 1 avec la fonctione max, donc si l'on divisait par `LN(1)` tout les membres calculants aurait un handicap >= `1`, qui plus est est il bien juste de donner un handicap a un membre qui est tout juste a la médiane ?
C'est pourquoi au lieu de prendre `1` on prend `1.189`, ce qui veut dire qu'il faut `18,9 %` au dessus de la médiane pour subir un handicap (si l'on néglige le +1 dans la formule qui devient effectivement négligeable pour un grand nombre de calculateurs).

Mais pourquoi `18,9%` me direz-vous ? 
C'est 16^(1/16), le facteur de difficulté entre 2 niveaux de la preuve de travail dont le hash est en hexadécimal.

En conclusion, ce qu'il faut retenir c'est l'idée d'indexer le handicap sur le logarithme du rapport a la médiane, et ne de l'apppliquer que pour les membres dont le rapport a la médiane dépasse le rapport entre 2 niveaux de difficulté de la preuve de travail.
