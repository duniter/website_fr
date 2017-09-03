Title: Rapport toile de confiance Ğ1 au 1er Septembre 2017
Date: 2017-09-02
Category: Toile de confiance
Tags: wot, toile de confiance
Slug: rapport-etat-wot
Authors: elois
Thumbnail: /images/network.svg

Depuis le [4 juillet 2017](https://forum.duniter.org/t/currency-monit-monitoring-dune-monnaie-et-de-sa-toile-de-confiance/2770/17?u=elois) je tiens des statistiques détaillées sur l'état de la toile de confiance que vous pouvez visualiser sur [g1-monit.elois.org](https://g1-monit.elois.org).
*Ces statistiques sont produites par le [module duniter](https://duniter.org/fr/wiki/duniter/liste-modules/) `duniter-currency-monit` qui se sert directement dans la blockchain locale du noeud duniter sur lequel il est installé.*

J'ai décidé de profiter de ces statistiques pour publier régulièrement un court rapport sur l'état global de la toile de confiance Ğ1.

## L'esprit de ces courts rapports réguliers

L'objectif de ces courts rapports réguliers n'est pas d'être exhaustif mais au contraire de mettre en avant certains indicateurs qui me semblent pertinents à un moment donné pour visualiser un phénomène donné. Il n'y a pas de fréquence définie, je publierai un rapport chaque fois qu'il me semblera y avoir quelque chose de pertinent à décrire et que j'aurai le temps pour.
Si vous lisez régulièrement mes rapports, que vous consultez très régulièrement *g1-monit* et qu'il vous vient l'envie de rédiger vous aussi des rapports, vous pouvez [me contacter](https://librelois.fr/contact/) pour qu'on en discute :)

# Prérequis
Avant de lire ces rapports, il est vivement recommandé d'étudier la [licence Ğ1](https://duniter.org/fr/files/licence_g1.txt) et de lire toutes les pages suivantes :
* [Devenir membre de la toile de confiance Ğ1](../devenir-membre)
* [Certifier de nouveaux membres](../certifier-de-nouveaux-membres)
* [Question Fréquentes sur la toile de confiance](../faq)
* [**Fonctionnement de la toile de confiance**](https://duniter.org/fr/introduction-a-la-toile-de-confiance/)

En particulier la lecture de l'article [**Fonctionnement de la toile de confiance**](https://duniter.org/fr/introduction-a-la-toile-de-confiance/) est indispensable pour bien connaitre le fonctionnement de chacune des règles de la toile.

Je ferai également appel à des notions de théorie des graphes mais je m'attellerai à définir à chaque fois les termes utilisés.

Enfin, vous devez connaitre une grandeur spécifique aux toiles de confiance duniter, **la qualité d'un membre**.

## Qualité d'un membre
Ce que je nomme qualité d'un membre est le rapport entre le taux de membres référents rendus atteignables par une certification de ce membre et le taux de membres référents qu'il faut atteindre pour respecter la règle de distance.
Je vais donner un exemple pour que ce soit plus clair :
prenons une toile avec 10 membres référents et xpercent=0.8. Et bien la qualité d'un membre dans une telle toile est le rapport du nombre de membres référents qu'il permet de joindre en moins de 5 pas (numérateur) sur le nombre 8 (dénominateur). Donc si un membre Bob permet de joindre 4 référents il aura une qualité de 0.5.
Et si Bob permet de joindre 10 référents il aura une qualité de 10/8=1.25.

Qu'entends-je par "permet de joindre" ? Quand je dis que Bob permet de joindre x membres référents j'entends que si Bob certifie une nouvelle identité (qui n'est certifiée que par Bob) alors il y aura x membres référents pour lequels il existera un chemin de moins de 5 pas de eux vers la nouvelle identité.

Ainsi, un membre ayant une qualité supérieure ou égale à 1 pourrait faire rentrer un nouveau membre à lui seul si la règle sigQty n'existait pas.

Lorsque la qualité moyenne est supérieure à 1, c'est que la règle de distance n'est pas contraignante. Lorsque la qualité moyenne s'approche de 1, la règle de distance va devenir contraignante pour quelques cas minoritaires. Et lorsque la qualité moyenne devient inférieure à 1, alors la règle de distance devient contraignante pour la majorité des identités (par identités j'entends nouveaux + membres souhaitant se renouveler !)

Actuellement la qualité moyenne est de **1.04**, ce qui signifie que la règle de distance n'est pas contraignante, donc la toile n'est pas "trop" tendue, mais 1.04 c'est proche de 1, donc si tous les membres ne certifient que vers l'extérieur à partir de maintenant alors la règle de distance pourrait devenir contraignante rapidement (ce qui peut être une situation souhaitable et voulue dans certains cas, c'est aussi une liberté des membres que de tendre ou détendre la toile).

# Rapport toile Ğ1 au 2 septembre 2017

## Observations

Nous sommes deux semaines après le passage du palier Y[n]=4, rappel sur l'effet qu'avait eu ce palier : 

> La qualité de la toile va légèrement augmenter après ce palier, environ 88% de membres auront une qualité >= 1 contre 83.75% actuellement. Soit un gain de 4%. La règle de distance sera donc globalement moins contraignante mais pas de beaucoup, et au rythme actuel de croissance du nombre de membres, la toile va rapidement se tendre de nouveau ! Le nombre de référents va passer de 150 à 140, cela montre bien que les membres ne s’arrêtent pas à 3 certifications émises, ils continuent d’en émettre.

L'effet de densification du palier s'est déjà dissipé, la toile de confiance est de nouveau aussi tendue qu'avant le passage du palier, voire légèrement davantage :

* La proportion de membres ayant une qualité >=1 à chuté à **82%** soit environ le même niveau, qu'avant le palier (83%)
* De plus, une dizaine de membres commencent à chuter à des niveaux de qualité très faibles (inférieurs à 0.9), ce qui veut dire qu'ils commencent à être trop distants des membres référents, zones en noir sur ce graphique de la page [qualité toile]( https://g1-monit.elois.org/gaussianWotQuality?lg=fr) : </BR><img src="https://librelois.fr/public/qualite-toile-020917.png" width="690" height="339">
* D'ailleurs sur les 79 futurs membres ayant reçu au moins 1 certification, 7 d'entre eux ne respectent pas la règle de distance, 3 ont été certifiés par le même membre mais cela fait quand même **4 cas différents de non-respect de la règle de distance**.
* Un autre indicateur nous montre bien la tension de la toile, **l'augmentation de la longueur moyenne du plus court chemin entre deux membres** est désormais de **4.13**. Cette valeur a continuellement augmenté même lors du passage du palier car elle est indépendante de la notion de membre référent, elle montre l'état de tension de la toile entière là où la qualité ne montre que l'état de tension d'un sous ensemble de la toile (le sous-ensemble des liens référent->membre).
* Enfin le nombre de membres référents est quant à lui repassé au-dessus de sa valeur d'avant le palier (153) : 
<img src="https://librelois.fr/public/fin-effet-palier-yn-4.png" width="690" height="339">

## Interprétations

  La règle de distance est encore très loin d'être bloquante, mais la toile n'a jamais été aussi tendue depuis que je tiens des statistiques très détaillés sur son état, c'est-à-dire depuis le 4 juillet 2017.
  
  La toile de confiance Ğ1 est en train de se tendre car le flux de nouveaux entrants va plus vite que la reconnaissance interne entre les membres déjà membres. Ce phénomène est parfaitement normal en début de monnaie et va d'autant s'accélérer que la Ğ1 gagnera en popularité. La toile va donc très probablement continuer à se tendre jusqu'à ce que la règle de distance devienne bloquante.

  À ce moment-là, le flux d'entrée de nouveaux va ralentir et les membres qui étaient alors très actifs vers l'extérieur devront se mettre à certifier vers l'intérieur pour densifier un peu la toile afin que celle-ci puisse de nouveau acceuillir.
Là encore c'est un phénomène normal en début de monnaie et même souhaitable car cette contrainte sur les entrées limitera également les éventuelles micro-attaques sybil en cours (les petites fraudes) de sorte qu'elles restent microscopiques par rapport à la taille de la toile.

  *Aparté : je rapelle qu'il est impossible d'empêcher les petites fraudes, il y en aura forcément, peut-être même qu'il y en a déjà, la seule chose que l'on peut et que l'on doit faire c'est contraindre ces petites fraudes à rester marginales pour que la globalité de la toile reste de confiance et c'est précisement le rôle de la règle de distance.*

  Voila pourquoi il est important d'insister auprès des autres membres de la Ğ1 que vous rencontrez sur le fait qu'il doivent certifier les membres qu'ils connaissent personnellement même s'ils sont déjà membres et qu'il doivent le faire sans attendre.
Ce point-là n'est pas toujours bien expliqué et encore moins compris, et c'est bien compréhensible vu la quantité de nouveaux concepts à intégrer par ailleurs, mais si nous n'insistons pas suffisamment sur l'importance des certifications internes alors il y aura peut-être beaucoups d'incompréhensions lorsque la règle de distance deviendra bloquante, et cette incompréhension pourrait provoquer de la méfiance et freiner la popularité de la Ğ1.

  Il convient de nuancer ce propos global en précisant que la toile se régionalise, ainsi la règle de distance ne deviendra contraignantes que dans certaines régions et pas du tout dans d'autres, il suffit pour anticiper cela de surveiller les membres à la qualité la plus faible, et s'il commence à s'en concentrer beaucoup dans une même région, nous pouvons très bien contacter directement les groupes locaux de cette région, et par la même occassion leur apprendre à utiliser g1-monit pour surveiller eux-mêmes leur propre situation à l'avenir.
  
## Conclusion

  Les différents indicateurs de l'état de tension de la toile nous permettront de voir venir de loin, et c'est tout l'objectif du développement de g1-monit et de la rédaction de ces rapports : éveiller votre vigilance afin que vous surveilliez vous-même votre toile de confiance, après tout c'est un bien commun :)

  Certains sont d'avis que la règle de distance est trop contraignante et qu'il faudra l'assouplir, d'autres que les règles actuelles conviennent parfaitement et que les membres de la Ğ1 sont capables de réguler d'eux-mêmes l'équilibre entre leurs  certifications internes et externes. Les membres de la Ğ1 seront-ils suffisamment vigilants pour réguler la toile d'eux-mêmes ? J'espère que la réponse est oui, le suivi des statistiques détaillés de la toile nous le dira :)
