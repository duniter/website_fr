Title: Duniter version 1.3.14
Date: 2017-07-05
Category: Technique
Tags: release
Slug: duniter-version-1.3.14
Authors: cgeek
Thumbnail: /images/box.svg

La version 1.3.14 de Duniter est désormais [disponible au téléchargement](https://github.com/duniter/duniter/releases/tag/v1.3.14) !

## Correctifs

Cette version compile les correctifs jusqu'à la version 1.3.13, et apporte une touche finale concernant le réseau Duniter qui avait tendance à forker régulièrement ces dernières semaines.

Il semble qu'un bug au niveau du contact en IPv6 soit à l'origine du problème. L'IPv6 est donc désormais mise en dernier choix pour contacter un nœud, l'ordre de préférence est maintenant : DNS, IPv4, IPv6.

Ce correctif a été testé sur un nœud du réseau Ğ1, qui révèle immédiatement des nœuds considérés éteints de longue date du point de vue de ce nœud, qui les considère à nouveau *allumés et disponibles*.

## Synchronisation

> <span class="icon">![](../images/icons/white_check_mark.png)</span> Pas besoin de resynchroniser.

## Compatibilité

> <span class="icon">![](../images/icons/white_check_mark.png)</span> Compatible avec la Ğ1.

-----

## Mettre à jour sa version

* Lien pour [installer la nouvelle version](https://github.com/duniter/duniter/blob/master/doc/install-a-node.md) depuis un poste vierge
* Lien pour [mettre à jour vers la nouvelle version](https://github.com/duniter/duniter/blob/master/doc/update-a-node.md) depuis une installation existante
