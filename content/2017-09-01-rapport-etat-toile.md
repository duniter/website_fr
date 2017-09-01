Title: État de la toile de confiance Ğ1 au 1er Septembre 2017
Date: 2017-09-01
Category: Toile de confiance
Tags: wot, toile de confiance
Slug: rapport-etat-wot
Authors: elois
Thumbnail: /images/network.svg

Depuis le [4 juillet 2017](https://forum.duniter.org/t/currency-monit-monitoring-dune-monnaie-et-de-sa-toile-de-confiance/2770/17?u=elois) je tiens des statistiques détaillés sur l'état de la toile de confiance que vous pouvez visualiser sur [g1-monit](https://g1-monit.elois.org)

Bilan deux semaines après le passage du palier Y[n]=4 : 

l'effet de densification du palier s'est déjà dissipé, la toile de confiance est de nouveau aussi tendue qu'avant le passage du palier, voir même légèrement davantage : 

*  La proportion de membre ayant une qualité >=1 à chuté à **82%** soit environ le même niveau, qu'avant le palier (83%)
* De plus, une dizaine de membres commencent a chuter a des niveau de qualité très faibles (inférieurs à 0.9), ce qui veut dire qu'ils commencent a être trop distants des membres référents :  https://g1-monit.elois.org/gaussianWotQuality?lg=fr
* D'ailleurs sur les 79 futurs membres ayant reçu au moins 1 certifications, 7 d'entre eux ne respectent pas la règle de distance, 3 ont été certifiés par le même membre mais cela fait quand même **4 cas différents de non-respect de la règle de distance.**
* Un autre indicateur nous montre bien la tension de la toile, **l'augmentation de la longueur moyenne du plus court chemin entre deux membres :** désormais 4,13, cette valeur a continuellement augmentée même lors du passage du palier car elle est indépendante de la notion de membre référent, elle montre l'état de tension de la toile entière là ou la qualité ne montre que l'état de tension d'un sous ensemble de la toile (le sous-ensemble des liens référent->membre).
* Enfin le nombre de membres référents est quand a lui est repassé au dessus de sa valeur d'avant le palier (153) : 
<img src="https://librelois.fr/public/fin-effet-palier-yn-4.png" width="690" height="339">

La situation est encore loin d'être bloquante, mais la toile n'a jamais été aussi tendue depuis que je tiens des statistiques très détaillés sur son état, c'est à dire depuis le 4 juillet 2017.
