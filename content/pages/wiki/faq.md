Title: FAQ
Order: 9
Date: 2017-07-07
Slug: faq
Authors: cgeek, inso, Ğaluel

[TOC]

# Portefeuilles et identités

#### Comment recevoir de la monnaie ?

> **Pour recevoir de la monnaie, vous avez besoin de générer votre clé privée.**. Cette clé privée est associée à une clé publique. En partageant cette clé publique, vous pouvez recevoir de la monnaie. La clé privée peut-être générée par différente méthode :  

> - En mémorisant une clé secrète et un mot de passe. Cette clé secrète et ce mot de passe, associés, vont générer une clé privée. Pour être utilisée, il faut connaître le couple clé secrète/mot de passe.
> - En générant dans un fichier une clé privée aléatoire. Pour être utilisée, il faut être en possession du fichier de clé privée.

#### Qu'est-ce que la création d'un compte membre ?

> **La création d'un compte membre est l'association entre une clé publique et un UID (Pseudonyme du compte).**
Lorsqu'il créé un compte membre, l'utilisateur déclare au réseau de la monnaie *à dater d'aujourd'hui, cette clé publique est dorénavant associée à cette identité*. Un compte membre est obligatoirement unique par individu.

#### Qu'est-ce que la révocation d'un compte membre ?

> **La révocation d'un compte membre consiste à invalider une identité.**
Lorsqu'il révoque un compte membre, l'utilisateur déclare au réseau de la monnaie *à dater d'aujourd'hui, l'identité créée à telle date antérieure n'est plus valide*. L'identité est invalide mais la monnaie présente sur la clé associée est toujours valide ! La révocation empêchera :  

> - de certifier l'identité révoquée
> - de demander une adhésion pour l'identité révoquée  

> Mais la révocation n'impact pas l'envoi et la réception de monnaie sur la clé associée à l'identité révoquée.

#### Pourquoi révoquer un compte membre, qu'il soit en cours d'adhésion ou déja membre ?

> **En révoquant un compte membre, vous assurez à la toile : **

> - Que ce compte ne pourra pas devenir membre. 
> - Que vous ne cherchez pas à créer de multiples comptes membres
> - Que les certifications sont émises vers un compte qui est en votre possession !

#### J'ai perdu mes identifiants, ou je souhaite changer mon pseudonyme ou ma clé privée, que puis-je faire ?

> **Vous devez révoquer le compte, recréer un compte et redémarrer le processus de certifications.**
Si le compte était en cours d'adhésion à la toile de confiance, vous devez aussi le révoquer. En effet, si ce compte recevait suffisamment de certifications et devenait membre, vous n'auriez alors pas le droit de créer un nouveau compte ! Vous seriez dans l'obligation d'attendre l'expiration de celui-ci.


# La toile de confiance

## Les certifications 

#### Je certifie quelqu'un, quelles conséquences ?

>** J'engage ma responsabilité vis à vis de toute la toile Ğ1**
En certifiant un nouveau membre j'assure, conformément à la licence Ğ1, l'ensemble des autres membres que je connais bien la personne certifiée, je serai donc capable le cas échéant d'effectuer des vérifications sur un double compte qui aurait été créé par cette même personne, en étant capable d'effectuer des recoupements sur les activités d'échanges économiques de la personne certifiée.

#### Pourquoi certifier quelqu'un ?

> **La certification est l'action la plus importante de la toile de confiance, c'est ce qui créé les liens de la toile de confiance**. Vous ne devez certifier quelqu'un que si vous connaissez suffisament bien cette personne ! En effet, c'est parce que chacun connait suffisamment bien les personnes qu'il/elle a certifié, que la toile peut se construire et que la confiance en l'unicité des personnes apparait par récursivité.

#### Quels sont les impacts techniques lorsque je certifie un nouvel entrant ?

> **Certifier des nouveaux venus va tendre la toile.**
La conséquence est qu'en ne certifiant que des nouveaux venus, la toile peut devenir tellement tendue qu'elle ne permet plus à personne d'y rentrer !

#### Quels sont les impacts techniques lorsque je certifie un membre existant ?

> **Certifier des membres va détendre la toile tout en consolidant les liens qui la constitue**
La toile est alors consolidée. Les chemins entre membres qui la constituent sont doublement renforcés. Elle se détend et peut alors accueillir de nouveaux membres.

#### Existe-t-il des règles de courtoisie entre membres ?

> **Par courtoisie, lorsque l'on rejoint la toile de confiance, on peut contre-certifier ses certifieurs en priorité, si et seulement si on les connaît tout aussi bien**
On aide ainsi nos certifieurs à ne pas être placés sur les bords de la toile au fur et à mesure de l'arrivée des nouveaux. En effet, une fois que vous êtes membres référent, vos certifications peuvent exclure quelqu'un de la toile si il est trop éloigné de vous !

## Les stratégies de certifications

#### Que se passe-t-il si je favorise des certifications vers l'extérieur ?

> **Ne certifier que vers l'extérieur est une bonne stratégie pour contrer les attaques sybilles**
Lorsque l'on certifie uniquement vers l'extérieur, la toile est de plus en plus tendue. La présence constante de membres à une distance de 5 d'autres membre va freiner et limiter l'arrivée de comptes sybilles en cas d'attaques. Ce procédé peut donc être utilisé par l'ensemble de la toile Ğ1 pour stopper son expansion le temps d'effectuer les vérifications nécessaires, et notamment découvrir à l'aide de leurs certifieurs les membres qui auraient effectué de fausses manoeuvres.

> Il s'agit donc aussi d'un procédé de sécurité.

## Le comportement de la toile de confiance

#### A quelle rythme évolue la toile de confiance au début de la monnaie ?

> **A ses débuts, la toile évolue au rythme des certifications internes et externes.**
Lorsque la toile arrive a sa dimension maximum, certifier vers l'intérieur va la détendre. Lorsque les utilisateurs certifient vers l'extérieur, elle va se tendre. Un peu de la même manière que la respiration des êtres vivants ! A terme, l'évolution de la toile sera plus fluide. Cette fluidité dépend du nombre de membres certifiant de manière active ! 

> Quelle que soit le type de certification, externe ou interne, le procédé inscrit dans la licence Ğ1 reste valide, il convient donc toujours de s'assurer que sa responsabilité est correctement engagée du fait que l'on connaisse bien la personne certifiée, et de s'assurer par tous moyens que la clé publique que l'on envisage de certifier est bien contrôlée par la personne connue.


