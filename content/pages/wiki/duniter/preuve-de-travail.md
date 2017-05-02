Title: Preuve de travail
Order: 9
Date: 2017-05-02
Slug: preuve-de-travail
Authors: cgeek

## L'empreinte

Exemple d'empreinte valide :

```
00000276902793AA44601A9D43099E7B63DBF9EBB55BCCFD6AE20C729B54C653
```

On peut voir que cette empreinte démarre par 5 zéros : réaliser une telle empreinte demande beaucoup de *travail* de la part d'un ordinateur, d'où le fait qu'on appelle l'opération consistant à réaliser une telle empreinte « *preuve de travail* ».

## Le Nonce

Il s'agit du champ du document `Block` permettant de faire varier l'empreinte finale du bloc, empreinte qui définit le niveau de la preuve de travail.

Exemples de valeurs de Nonce :

* 10100000112275
* 10300000288743
* 10400000008538
* 10700000079653
* 10300000070919

En réalité ces valeurs de `Nonce` suivent toutes un même schéma `XYY00000000000`. Le Nonce ne correspond pas aux nombres d'essais, mais plutôt à un espace de Nonce possible. La décomposition est la suivante :

* X correspond au numéro de pair. Par exemple toi qui a plusieurs nœuds avec ta clé personnelle et donc tous capable de calculer, chacun de tes nœuds réaliser sa preuve avec un X différent, afin de ne pas calculer la même preuve justement. Car potentiellement, ils réalisent exactement le même prochain bloc (puisque l'émetteur est le même, le contenu possiblement identique, seul le Nonce peut varier), donc il faut avoir un Nonce qui les différencie.
* Y correspond au numéro de cœur du processeur. On peut voir par exemple que quelqu'un possède au moins 7 cores dans son CPU ici, car on lit le Nonce `107[...]`. Un serveur avec 99 cores pourrait réaliser une preuve `199[...]` par exemple.

Le reste du Nonce, la partie derrière XYY, est l'espace de Nonce du nœud pour chaque core du CPU. Ce qui fait donc un espace de 11 chiffres (`00000000000`) pour trouver un Nonce correct pour chaque core du CPU de la machine (CPU au sens large, ce peut-être un bi-CPU, on considère le nombre de cores résultants pour la PoW).
