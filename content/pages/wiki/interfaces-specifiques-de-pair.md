Title: Interfaces spécifiques d'un pair
Order: 9
Date: 2017-03-31
Slug: interfaces-specifiques-de-pair
Authors: cgeek

> Reprise d'un [commentaire sur le ticket GitHub #337](https://github.com/duniter/duniter/issues/337#issuecomment-251380492).

### Ajouter une interface

```
duniter config --addep "SUPER_ENDPOINT_ELASTIC_SEARCH cgeek.fr blablabla 21020"
```

Ce qui produit :

```json
{
  "version": 2,
  "currency": "test_net",
  "endpoints": [
    "BASIC_MERKLED_API cgeek.fr 88.174.120.187 2a01:e35:8ae7:8bb0:b468:a0c:a607:379f 9330",
    "BASIC_MERKLED_API 88.174.120.187 9333",
    "SUPER_ENDPOINT_ELASTIC_SEARCH cgeek.fr blablabla 21020"
  ],
  "block": "44041-0000297B14119AC6710D493D773821B11E016DBE317E778FF8B0B5BC347B8039",
  "signature": "tgNB44JiHBuP3G1DsQthkTFBrghNX7me1R5XACx15SQ1RC39yuqhaHWhy94rYttJRgsWNPOQPRmfuEDs6bM7BQ==",
  "pubkey": "HnFcSms8jzwngtVomTTnzudZx7SHUQY8sVE1y8yBmULk"
}
```

### Supprimer une interface

```
duniter config --remep "SUPER_ENDPOINT_ELASTIC_SEARCH cgeek.fr blablabla 21020"
```

Ce qui produit :

```json
{
  "version": 2,
  "currency": "test_net",
  "endpoints": [
    "BASIC_MERKLED_API cgeek.fr 88.174.120.187 2a01:e35:8ae7:8bb0:b468:a0c:a607:379f 9330",
    "BASIC_MERKLED_API 88.174.120.187 9333"
  ],
  "block": "44041-0000297B14119AC6710D493D773821B11E016DBE317E778FF8B0B5BC347B8039",
  "signature": "tgNB44JiHBuP3G1DsQthkTFBrghNX7me1R5XACx15SQ1RC39yuqhaHWhy94rYttJRgsWNPOQPRmfuEDs6bM7BQ==",
  "pubkey": "HnFcSms8jzwngtVomTTnzudZx7SHUQY8sVE1y8yBmULk"
}
```

### Précautions

Une bonne pratique est de réaliser ces opérations **exclusivement sur un seul nœud**, qui s'occupera de gérer les interfaces spécifiques. Car si vous avez :

* un nœud qui ajouter l'interface `EP1`
* un *autre* nœud qui supprime l'interface `EP1`

Alors vous tomberez dans un [ping-pong infini](../cles-partagees#le-stock-de-blockstamp), ce qui consommera tout le stock disponible de tampons temporels pour émettre de nouvelles fiches de pair. Vous n'aurez alors plus la possibilité de mettre à jour votre fiche de pair avant qu'un nouveau bloc apparaisse.
