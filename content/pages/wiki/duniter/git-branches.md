Title: Fonctionnement des branches du dépot git Duniter
Order: 9
Date: 2017-09-22
Slug: configurer
Authors: elois

Le [dépot git duniter](https://github.com/duniter/duniter) a de nombreuses branches, voici comment savoir sur quel branche vous devez contribuer en fonction de ce que vous voulez faire :

## Master : uniquement pour la doc

La branche master correspond a une veille version oldstable, seule la partie doc est mise à jours car c'est la doc de cette branche qui est généralement consultée par ceux qui ne connaissent pas le projet.

## Pour contribuer au code (hors protocole DUP)

Créez une nouvelle branche a partir de la branche `dev`.

Développez, puis soumettez une PR `from` votre branche into `dev`.

Si vous faîte parti de l'organisation Duniter, que votre contribution est mineure (type et petits correctifs) et que vous êtes sûr de vous, vous pouvez pusher votre correctif directement sur la branche dev.

## Pour contribuer au protocole DUP (correctif ou évolution)

Discutez en dabord avec nous [sur le forum](https://forum.duniter.org), le protocole DUP ne peut pas être modifié comme ça !
En tout les cas de telles contributions ne se feront pas sur la branche dev mais sur une branche dédiée a la prochaine version majeure. Actuellement (novembre 2017) il s'agit de la branche `2.0-dev`.

## Les branches de version (`1.6` par exemple)

Les branches de version permettent d'apporter un éventuel path a une version stable si cela est nécessaire et ne peut attendre la version stable suivante. Nous pouvons ainsi librement expérimenter sans risquer de casser les versions stables déjà publiés !

## Les autres branches

Vous pouvez les ignorer, il s'agit de travaux en cours de développeurs membres de l'organisation duniter.
