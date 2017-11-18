Title: Duniter est-il énergivore ?
Date: 2017-11-18
Category: Technique
Tags: preuve de travail
Slug: duniter-est-il-energivore
Authors: cgeek
Thumbnail: /images/light.svg

Le Bitcoin a la réputation d'être « énergivore ». Or Duniter hérite de certaines propriétés du Bitcoin comme la preuve de travail et la blockchain. Dès lors, des individus se posent légitimement cette question : 

> Duniter est-il aussi énergivore ?

### Un peu de définitions

D'abord, il convient de s'arrêter sur le terme *énergivore* qui signifie « qui consomme de l'énergie ». Or à peu près n'importe quel système est énergivore, par exemple nos cellules humaines. Ce n'est pas cette définition qui pose problème, car on conçoit volontiers que Bitcoin ou Duniter requiert de l'énergie pour fonctionner.

On pourrait par contre penser qu'il s'agit d'un problème de quantité : par exemple, 10 Wh est inférieur à 10 kWh d'un facteur 1000. Oui mais, est-ce que 10 kWh c'est beaucoup ?

### Un rapport à d'autres utilisations

En tant que tel, on est bien incapable de dire que « 10 kWh c'est beaucoup ». Par contre, on saurait dire « 10 kWh c'est beaucoup d'énergie si c'est juste pour produire de la lumière pendant 1h dans mon salon ». En effet, aujourd'hui une ampoule de 100 W (même de vieille génération) suffirait largement à illuminer un salon de 50m² et ne consommerait que 100 Wh en une heure (par définition), et donc on est loin de 10 kWh : c'est 100 fois moins !

C'est là que je souhaite en venir : on dit d'un système qu'il est « énergivore » **en rapport au service fourni**, et donc en comparaison à d'autres utilisations de cette même quantité d'énergie.

Par exemple dans le cas de Bitcoin, il apparaît que [chaque transaction consomme 215 kWh](https://mrmondialisation.org/le-bitcoin-est-devenu-un-enfer-energetique/). Que peut-on faire avec une telle quantité d'énergie ? On peut fournir l'équivalent de 32 jours de consommation électrique d'un français moyen. Cela peut en effet paraître élevé pour simplement effectuer *un unique transfert de bitcoins*. Or Bitcoin réalise 300000 transactions *par jour*. Je vous laisse faire vos calculs.

> Oui, c'est *beaucoup* ! En rapport à d'autres utilisations possible de cette même quantité d'énergie.

### Et Duniter dans tout cela ?

Un premier point à comprendre est qu'il n'y a pas de course à la puissance dans Duniter, **pour la simple et bonne raison qu'il n'y a pas de récompense particulière à calculer des blocs** contrairement au Bitcoin. Cette simple mesure coupe l'herbe sous le pied d'une éventuelle course.

Toutefois, Duniter possède bien un mécanisme de preuve de travail pour permettre aux nœuds du réseau de parler de façon synchrone. Or cette tâche est la source de la consommation énergétique du Bitcoin. Mais là encore, Duniter bénéficie de mécanismes uniques du fait de sa toile de confiance : d'abord, seuls les membres de la monnaie peuvent calculer des blocs, ce qui limite le nombre de participants potentiels. Mais aussi, Duniter possède un mécanisme qui exclut *en permanence 1/3 du réseau de calculateurs de la preuve de travail*. Cela signifie qu'à chaque bloc, il existe 1/3 des calculateurs qui se tournent les pouces. Et donc, seuls 2/3 réalisent effectivement des calculs. Ce 1/3 exclu peut alors ajuster sa consommation électrique pour réaliser uniquement des opérations simples, comme réceptionner des transactions sur le réseau.

<center><image src="../images/networking.svg" width="200px"/></center>

Est-ce que pour autant la consommation électrique des 2/3 restants est élevée ? Contrairement au Bitcoin, les machines utilisées pour le calcul sont des ordinateurs domestiques, éventuellement des serveurs ou plus simplement des Raspberry PI. Et tout cela suffit. D'ailleurs, les machines ultra-efficace de Bitcoin (les fameux [ASIC](https://en.bitcoin.it/wiki/ASIC)) sont totalement inutiles dans Duniter car le mécanisme de preuve de travail n'est pas le même.

**Et donc dans les faits, chaque nœud Duniter consomme autant qu'une ampoule de 10 W à 100W et qui tourne en permanence.**

<center><image src="../images/light.svg" width="200px"/></center>

### Ça fait combien pour la Ğ1 ?

Aujourd'hui la Ğ1 compte environ 30 nœuds membres qui calculent des blocs. Si l'on compte une moyenne de 55 W de consommation instantannée par nœud, alors on obtient `55*24 = 1,32 kWh` de consommation électrique par jour et par nœud, soit `1,32*30 = 39,6 kWh` de consommation totale par jour.

Est-ce beaucoup ? Nous avons aujourd'hui environ 12 transactions par jour. Il peut paraître élevé d'avoir 30 ampoules de 55 W allumées en permanence juste pour réaliser 12 transactions par jour.

Oui mais : rien n'empêche de monter à 120 transactions par jour avec la même taille de réseau. Duniter est actuellement en sous-régime, 120 transactions, c'est tout à fait faisable ! De même que 1200 ou 12000 transactions par jour (40 transactions par bloc). Dans ce cas, est-ce que 30 ampoules serait beaucoup d'énergie au regard de ce nombre de transactions ?

Je vous laisse répondre à cette question par vous-même. :-)

<center><image src="../images/duniter-logo.png" width="200px"/></center>