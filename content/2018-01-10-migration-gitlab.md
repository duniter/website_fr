Title: Migration sous gitlab
Date: 2017-11-18
Category: Technique
Tags: gitlab
Slug: migration-gitlab
Authors: inso
Thumbnail: /images/code.svg

En 2018, nous migrons nos dépôts de code Duniter sous [Gitlab](https://git.duniter.org). 
Dorénavant, nous ne dépendons plus d'une plateforme privatrice pour publier nos releases et maintenir nos issues.

Tout a été migré : les issues, les dépôts Git, et même les comptes utilisateurs ! 
Il est par ailleurs possible de se connecter en utilisant ses logins Github. 

Vous retrouverez notamment les dépôts suivant : 
  - Le dépôt de [Duniter Typescript](https://git.duniter.org/nodes/typescript/)
  - Le dépôt de [Duniter Rust](https://git.duniter.org/nodes/rust/)
  - Le dépôt de [Cesium](https://git.duniter.org/clients/cesium)

Comme sur Github, si vous souhaitez contribuer, vous pouvez fourcher le projet, créer des issues, etc.
  
Nous profitons également de cette migration pour **changer notre manière de faire évoluer le protocole.** 
Nous avons mis en place un [dépot dédié aux RFC du protocole](https://git.duniter.org/nodes/common/doc).
Les propositions d'améliorations et d'évolution du protocole sont gérées à travers des [merge request](https://git.duniter.org/nodes/common/doc/merge_requests)
sur le dépôt.

