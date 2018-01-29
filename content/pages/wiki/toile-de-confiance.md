Title: La toile de confiance en détail
Order: 9
Date: 2017-07-12
Slug: toile-de-confiance
Authors: librelois

L'Objet de cet article est de détailler le fonctionnement des différents paramètres d'une toile de confiance duniter ainsi que d'expliquer comment on été choisies les valeurs de ses paramètres dans le cas de la monnaie Ğ1. 

Aucune connaissance particulière n'est requise pour comprendre ce qui suit, car je vais à chaque fois bien définir toutes les notions abordés et tout les termes utilisés :)
Cependant nous irons assez loin, nous rentrerons nottament dans le détail du protocole duniter (uniquement sur les parties toile de confiance bien sur) ainsi que dans des aspects de théorie des graphes car cela me semble essentiel pour vraiment comprendre tout les rouages d'une toile de confiance duniter.
Rassurez vous, nous allons y aller progressivement, nous commencerons par une vision d'ensemble pusi nosu détaillerons graduellement :)

## Prérequis
Avant de lire cet article, il est vivement recommendé d'étudier la [licence Ğ1](https://duniter.org/fr/files/licence_g1.txt) et de lire les pages suivantes :
* [Devenir membre de la toile de confiance Ğ1](../devenir-membre)
* [Certifier de nouveaux membres](../certifier-de-nouveaux-membres)
* [Question Fréquentes sur la toile de confiance](../faq)

## Pourquoi à t'on besoin d'une toile de confiance

Nous avons besoin d'une toile de confiance pour répondre à 2 objectifs :
1. S'assurer que chaque être humain membre de la monnaie co-créer bien le même nombre de Dividende Universel par intervalle de création (Dans le cas de la Ğ1 cet intervalle vaut `86400` (=1 jour exprimé en secondes), c'est le paramètre monétaire* `dt`).
2. Identifier les calculateurs de block pour leur affecter une difficulté personnalisée. Cela est nécessaire afin d'éviter que le mécanisme de [preuve de travail](../duniter/preuve-de-travail) ne permette une centralisation du support de la monnaie (la blockchain) comme c'est hélas le cas dans de nombreuses crypto-monnaies non-libres.

> Attend c'est quoi un "paramètre monétaire" ?

Chaque monnaie duniter possède sa propre blockchain au sein de laquelle sont définis ses propres paramètres monétaires (dans le bloc zéro), il s'agit d'un ensemble de "curseurs" qu'il faut ajuster en fonction des objectifs visés. A l'heure ou j'écris ces lignes le protocole duniter (noté DUP) comporte 21 paramètres monétaires dont 10 concernent la toile de confiance !
Nous décrirons en détail les 10 paramètres qui concernent la toile de confiance, nous n'aborderons pas les autres.
Sachez simplement que dans le cas de la monnaie Ğ1 le DU est créer toutes les 24h (86400secondes) mais que cet intervalle de temps régit par le paramètre `dt` peut très bien etre fixée a d'autres valeurs d'autres monnaies.

Nous ne traiterons pas ici le 2ème objectif relatif a la preuve de travail car ce n'est pas l'objet de cet article, la seule chose a comprendre c'est que la toile de confiance nous permet **d'identifier** les membres qui calculent des blocks, et cette identification nous permet d'imposer une rotation des membres calculateurs, ce ne serait pas possible sans système d'identification. Cette rotation des membres calculateurs est essentielle, sans elle un membre très riche pourrait investir dans des fermes de calcul géante pour prendre le controle de la blockchain et paraliser toute la communauté !

Revennons donc au 1er objectif, s'assurer que chaque humain n'est qu'un seul compte membre.
En pratique, le risque zéro n'existe pas, notre objectif n'est donc pas de concevoir une toile de confiance au sein de laquelle la fraude serait impossible (ce qui est de toute manière impossible).
Voici donc une reformulation plus réaliste en 4 sous-objectifs :
1. Rendre l’acte de certification suffisamment lourd pour obliger les membres à un minimum de  vigilance.
2. Rendre la fraude suffisamment difficile pour qu'elle soit marginale.
3. Éviter que les éventuelles attaques sybil est un impact significatif sur la monnaie. (_que les faux DU créer est un poid négligeable par rapport a la masse monétaire légitime._)
4. Rendre la croissance de régions sybil suffisamment lente pour que la communauté est le temps de 
réagir.

> **Attend, une attaque quoi ?**

Une [**attaque sybil**](https://fr.wikipedia.org/wiki/Attaque_Sybil), c'est le nom que l'on donne à une attaque d'un système de réputation par la création de fausses identités.
Une toile de confiance est en cas particulier de [**système de réputation**](https://en.wikipedia.org/wiki/Reputation_system).

Il y a beaucoup de stratégies de scénarios d'attaques sybil possibles ainsi que de mobiles différents.
Notre objectif est que la toile de confiance nous prémunisse des attaques sybil susceptibles de compromettre le bon fonctionnement de la monnaie ou/et du réseau informatique qui la porte.
Ce qui veut dire que les micro attaques sybil orchestrés par un petit groupe dont l'objectif est seulement un petit enrichissement personnel ne nous intéressent pas ici, ce n'est pas a la toile de confaince de nous prémunir de ces micro attaques, mais a la justice de la communauté concernée, tout comme ce n'est pas a la commune de vous prémunir d'un cambriolage chez vous, mais la commune vas vous garantir le fonctionnement des réseaux d'eau, le nettoiement de la voirie, etc
De la même façon, la toile de confiance duniter nous garantie collectivement le bon fonctionnement de notre monnaie et du réseau informatique qui la porte, et c'est déjà énorme !

## l'Importance de l'indépendance à tout autre systèmes d'identification

Il nous ai très régulièrement proposé de nous baser sur des systèmes d'identification centralisés et alimentés par des monnaies non-libre dépendant d'un état ou d'un autre.
Mais nous serions alors dépendant de ces systèmes d'identification centralisés pour le bon fonctionnement de notre toile de confiance, ça n'a pas de sens.
De plus, les membres d'une monnaie libre peuvent être de n'importe quelle nationalité ou culture, nous perdrions cette universalité en dépendant d'un système d'identification d'un état ou d'un autre, en plus cela exclurait les sans-papier et les apatrides.
Il est essentiel pour nous de ne dépendre d'aucun état ni d'aucune institution. Nous ne dépendons que du réseau internet, et encore, il existe d'autres réseaux, si internet vennait a s'étteindre les humains membres d'une monnaies libres pourrait très bien créer leur propre réseau d'information, c'est déjà ce que font certaines associations en créant leurs propres bout de réseau, donc c'est possible.

## Quelques bases en théorie des graphes

### un peu de vocabulaire

graphe : Ensemble de point(nommé sommets) reliées entre eux par des flèches (nommés arcs).

graphe simple : graphe sans boucle (arc reliant un sommet a lui-même) et sans arcs superposés (plusieurs arcs reliant le même couple de sommets dans le même sens).

graphe orientés : graphe ou les arcs ont un sens, l'arc A->B est donc différent de l'arc B->A.

extrémité initiale et finale d'un arc : l'arc A->B à pour extrémité initiale A et pour extrémité finale B.

sommet isolé : sommet n'étant lié a aucun arc.

degré d'un sommet : nombre d'arc reliant ce somment (dans les deux sens).

demi-degré extérieur d'un sommet A : nombre d'arc ayant pour extrémité initiale le sommet A

demi-degré intérieur d'un sommet A : nombre d'arc ayant pour extrémité finale du sommet A

chemin : trajet qu'il faut suivre pour se rendre d'un sommet A à un sommet B en respectant le sens des arcs. Le nombre d'arc traversés est la longueur du chemin. 

### définition d'une toile de confiance duniter

Les toiles de confiance duniter (une par monnaie) sont des graphes simples orientés et sans sommets isolés.
Les sommets en sont les membres et les arcs les certifications.

Pourquoi orientés ?
Certifier est un acte personnel qui n'engage que l'émetteur de la certification, la confiance qu'il accorde au receveur n'est pas forcément réciproque dans tout les cas (elle l'est souvent), mais on peut pas imposer au receveur de faire confiance a l'emetteur.

De plus, tout les sommets sont des identités membres ou ayant déjà été membres par le passé, les sommets correspondant aux anciens membres sont dans un état particulier dit "désactivé". Les sommets désactivés ne peuvent plus émettrent ou recevoirs de nouvelles certifications, mais les certifications qu'ils ont émis et reçus avant de perdre leur statut de membre restent actives sur les autres membres jusqu'a leur date d'expiration dans le but d'éviter un éffondrement de la toile en cascade. Si ces anciens membres ne redeviennent pas membres alors les certifications qu'ils avaient émis et reçus finiront par expirés, et les sommets "désactivés" en question finiront donc par devenir des sommets isolés.

Pour finir sur cet histoire d'ancien membre, au bout d'un certain délai qui dépend d'un paramètre monétaire le sommet désactivé est supprimé et l'identité associée passe à l'état révoquée, c'est a dire que cette identité ne pourra plus jamais redevenir membre. l'Humain qui possédais cette identité reste toutefois libre de redemander son adhésion dans la toile sous une nouvelle identité :) 

> Qu'entend tu par identité ?

Une identité c'est un groupe de 3 informations : une clé publique, un nom, et un blockstamp*.
Un blockstamp c'est une référence a un block précis d'une blockchain ce qui permet de dater le moment auquel l'identité a été créée, et de relier l'identité a une blockchain particulière, donc a une monnauie particulière (car chaque monnaie a sa propre blockchain).

Une identité peut etre dans 5 états différents : en attente*, membre, ancien membre, révoqué ou exclu.
Nous reviendrons plus en détail sur chacun de ses états.

Résumons tout cela avec un exemple : 

    A -> B -> C
         |
	 \--> D

  Si pour une raison x ou y A perd son statut de membre alors la toile s'éffondre et tout les autres membres perdent aussi leur statut de membre en cascade. pour éviter cela, la certification A->B restera valide jusqu'à sa date d'expiration, laissant a B le temps de ce faire certifier par C ou D par exemple.

L'absence de sommet isolé implique également que lorsque qu'un nouveau membre est ajouté a la toile de confiance il faut ajouter en même temps (c'est à dire dans le même bloc) l'ensemble des certifications qui lui permette devenir membre.
C'est pourquoi nous avons besoin d'un espace de stockage intermédiaire qui contient les identités **en attente*** de devenir membre ainsi que les certifications émises par des membres envers ces identités, c'est espace c'est la fameuse "piscine" des noeuds duniter (que l'on aurait aussi pu nommer "bac a sable" puisque dans le code de duniter c'est le terme `sandbox` qui est utilisé). Attention ces "piscine" contiennent également d'autres types de documents qui ne sont pas mentionnés ici.

## Définition des règles d'une toile de confiance duniter

  Les toiles de confiance duniter (une par monnaie) sont régies par 8 règles présentées ci-après.
L'application de ses règles dépendent de 11 paramètres variables d'une monnaie à l'autre, la valeur de 10 d'entre eux sont fixés dans le block zéro, le 11ème paramètre `msPeriod` est en dur dans le code car il a été ajouté après l'écriture du bloc zéro de la Ğ1.
Cette partie ne présente que les définitions des règles, les raisons d'être de ces règles sont présentés dans le cadre de l'historicité de leur apparition dans la partie "Origine des règles et cas de la  Ğ1".

### 1. Règle de distance et Membres Référents

  paramètres : **StepMax** et **xPercent**

  Ces deux paramètres sont très fortement liés et définissent ensemble une seule et même règle : la règle de distance.
  Pour définir la règle de distance, nous devons au préalable définir ce qu'est un membre référent :

> **Membre référent** : un membre A est référent si et seulement si ses deux demi-degrés sont supérieurs ou égaux à `CEIl(N^(1/stepMax))` où N est le nombre total de membres.**  

Nous pouvons maintenant définir la règle de distance : 

> **Règle de distance** : un membre A respecte la règle de distance si et seulement si pour plus de xPercent % des membres référents R il existe un chemin de R vers A d'une longueur inférieure ou égale à `stepMax`.**  

La notion de membre référent ne sert qu'a l'application de la règle de distance, les membres référents n'ont aucun privilèges sur les membres non-référents.
Dans un toile aboutie, c'est à dire dans une toile ou chaque membre a certifier tout les membres qu'il est en mesure de légitimement certifier, tout les membres devraient êtres référents, mais de part la croissance progressive de la toile d'une part et le remplacement générationnel d'autre part, il existe a tout instant t des membres qui n'ont pas encore certifier tout les membres qu'il sont en mesure de légitimement certifier, ces membres là serait bloquants s'il était pris en compte dans la règle de distance, et la toile de confiance ne pourrait jamais acceuillir de nouveaux membres. (Vous pouvez le visualiser sur la page "qualité toile" de currency-monit en cochant l'option "si le concept de membre référent n'existait pas").

> **Quand s'applique la règle de distance ?**

la vérification de la règle de distance étant couteuse en calcul, elle ne s'applique que lors de l'obtention et du renouvellement du statut de membre. (Voir partie "renouvellement du statut de membre").
_Cas particulier : la règle de distance ne s'applique pas au block zéro (écriture de la toile initiale)._

### 2. Règle du nombre minimal de certifications reçus

  paramètre : **sigQty**

C'est la règle la plus simple, elle stipule que tout membre doit a tout moment (comprendre a tout bloc) être le destinataire d'au moins `sigQty` certifications actives.
Si ne serait-ce que pour le temps d'un seul bloc, un membre A se retrouve avec moins de `sigQty` certifications actives reçus, alors il perd le statut de membre a ce bloc là, il doit alors publier une demande de renouvellement.

### 3. Règle de renouvellement

  paramètres : **msValidity**, **msPeriod** et **msWindow**

L'obtention du statut de membre n'est pas un acquis pour la vie, mais pour une durée de `msValidity` secondes.

Tout membre (ou ancien membre non révoqué et non exclu définitivement) peut a tout moment émettre une demande de renouvellement a condition que son dernier renouvellement date de plus de `msPeriod` secondes (Lorsque qu'un membre ne s'est jamais renouveller la date de dernier renouvellement correspond a la date d'obtention du statut de membre).
Lorsqu'une demande de renouvellement est émise, elle est stockée en "piscine" pour une durée maximale de `msWindow` secondes, puis elle sera inscrite en blockchain dés que le membre en question respectera la règle de distance **et** la règle sigQty (s'il les respectent déjà, dés qu'un noeud ayant reçu la demande de renouvellement trouve un block).

Tout membre dont le dernier renouvellement date de plus de `msValidity` secondes perd le statut de membre au premier bloc ou cette durée est atteinte. Dans ce cas, l'ancien membre dispose a nouveau d'une durée de `msValidity` secondes pour redevenir membre par cette même procédure de renouvellement. Passé ce délai, donc `2*msValidity` après le dernier renouvellement, l'ancien membre est exclu définitivement et ne pourra plus jamais redevenir membre avec ce compte. S'il souhaite redevenir membre il devra se créer un nouveau compte à partir de zéro.

### 4. Règle d'expiration des certifications

  paramètre : **sigValidity**

Toute certification inscrite en blockchain expire **sigValidity** secondes après son émission.

/!\ l'émission et l'écriture d'une certification sont des instants différents. Lorsque membre A émet une certifiation à un instant t1, elle est d'abord stockée en piscine à cet instant t1, puis sera écrite en blockchain a un instant t2, dés que les règles de la toile de permette, il peut y avoir plusieurs semaines d'écart entre t1 et t2 !!

### 5. Règle du stock limité de certifications actives

  paramètre : **sigStock**

Par certification active nous entendons certification inscrite en blockchain et qui n'a pas encore expirée.

A tout bloc et pour tout membre, l'ensemble des certifications émises par ce membre et actives doit être inférieur ou égal à sigStock. Lorsque ce quota est atteint, le membre en question devra attendre qu'une certification active dont il est l'émétteur expire pour pouvoir en écrire une autre.

### 6. Règle de l'intervalle d'écriture entre deux certifications

  paramètre : **sigPeriod**

Lorsqu'une certification émise par un membre A est écrite en blockchain, aucune autre certification émise par A ne pourra être écrite en blockchain avant `sigPeriod` secondes.

### 7. Règle de la fenêtre d'écriture d'une certification 

  paramètre : **sigWindow**

Lorsqu'une certification est émise par un membre A, elle restera stockée en "piscine" pour au plus `sigWindow` secondes. Si la certification en question n'a toujours pas été écrite en blockchain passé ce délai, elle est purement supprimée.

### 8. Règle de la fenêtre d'écriture d'une identité 

  paramètre : **idtyWindow**

Lorsqu'une identitée est émise, elle restera stockée en "piscine" pour au plus `idtyWindow` secondes. Si l'identitée en question n'a toujours pas été écrite en blockchain passé ce délai, elle est purement supprimée.

## Le cas particulier de la toile initiale au block zéro

  L'application des règles présentées ne rend l'expansion d'une toile possible qu'a partir d'une toile pré-éxistante, il y a donc un cas particulier ou certaines règles ne s'appliquent pas : l'écriture du block zéro.

Seules les règles 2 et 5 s'appliquent lors de l'écriture du block zéro.

Dans la pratique, c'est l'humain qui génère le bloc zéro qui choisi manuellement qu'elles identités il écrira dans le block zéro, mais toutes les identités et certifications écrites dans le block zéro doivent respecter les règles 2 et 5 et de plus le block zéro doit être signé avec la clé privée d'une des identités écrites.
Dés lors qu'un bloc zéro correct a été généré, toute identité inscrite dans ce block zéro peut soumettre le block suivant, de fait l'auteur du block zéro n'a donc plus la main.

### 1. Règle de distance et Membres Référents

## Origine des règles et cas de la Ğ1

### 1. Distance et taille limite

La règle de distance à pour objectif de limiter la taille maximale d'une région sybil ainsi que la taille maximale de la communauté monétaire.
`xpercent` permet d'éviter une minorité de blocage (membres trop peu actifs).

![zone sybil]({filename}/images/wiki/toile-de-confiance/zone-sybil.png)

Les régions sybil sont isolés du reste du graphe, car les comptes sybil ne recevrons de certifications que de la part d'autres comptes sybil ou de la part des auteurs de l'attaque. Ainsi, tout plus court chemins entre un membre légitime et un compte, sybil passe forcément par un auteur de l'attaque. La limite de la profondeur de la région sybil dépend donc de la distance max entre des auteurs de l'attaque et les xpercent% membres référents les plus proches, cette distance caractérisqtique est nommée `stepAttackers`.
La taille maximale d'une région sybil crée par sigQty membres malveillants dépend du levier L=sigQty/sigStock :

    taille max région sybil = (sigStock-sigQty)*(1-L^(stepMax-stepAttackers))/(1-L)

Et de même la taille maximale théorique de la toile de confiance est :

    WoTmax = (sigStock)*L^(stepMax-1)

Sauf que dans les fait, la plupart des membres ne consommeront pas tout leur stock de certifications. De nombreuses études sociologiques montrent qu'un humain connait en moyenne 50 personnes, remplaçons donc sigStock par 50 : 

  WoTmoy= (50)*(50/sigQty)^(stepMax-1)

Notre toile de confiance peut donc être dimensionnée avec seulement 2 paramètres, notre objectif avec la Ğ1 est de créer une zone économique libre de l'ordre du million d'utilisateurs, voyons donc quelles combinaisons du couple (sigQty;stepMax) permettent d'attendre le million : 

![graphe WoTmoy en fonction de sigQty et stepMax]({filename}/images/wiki/toile-de-confiance/graphe-WoTmoy.png)

La taille max d'une région sybil croît linéairement par rapport a sigQty mais exponentionellement par rapport à stepMax, donc pour avoir une toile la plus solide possible nous devons minimiser la valeur de stepMax. le graphe ci-dessus nous montre que la valeur de stepMax la plus faible pêrmettant d'attendre le million de membres est 5.
Pour la valeur de sigQty nous avons le choix entre 4 pour atteindre 1,2million ou 5 pour atteindre 1/2 million.
Sachant que la formule WoTmoy nous donne un ordre de grandeur et qu'elle considère tout les comtpes comme référents (ce qui n'est pas le cas en réalité), la taille maximale réelle que nous pourrons atteindre est certainement plus élevée, 1/2 millon est donc suffisant d'autant que plus sigQty est faible plus il est facile de lancer une attaque sybil (c'est plus simple d'être 4 complices que d'être 5). Par mesure de sécurité nous avons donc choisi 5, ce qui nous donne déjà : 

stepMax = 5
sigQty = 5
sigStock >= 50

la taille max d'une région sybil est donc : (sigStock-sigQty)*(1-(sigStock/5)^(5-stepAttackers))/(1-(sigStock/5))

avec sigStock = 50 cela fait une région sybil de :45*(1-10^(5-stepAttackers))/(-9)

Une bonne façon de nous protéger est donc de maximiser stepAttackers. C'est pour cela que nous avons fait en sorte que dans la toile initiale Ğ1 beaucoup de membres référents soit déjà à 4 de distance les un des autres.

Autre moyen de nous prémunir d'une attaque sybil, si elle était suffisamment lente pour que nous ayons le temps de la détecter alors les membres référentes pourraits tendre volontairement la toile pour stopper l'élargissement de la zone sybil le temps que les auteurs de l'attaque soit déchut de leur statut de membre par non renouvellement des certifications légitimes dont ils avaient bénéficier pour devenir membre.
Le problème c'est qu'une attaque sybil peut etre propagée par des comptes robots qui ce certifieront très vite et de manière optimale, comment donc pourrions nous les ralentir de force ?
En imposant un délai minimal entre deux certifications !

### 2. une question de temps

  Nous venons de voir que pour ralentir de déploiement d'une attaque sybil afin d'avoir le temps de la détecter et de prendre des mesures, nous pourrions imposer un délai minimal entre deux écritures de certifications par le même compte. c'est la raison pour laquelle nous avons créer le paramètre sigPeriod.

Voici un graphe d'évolution de la taille d'une région sybil en fonction de sigPeriod et de stepAttackers :

f[stepAttackers](t) = {p=0, t
			p=1, t(sigStock/5)
			...p=n, t(sigStock/5)^n}

![graphe taille sybil en fonction de sigPeriod et stepAttackers]({filename}/images/wiki/toile-de-confiance/graphe-sigPeriod.png)

### 3. Une confiance éternelle ? (sigValidity, msValidity)

### 4. Éviter que les piscines ne deviennent des dépots sédimentaires (idtyWindow, sigWindow, msWindow)

Il faut nettoyer régulièrement les piscines pour éviter qu'elles n'atteignent des tailles astronomiques et pour garantir que même les petites machines peu puissantes puissent éxécuter un noeud duniter.
Pour ce faire il faut que les identités et certifications en attentes restent le moins longtemps possible en piscine, elle doivent cependant y rester suffisamment longtemps pour avoir une chance raisonnable d'être inscrites en blockchain.

### 5. Éviter de limiter les membres connaissant beaucoup de monde (sigStock)

### 6. Se prémunir des minorités de blocage (xpercent)

### 7. L'ajout de msPeriod, une protection anti-spam

Ce paramètre un peu a part, rajouter après le bloc zéro, ne sert pas a réguler la toiel de confiance mais a proteger le réseau informatique qui porte la monnaie contre les atatque de type spam.
En effet, des membres malveillants qui souhaitent nuire au bon fonctionnement de la monnaie pourrait demander leur renouvellement a chaque block (toute les 5 min), ou pire encore, envoyer des centaines de requete de renouvellement par minute pour déborder les noeuds duniter. En l'absence de limitation, les noeuds duniter sont sencés traiter toutes vos requetes de renouvellement, même si vous vous êts renouvellés il y a 5min !
Pour nous prémunir de cette possibilité d'attaque nous avons ajouté le paramètre `msPeriod`.
Par souci de simplicité, nous avons choisi de lui attribuer la même valeurs qu'aux paramètres idtyWindow, sigWindow et msWindow.

## Mesure 

* [Étude de l'évolution de la toile Ğ1](#) _(page encore inexistante)_
