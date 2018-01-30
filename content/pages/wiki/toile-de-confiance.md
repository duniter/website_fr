Title: La toile de confiance en détail
Order: 9
Date: 2017-07-12
Slug: toile-de-confiance
Authors: librelois

L'objet de cet article est de détailler le fonctionnement des différents paramètres d'une toile de confiance duniter ainsi que d'expliquer comment ont été choisis les valeurs de ses paramètres dans le cas de la monnaie Ğ1.

Aucune connaissance particulière n'est requise pour comprendre ce qui suit, car je vais à chaque fois bien définir toutes les notions abordées et tous les termes utilisés :)
Cependant nous irons assez loin, nous rentrerons nottament dans le détail du protocole duniter (uniquement sur les parties toile de confiance biensûr) ainsi que dans des aspects de théorie des graphes car cela me semble essentiel pour vraiment comprendre tous les rouages d'une toile de confiance duniter.
Rassurez-vous, nous allons y aller progressivement, nous commencerons par une vision d'ensemble puis nous détaillerons graduellement :)

## Prérequis
Avant de lire cet article, il est vivement recommendé d'étudier la [licence Ğ1](https://duniter.org/fr/wiki/licence-g1) et de lire les pages suivantes :
* [Devenir membre de la toile de confiance Ğ1](../devenir-membre)
* [Certifier de nouveaux membres](../certifier-de-nouveaux-membres)
* [Question Fréquentes sur la toile de confiance](../faq)

## Pourquoi a-t-on besoin d’une toile de confiance ?

Nous avons besoin d'une toile de confiance pour répondre à deux objectifs :
1. S'assurer que chaque être humain membre de la monnaie co-créer bien le même nombre de Dividendes Universel par intervalles de création (dans le cas de la Ğ1 cet intervalle est `86400` (=1 jour exprimé en secondes), c'est le paramètre monétaire* `dt`).
2. Identifier les calculateurs de blocs pour leur affecter une difficulté personnalisée. Cela est nécessaire afin d'éviter que le mécanisme de [preuve de travail](../duniter/preuve-de-travail) ne permette une centralisation du support de la monnaie (la blockchain) comme c'est hélas le cas dans de nombreuses crypto-monnaies non-libres.

> Attends c'est quoi un "paramètre monétaire" ?

Chaque monnaie Duniter possède sa propre blockchain au sein de laquelle sont définis ses propres paramètres monétaires (dans le bloc zéro), il s'agit d'un ensemble de "curseurs" qu'il faut ajuster en fonction des objectifs visés. À l'heure ou j'écris ces lignes le protocole Duniter (noté DUP) comporte vingt-et-un paramètres monétaires dont dix concernent la toile de confiance !
Nous décrirons en détail les dix paramètres qui concernent la toile de confiance, nous n'aborderons pas les autres.
Sachez simplement que dans le cas de la monnaie Ğ1, le DU est créé toutes les 24 h (86 400 secondes) mais que cet intervalle de temps régit par le paramètre `dt` peut très bien être fixée à d'autres valeurs pour d'autres monnaies.

Nous ne traiterons pas ici le deuxième objectif relatif à la preuve de travail, car ce n'est pas l'objet de cet article, la seule chose à comprendre est que la toile de confiance nous permet **d'identifier** les membres qui calculent des blocs, et que cette identification nous permet d'imposer une rotation des membres calculateurs, ce ne serait pas possible sans système d'identification. Cette rotation des membres calculateurs est essentielle, sans elle un membre très riche pourrait investir dans des fermes de calcul géantes pour prendre le contrôle de la blockchain et paraliser toute la communauté !

Revenons donc au premier objectif, s'assurer que chaque humain n'ait qu'un seul compte membre.
En pratique, le risque zéro n'existe pas, notre objectif n'est donc pas de concevoir une toile de confiance au sein de laquelle la fraude serait impossible (ce qui est de toute manière impossible).
Voici donc une reformulation plus réaliste en quatre sous-objectifs :
1. Rendre l’acte de certification suffisamment lourd pour obliger les membres à un minimum de vigilance.
2. Rendre la fraude suffisamment difficile pour qu'elle soit marginale.
3. Éviter que les éventuelles attaques sybil aient un impact significatif sur la monnaie. (_que les faux DU créés aient un poids négligeable par rapport à la masse monétaire légitime._)
4. Rendre la croissance de régions sybil suffisamment lente pour que la communauté est le temps de réagir.

> **Attends, une attaque quoi ?**

Une [**attaque sybil**](https://fr.wikipedia.org/wiki/Attaque_Sybil), c'est le nom que l'on donne à une attaque d'un système de réputation par la création de fausses identités.
Une toile de confiance est un cas particulier de [**système de réputation**](https://en.wikipedia.org/wiki/Reputation_system).

Il y a beaucoup de stratégies de scénarios d'attaques sybil possibles ainsi que de mobiles différents.
Notre objectif est que la toile de confiance nous prémunisse contre les attaques sybil susceptibles de compromettre le bon fonctionnement de la monnaie ou/et du réseau informatique qui la porte.
Ce qui veut dire que les micro-attaques sybil orchestrés par un petit groupe dont l'objectif est seulement un petit enrichissement personnel ne nous intéressent pas ici, ce n'est pas à la toile de confiance de nous prémunir de ces micro-attaques, mais à la justice de la communauté concernée, tout comme ce n'est pas à la commune de vous prémunir d'un cambriolage chez vous, mais la commune va vous garantir le fonctionnement des réseaux d'eau, le nettoyage de la voirie, etc…
De la même façon, la toile de confiance Duniter nous garantie collectivement le bon fonctionnement de notre monnaie et du réseau informatique qui la porte, et c'est déjà énorme !

## l’importance de l’indépendance à tout autre systèmes d’identification

Il nous est très régulièrement proposé de nous baser sur des systèmes d'identification centralisés et alimentés par des monnaies non-libre dépendant d'un état ou d'un autre.
Mais, nous serions alors dépendants de ces systèmes d'identification centralisés pour le bon fonctionnement de notre toile de confiance, ça n'a pas de sens.
De plus, les membres d'une monnaie libre peuvent être de n'importe quelle nationalité ou culture, nous perdrions cette universalité en dépendant d'un système d'identification étatique. De plus, cela exclurait les sans-papiers et les apatrides.
Il est essentiel pour nous de ne dépendre d'aucun état ni d'aucune institution. Nous ne dépendons que du réseau internet, et encore, il existe d'autres réseaux, si internet vennait a s'éteindre, les humains membres d'une monnaie libre pourrait très bien créer leur propre réseau d'information, c'est déjà ce que font certaines d’associations en créant leurs propres bout de réseau, donc c'est possible.

## Quelques bases en théorie des graphes

### Un peu de vocabulaire

- graphe : ensemble de points (nommés sommets) reliées entre eux par des flèches (nommées arcs).
- 
- graphe simple : graphe sans boucle (arc reliant un sommet à lui-même) et sans arcs superposés (plusieurs arcs reliant le même couple de sommets dans le même sens).
- 
- graphe orientés : graphe ou les arcs ont un sens, l'arc A –> B est donc différent de l'arc B –> A.
- 
- extrémité initiale et finale d'un arc : l'arc A –> B a pour extrémité initiale A et pour extrémité finale B.
- 
- sommet isolé : sommet n'étant lié à aucun arc.
- 
- degré d'un sommet : nombre d'arcs reliant ce sommet (dans les deux sens).
- 
- demi-degré extérieur d'un sommet A : nombre d'arcs ayant pour extrémités initiales le sommet A
- 
- demi-degré intérieur d'un sommet A : nombre d'arcs ayant pour extrémités finales le sommet A
- 
- chemin : trajet qu'il faut suivre pour se rendre d'un sommet A à un sommet B en respectant le sens des arcs. Le nombre d'arcs traversés est la longueur du chemin.

### Définition d’une toile de confiance Duniter

Les toiles de confiance Duniter (une par monnaie) sont des graphes simples orientés et sans sommets isolés.
Les sommets en sont les membres et les arcs les certifications.

Pourquoi orientés ?
Certifier est un acte personnel qui n'engage que l'émetteur de la certification, la confiance qu'il accorde au récepteur n'est pas forcément réciproque dans tous les cas (elle l'est souvent), mais on peut pas imposer au récepteur de faire confiance à l'émetteur.

De plus, tous les sommets sont des identités membres ou ayant déjà été membres par le passé, les sommets correspondant aux anciens membres sont dans un état particulier dit "désactivé". Les sommets désactivés ne peuvent plus émettre ou recevoir de nouvelles certifications, mais les certifications qu'ils ont émis et reçus avant de perdre leurs statuts de membre restent actives vers les autres membres jusqu’à leurs dates d'expirations dans le but d'éviter un effondrement en cascade de la toile de confiance. Si ces anciens membres ne redeviennent pas membres alors les certifications qu'ils avaient émis et reçus finiront par expirer, et les sommets "désactivés" en question finiront donc par devenir des sommets isolés.

Pour finir sur cette histoire d'ancien membre, au bout d'un certain délai qui dépend d'un paramètre monétaire, le sommet désactivé est supprimé et l'identité associée passe à l'état révoqué, c'est-à-dire que cette identité ne pourra plus jamais redevenir membre. L’humain qui possédait cette identité reste toutefois libre de redemander son adhésion dans la toile sous une nouvelle identité :)

> Qu’entends-tu par identité ?

Une identité est un groupe de trois informations : une clé publique, un nom, et un blockstamp.
Un blockstamp est une référence à un bloc précis d'une blockchain. Ça permet de dater le moment auquel l'identité a été créée, et de relier l'identité à une blockchain particulière, donc à une monnaie particulière (car chaque monnaie a sa propre blockchain).

Une identité peut être dans cinq états différents : en attente, membre, ancien membre, révoquée ou exclue.
Nous reviendrons plus en détail sur chacun de ses états.

Résumons tout cela avec un exemple :

    A -> B -> C
         |
	 \--> D

Si pour une raison x ou y, A perd son statut de membre, alors la toile s'effondre et tous les autres membres perdent aussi leurs statuts de membre en cascade. Pour éviter cela, la certification A –> B restera valide jusqu'à sa date d'expiration, laissant à B le temps de se faire certifier par C ou D par exemple.

L'absence de sommet isolé implique également que lorsque qu'un nouveau membre est ajouté à la toile de confiance il faut ajouter en même temps (c'est-à-dire dans le même bloc) l'ensemble des certifications qui lui permettent de devenir membre.
C'est pourquoi nous avons besoin d'un espace de stockage intermédiaire qui contient les identités **en attente** de devenir membre ainsi que les certifications émises par des membres envers ces identités, c'est espace c'est la fameuse "piscine" des nœuds Duniter (que l'on aurait aussi pu nommer "bac à sable" puisque dans le code de Duniter c'est le terme `sandbox` qui est utilisé). Notons que ces "piscines" contiennent également d'autres types de documents non mentionnés ici.

## Définition des règles d’une toile de confiance Duniter

Les toiles de confiance Duniter (une par monnaie) sont régies par huit règles présentées ci-après.
L'application de ces règles dépendent de onze paramètres variables d'une monnaie à l'autre. La valeur de dix d'entre eux sont fixés dans le bloc zéro, le onzième paramètre `msPeriod` est écrit en dur dans le code, car il a été ajouté après l'écriture du bloc zéro de la Ğ1.
Cette partie ne présente que les définitions des règles, les raisons d'être de ces règles sont présentés dans le cadre de l'historicité de leur apparition dans la partie "Origine des règles et cas de la  Ğ1".

### 1. Règle de distance et membres référents

  Paramètres : **StepMax** et **xPercent**

  Ces deux paramètres sont très fortement liés et définissent ensemble une seule et même règle : la règle de distance.
  Pour définir la règle de distance, nous devons au préalable définir ce qu'est un membre référent :

> **Membre référent** : un membre A est référent si et seulement si ses deux demi-degrés sont supérieurs ou égaux à `CEIl(N^(1/stepMax))` où N est le nombre total de membres.**

Nous pouvons maintenant définir la règle de distance :

> **Règle de distance** : un membre A respecte la règle de distance si et seulement si pour plus de xPercent % des membres référents R il existe un chemin de R vers A d'une longueur inférieure ou égale à `stepMax`.**

La notion de membre référent ne sert qu'à l'application de la règle de distance, les membres référents n'ont aucuns privilèges sur les membres non-référents.
Dans un toile aboutie, c'est-à-dire dans une toile ou chaque membre a certifié tous les membres qu'il est en mesure de certifier légitimement, tous les membres devraient êtres référents, mais de part la croissance progressive de la toile d'une part et le remplacement générationnel d'autre part, il existe à tous instants `t` des membres qui n'ont pas encore certifié tous les membres qu'ils sont en mesure de certifier légitimement. Ces membres seraient bloquants s'ils étaient pris en compte dans la règle de distance, et la toile de confiance ne pourrait jamais acceuillir de nouveaux membres. (Vous pouvez le visualiser sur la page "qualité toile" de currency-monit en cochant l'option "si le concept de membre référent n'existait pas").

> **Quand s'applique la règle de distance ?**

La vérification de la règle de distance étant couteuse en calcul, elle ne s'applique que lors de l'obtention et du renouvellement du statut de membre. (Voir partie "renouvellement du statut de membre").
_Cas particulier : la règle de distance ne s'applique pas au bloc zéro (écriture de la toile initiale)._

### 2. Règle du nombre minimal de certifications reçus

  Paramètre : **sigQty**

C'est la règle la plus simple, elle stipule que tout membre doit à tout moment (comprendre à tous blocs) être le destinataire d'au moins `sigQty` certifications actives.
Si ne serait-ce que pour le temps d'un seul bloc, un membre A se retrouve avec moins de `sigQty` certifications actives reçus, alors il perd le statut de membre à ce bloc. Il doit alors publier une demande de renouvellement de son adhésion.

### 3. Règle de renouvellement de l’adhésion

  Paramètres : **msValidity**, **msPeriod** et **msWindow**

L'obtention du statut de membre n'est pas un acquis pour la vie, mais pour une durée de `msValidity` secondes.

Tout membre (ou ancien membre non révoqué et non exclu définitivement) peut à tout moment émettre une demande de renouvellement de son adhésion à condition que son dernier renouvellement date de plus de `msPeriod` secondes (lorsque qu'un membre ne s'est jamais renouvellé, la date du dernier renouvellement correspond à la date d'obtention du statut de membre).
Lorsqu'une demande de renouvellement d'adhésion est émise, elle est stockée en "piscine" pour une durée maximale de `msWindow` secondes, puis elle sera inscrite en blockchain dès que le membre en question respectera la règle de distance **et** la règle sigQty (s’il les respecte déjà, dès qu'un nœud ayant reçu la demande de renouvellement trouve un bloc).

Tout membre dont le dernier renouvellement date de plus de `msValidity` secondes perd le statut de membre au premier bloc ou cette durée est atteinte. Dans ce cas, l'ancien membre dispose à nouveau d'une durée de `msValidity` secondes pour redevenir membre par cette même procédure de renouvellement. Passé ce délai, donc `2 × msValidity` après le dernier renouvellement, l'ancien membre est exclu définitivement et ne pourra plus jamais redevenir membre avec ce compte. S'il souhaite redevenir membre il devra se créer un nouveau compte à partir de zéro.

### 4. Règle d’expiration des certifications

  Paramètre : **sigValidity**

Toute certification inscrite en blockchain expire **sigValidity** secondes après son **émission**.

/!\ L'émission et l'écriture d'une certification ont lieu à des instants différents. Lorsque le membre A émet une certifiation à un instant t1, elle est d'abord stockée en piscine à cet instant t1, puis sera écrite en blockchain à un instant t2, dès que les règles de la toile le permettent, il peut y avoir plusieurs semaines d'écarts entre t1 et t2 !!

### 5. Règle du stock limité de certifications actives

  Paramètre : **sigStock**

Par certification active nous entendons certification inscrite en blockchain et qui n'a pas encore expiré.

À tout bloc et pour tout membre, l'ensemble des certifications émises par ce membre et actives doit être inférieur ou égal à sigStock. Lorsque ce quota est atteint, le membre en question devra attendre qu'une certification active dont il est l'émetteur expire pour pouvoir en écrire une autre.

### 6. Règle de l’intervalle d’écriture entre deux certifications

  Paramètre : **sigPeriod**

Lorsqu'une certification émise par un membre A est écrite en blockchain, aucune autre certification émise par A ne pourra être écrite en blockchain avant `sigPeriod` secondes.

### 7. Règle de la fenêtre d’écriture d’une certification

  Paramètre : **sigWindow**

Lorsqu'une certification est émise par un membre A, elle restera stockée en "piscine" pour au plus `sigWindow` secondes. Si la certification en question n'a toujours pas été écrite en blockchain passé ce délai, elle est purement supprimée.

### 8. Règle de la fenêtre d’écriture d'une identité 

  Paramètre : **idtyWindow**

Lorsqu'une identitée est émise, elle restera stockée en "piscine" pour au plus `idtyWindow` secondes. Si l'identitée en question n'a toujours pas été écrite en blockchain passé ce délai, elle est purement supprimée.

## Le cas particulier de la toile initiale au bloc zéro

L'application des règles présentées ne rend l'expansion d'une toile possible qu’à partir d'une toile pré-éxistante, il y a donc un cas particulier ou certaines règles ne s'appliquent pas : l'écriture du bloc zéro.

Seules les règles 2 et 5 s'appliquent lors de l'écriture du bloc zéro.

Dans la pratique, c'est l'humain qui génère le bloc zéro qui choisi manuellement quelles identités sont écrites dans le bloc zéro, mais toutes les identités et certifications écrites dans le bloc zéro doivent respecter les règles 2 et 5 et de plus le bloc zéro doit être signé avec la clé privée d'une des identités écrites.
Dès lors qu'un bloc zéro correct a été généré, toute identité inscrite dans le bloc zéro peut soumettre le bloc suivant, de fait l'auteur du bloc zéro n'a donc plus la main.

## Origine des règles et cas de la Ğ1

### 1. Distance et taille limite

La règle de distance a pour objectif de limiter la taille maximale d'une région sybil ainsi que la taille maximale de la communauté monétaire.
`xpercent` permet d'éviter une minorité de blocage (membres trop peu actifs).

![zone sybil]({filename}/images/wiki/toile-de-confiance/zone-sybil.png)

Les régions sybil sont isolés du reste du graphe, car les comptes sybil ne reçevrons de certifications que de la part d'autres comptes sybil ou de la part des auteurs de l'attaque. Ainsi, tout plus court chemins entre un membre légitime et un compte sybil passe forcément par un auteur de l'attaque. La limite de la profondeur de la région sybil dépend donc de la distance maximum entre les auteurs de l'attaque et les xpercent% membres référents les plus proches, cette distance caractéristique est nommée `stepAttackers`.
La taille maximale d'une région sybil crée par sigQty membres malveillants dépend du levier L=sigQty/sigStock :

    taille max région sybil = (sigStock-sigQty)*(1-L^(stepMax-stepAttackers))/(1-L)

Et de même la taille maximale théorique de la toile de confiance est :

    WoTmax = (sigStock)*L^(stepMax-1)

Sauf que dans les faits, la plupart des membres ne consommeront pas tout leurs stocks de certifications. De nombreuses études sociologiques montrent qu'un humain connaît en moyenne cinquante personnes, remplaçons donc sigStock par 50 :

  WoTmoy= (50)*(50/sigQty)^(stepMax-1)

Notre toile de confiance peut donc être dimensionnée avec seulement deux paramètres, notre objectif avec la Ğ1 est de créer une zone économique libre de l'ordre du million d'utilisateurs, voyons donc quelles combinaisons du couple (sigQty;stepMax) permettent d'attendre le million :

![graphe WoTmoy en fonction de sigQty et stepMax]({filename}/images/wiki/toile-de-confiance/graphe-WoTmoy.png)

La taille maximale d'une région sybil croît linéairement par rapport à sigQty mais exponentionellement par rapport à stepMax, donc pour avoir une toile la plus solide possible, nous devons minimiser la valeur de stepMax. Le graphe ci-dessus nous montre que la valeur de stepMax la plus faible permettant d'attendre le million de membres est de cinq.
Pour la valeur de sigQty nous avons le choix entre quatre pour atteindre 1,2 million ou cinq pour atteindre le demi million.
Sachant que la formule WoTmoy nous donne un ordre de grandeur et qu'elle considère tous les comtpes comme référents (ce qui n'est pas le cas en réalité), la taille maximale réelle que nous pourrons atteindre est certainement plus élevée, un demi millon est donc suffisant d'autant que plus sigQty est faible plus il est facile de lancer une attaque sybil (c'est plus simple d'être quatre complices que d'être cinq). Par mesure de sécurité nous avons donc choisi cinq, ce qui nous donne déjà :

stepMax = 5
sigQty = 5
sigStock >= 50

la taille max d'une région sybil est donc : `(sigStock-sigQty)*(1-(sigStock/5)^(5-stepAttackers))/(1-(sigStock/5))`

avec sigStock = 50 cela fait une région sybil de : `45*(1-10^(5-stepAttackers))/(-9)`

Une bonne façon de nous protéger est donc de maximiser `stepAttackers`. C'est pour cela que nous avons fait en sorte que dans la toile initiale Ğ1 beaucoup de membres référents soient déjà à quatre de distance les un des autres.

Autre moyen de nous prémunir d'une attaque sybil, si elle était suffisamment lente pour que nous ayons le temps de la détecter alors les membres référentes pourraits tendre volontairement la toile pour stopper l'élargissement de la zone sybil le temps que les auteurs de l'attaque soit déchut de leur statut de membre par non renouvellement des certifications légitimes dont ils avaient bénéficié pour devenir membre.
Le problème c'est qu'une attaque sybil peut être propagée par des comptes robots qui se certifieront très rapidement et de manière optimale, comment donc pourrions-nous les ralentir de force ?
En imposant un délai minimal entre deux certifications !

### 2. une question de temps

Nous venons de voir que pour ralentir de déploiement d'une attaque sybil afin d'avoir le temps de la détecter et de prendre des mesures, nous pourrions imposer un délai minimal entre deux écritures de certifications par le même compte. C’est la raison pour laquelle nous avons créé le paramètre `sigPeriod`.

Voici un graphe d'évolution de la taille d'une région sybil en fonction de `sigPeriod` et de `stepAttackers` :

f[stepAttackers](t) = {p=0, t
			p=1, t(sigStock/5)
			...p=n, t(sigStock/5)^n}

![graphe taille sybil en fonction de sigPeriod et stepAttackers]({filename}/images/wiki/toile-de-confiance/graphe-sigPeriod.png)

### 3. Une confiance éternelle ? (sigValidity, msValidity)

Si toute certification restait valable at vitam eternam, cela serait problématique pour au moins deux raisons :
D'une part il est important que les membres qui décédent cessent de créer des DU.
D'autre part, il est important que les faux comptes détectés par la communauté puissent ne pas rester membre indéfiniment.

Pour ce faire, il est nécessaire que les certifications aient une durée de vie limités et qu'il faille donc renouveller sa confiance envers ses pairs régulièrement.
D'un autre côté, il ne faut pas non plus que les membres passent leur vie à renouveller leurs certifications plutôt qu'à participer à des échanges économiques.
De plus, une certification à durée de vie trop courte rendrait l'acte de certification trop léger. Il faut que l'acte de certification reste conséquent pour être pris au sérieux.
Enfin, nous souhaitons également que la durée de vie d'une certification soit une durée simple à retenir pour que le plus grand nombre s’en souvienne.

Une fois tous ces critères pris en compte, nous hésitions entre un, deux ou trois ans.
Historiquement, nous avons d'abord tranché sur les valeurs de `sigPeriod` et `sigStock`, ce qui impliquait qu'il fallait a minima 495 jours pour épuiser tout son stock de certifications, un an n'est donc pas possible.
Trois ans nous semblait trop long, nous avons donc choisi deux ans.

Mais considérer qu'un mort va continuer à créer des DU dont personne ne pourra bénéficier pendant une durée pouvant aller jusqu'à deux ans, cela nous semblait trop. C'est pourquoi nous avons opté pour une durée de vie plus faible concernant le renouvellement de l'adhésion.
Nous avons donc choisi un an. Mais, nous aurions aussi pu choisir six mois. La valeur de **msValidity** est au final assez secondaire et pourrait facilement être modifée dans le futur si la communauté le souhaite.

### 4. Éviter que les piscines ne deviennent des dépôts sédimentaires (idtyWindow, sigWindow, msWindow)

Il faut nettoyer régulièrement les piscines pour éviter qu'elles n'atteignent des tailles astronomiques et pour garantir que même les petites machines peu puissantes puissent exécuter un nœud Duniter.
Pour ce faire il faut que les identités et certifications en attentes restent le moins longtemps possible en piscine, elles doivent cependant y rester suffisamment longtemps pour avoir une chance raisonnable d'être inscrites en blockchain.
Pour la Ğ1, nous avons estimé que deux mois étaient un minimum pour que tous les certificateurs potentiels d'une nouvelle identité aient le temps de se synchroniser. Nous voulions aussi que cette durée corresponde à un faible nombre d'unités d'une grandeur usuelle, afin d'être facilement intégrée et mémorisée par le plus grand nombre.
Typiquement, choisir sept semaines aurait été plus compliqué à intégrer et à retenir. Nous voulions que les durées à connaître restent le plus facilement intégrable et mémorisables.
Un mois nous semblait trop court, la valeur de deux mois s'est donc imposée. Et par souci de simplicité, nous avons appliqué cette même valeur de deux mois aux trois paramètres `idtyWindow`, `sigWindow` et `msWindow`.

### 5. Éviter de limiter les membres connaissant beaucoup de monde (sigStock)

De nombreuses études sociologiques montrent qu'un humain connait en moyenne cinquante personnes. Bien entendu, c'est une moyenne. Certains humains en connaissent beaucoup plus, d'autres beaucoup moins.
Là encore, nous avons tranché par le critère "nombre facile à retenir".
Bien que l'impact de `sigStock` sur la taille maximale des régions sybil soit secondaire, il convient tout de même de ne pas choisir un `sigStock` trop grand !
150 nous semblait trop élevé, nous avons donc choisi 100.

### 6. Se prémunir des minorités de blocage (xpercent)

### 7. L'ajout de msPeriod, une protection anti-spam

Ce paramètre un peu à part, rajouté après le bloc zéro, ne sert pas à réguler la toile de confiance mais à proteger le réseau informatique qui porte la monnaie contre les attaques de type spam.
En effet, des membres malveillants qui souhaitent nuire au bon fonctionnement de la monnaie pourraient demander leur renouvellement à chaque bloc (toutes les cinq minutes), ou pire encore, envoyer des centaines de requêtes de renouvellement par minute pour submerger les nœuds Duniter. En l'absence de limitation, les nœuds Duniter sont cencés traiter toutes les requêtes de renouvellement, même si l’adhésion a été renouvellées il y a cinq minutes !
Pour nous prémunir de cette possibilité d'attaque nous avons ajouté le paramètre `msPeriod`.
Par souci de simplicité, nous avons choisi de lui attribuer la même valeurs qu'aux paramètres `idtyWindow`, `sigWindow` et `msWindow`.
