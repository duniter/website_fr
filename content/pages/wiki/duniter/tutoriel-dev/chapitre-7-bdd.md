Title: 7. Base de données
Order: 1
Date: 2017-11-07
Slug: chapitre-7-bdd
Authors: cgeek

## Introduction

Ce chapitre s'attarde à décrire la structure, les champs et les relations de la base de données de Duniter. Il s'agit d'une base de données SQLite, en un seul fichier.

Ainsi vous pourrez vous-même extraire des informations de la blockchain Duniter et de sa toile de confiance en rédigeant les requêtes SQL qui vous intéressent.

## Vue générale

::uml::

@startuml

database "\nBase de donnees Duniter (SQLite)" {

  package "Index Blockchain" {
      component b_index
      component m_index
      component i_index
      component s_index
      component c_index
  }

  package "Piscines" {
      component idty
      component cert
      component membership
      component txs
  }

  package "Autre" {
      component block
      component peer
      component wallet
      component meta
  }
}

@enduml

::end-uml::

### Table `block`

Contient les blocs soumis par le réseau, aussi bien les blocs acceptés en blockchain par le nœud local que les blocs de fork. C'est une table d'archive, les données qu'elle contient ne sont pas directement exploitées.

Éventuellement en cas de résolution de fork, Duniter vient piocher parmi les blocs avec `fork = 1` pour rejoindre une autre chaîne présente dans sa base de données.

##### fork (`BOOLEAN NOT NULL`)

Indique si le bloc est dans la blockchain courante ou s'il s'agit d'un fork.

##### hash (`VARCHAR(64) NOT NULL`)

Empreinte SHA256 du bloc.

##### inner_hash (`VARCHAR(64) NOT NULL`)

Empreinte SHA256 de la partie interne bloc, c'est-à-dire jusqu'à `InnerHash: ` exclu.

##### signature (`VARCHAR(100) NOT NULL`)

Signature de l'émetteur du bloc.

##### currency (`VARCHAR(50) NOT NULL`)

Nom de code de la monnaie.

##### issuer (`VARCHAR(50) NOT NULL`)

Clé publique émettrice du bloc.

##### parameters (`VARCHAR(255)`)

Uniquement pour le bloc#0 : paramètres initiaux de la monnaie.

##### previousHash (`VARCHAR(64)`)

Empreinte SHA256 du bloc précédent (hash).

##### previousIssuer (`VARCHAR(50)`)

Clé publique de l'émetteur du bloc précédent (issuer).

##### version (`INTEGER NOT NULL`)

Numéro de version du bloc.

##### membersCount (`INTEGER NOT NULL`)

Nombre de membres calculés pour ce bloc.

##### monetaryMass (`VARCHAR(100) DEFAULT '0'`)

Masse monétaire calculée pour ce bloc.

##### UDTime (`DATETIME`)

> *Champ historique non utilisé*. Vaut toujours `null`.

##### medianTime (`DATETIME NOT NULL`)

Temps moyen des 12 derniers blocs (pour la Ğ1).

##### dividend (`INTEGER DEFAULT '0'`)

Montant du Dividende Universel pour ce bloc, ou null si pas de dividende.

##### unitbase (`INTEGER NULL`)

Unité relative du dividende en puissance de 10. Le montant absolu du dividende est dividende*PUISSANCE(10, unitbase).

##### time (`DATETIME NOT NULL`)

Temps instantané pour ce bloc.

##### powMin (`INTEGER NOT NULL`)

Difficulté commune minimale calculée pour ce bloc.

##### number (`INTEGER NOT NULL`)

Numéro du bloc.

##### nonce (`INTEGER NOT NULL`)

Valeur du champ incrémental permettant de faire varier la preuve de travail.

##### transactions (`TEXT`)

Liste des transactions du bloc (format compact).

##### certifications (`TEXT`)

Liste des certifications du bloc (format compact).

##### identities (`TEXT`)

Liste des identités du bloc (format compact).

##### joiners (`TEXT`)

Liste des adhésions du bloc (format compact).

##### actives (`TEXT`)

Liste des adhésions de renouvellement du bloc (format compact).

##### leavers (`TEXT`)

Liste des adhésions de sortie du bloc (format compact).

##### revoked (`TEXT`)

Liste des révocations du bloc (format compact).

##### excluded (`TEXT`)

Liste des clés publiques exclues du bloc.

##### created (`DATETIME DEFAULT NULL`)

> *Champ historique non utilisé*. Vaut toujours `null`.

##### updated (`DATETIME DEFAULT NULL`)

> *Champ historique non utilisé*. Vaut toujours `null`.

##### issuersFrame (`INTEGER NULL`)

Taille de la fenêtre d'émetteurs calculée du bloc.

##### issuersFrameVar (`INTEGER NULL`)

Variation de la taille de la fenêtre calculée du bloc.

##### issuersCount (`INTEGER NULL`)

Nombre d'émetteurs différents dans la fenêtre, calculé du bloc.

##### len (`INTEGER NULL`)

Taille du bloc.

### Table `idty`

Piscine des identités : table où les identités en attente d'inscription dans la blockchain sont répertoriées. Lorsqu'une identité est finalement inscrite en blockchain, elle disparaît de la table `idty`.

##### revoked (`BOOLEAN NOT NULL`)

Indique si l'identité possède déjà une révocation attachée.

##### currentMSN (`INTEGER NULL`)

> *Champ historique non utilisé*. Vaut toujours `null`.

##### currentINN (`INTEGER NULL`)

> *Champ historique non utilisé*. Vaut toujours `null`.

##### buid (`VARCHAR(100) NOT NULL`)

Blockstamp attaché à l'identité.

##### member (`BOOLEAN NOT NULL`)

> *Champ historique non utilisé*. Vaut toujours `0`.

##### kick (`BOOLEAN NOT NULL`)

> *Champ historique non utilisé*. Vaut toujours `0`.

##### leaving (`BOOLEAN NULL`)

> *Champ historique non utilisé*. Vaut toujours `0`.

##### wasMember (`BOOLEAN NOT NULL`)

> *Champ historique non utilisé*. Vaut toujours `0`.

##### pubkey (`VARCHAR(50) NOT NULL`)

Clé publique gérant l'identité.

##### uid (`VARCHAR(255) NOT NULL`)

Pseudonyme attaché à l'identité.

##### sig (`VARCHAR(100) NOT NULL`)

Signature du document d'identité.

##### revocation_sig (`VARCHAR(100) NULL`)

Signature de révocation. Champ à `null` si pas de révocation attachée.

##### hash (`VARCHAR(64) NOT NULL`)

Empreinte SHA256 du document d'identité.

##### written (`BOOLEAN NULL`)

> *Champ historique non utilisé*. Vaut toujours `0`.

##### wotb_id (`INTEGER NULL`)

> *Champ historique non utilisé*. Vaut toujours `null`.

##### expires_on (`INTEGER NULL`)

Horodatage du moment où l'identité périmera hors blockchain.

##### expired (`INTEGER NULL`)

> *Champ historique non utilisé*. Vaut toujours `null`.

##### revoked_on (`INTEGER NULL`)

> *Champ historique non utilisé*. Vaut toujours `null`.

##### removed (`BOOLEAN NULL DEFAULT 0`)

> *Champ historique non utilisé*. Vaut toujours `null`.

### Table `cert`

Piscine des certifications : table où les certifications en attente d'inscription dans la blockchain sont répertoriées. Lorsqu'une certification est finalement incluse dans un bloc, elle disparaît de la table `cert`.

##### to (`VARCHAR(50) NOT NULL`)

Clé publique ciblée par la certification.

##### target (`CHAR(64) NOT NULL`)

Empreinte SHA256 de l'identité ciblée par la certification. Utile quand une identité n'est pas encore membre, car la clé publique peut encore créer autant d'identités qu'elle le souhaite. Le champ `target` permet de cibler de façon unique l'identité certifiée, même si la clé publique `to` est la même pour plusieurs identités.

> Note : `idty.hash = cert.target` permet d'obtenir les certifications reçues par une identité.

##### sig (`VARCHAR(100) NOT NULL`)

Signature du document de certification.

##### block_number (`INTEGER NOT NULL`)

Numéro de bloc du blockstamp.

##### block_hash (`VARCHAR(64)`)

Hash de bloc du blockstamp.

##### block (`INTEGER NOT NULL`)

Alias de `block_number`.

##### linked (`BOOLEAN NOT NULL`)

> *Champ historique non utilisé*. Vaut toujours `0`.

##### written (`BOOLEAN NOT NULL`)

> *Champ historique non utilisé*. Vaut toujours `0`.

##### written_block (`INTEGER`)

> *Champ historique non utilisé*. Vaut toujours `null`.

##### written_hash (`VARCHAR(64)`)

> *Champ historique non utilisé*. Vaut toujours `null`.

##### expires_on (`INTEGER NULL`)

Horodatage du moment où la certification périmera hors blockchain.

##### expired (`INTEGER NULL`)

> *Champ historique non utilisé*. Vaut toujours `0`.

### Table `membership`

Piscine des adhésions : table où les adhésions en attente d'inscription dans la blockchain sont répertoriées. Lorsqu'une adhésion est finalement incluse dans un bloc, elle disparaît de la table `membership`.

##### issuer (`VARCHAR(50) NOT NULL`)

Clé publique de l'émetteur de l'adhésion.

##### number (`INTEGER NOT NULL`)

Numéro de bloc du blockstamp pour l'adhésion.

##### blockNumber (`INTEGER`)

Alias de `number`.

##### blockHash (`VARCHAR(64) NOT NULL`)

Hash du blockstamp pour l'adhésion.

##### userid (`VARCHAR(255) NOT NULL`)

Pseudonyme de l'identité concernée par l'adhésion.

##### certts (`VARCHAR(100) NOT NULL`)

Blockstamp de l'identité concernée par l'adhésion.

##### block (`INTEGER`)

Blockstamp de l'adhésion.

##### fpr (`VARCHAR(64)`)

Alias de `blockHash`.

##### idtyHash (`VARCHAR(64)`)

Empreinte SHA256 de l'identité concernée par l'adhésion.

> Note : `membership.idtyHash = idty.hash = cert.target` permet d'obtenir les documents d'un dossier d'identité.

##### written (`BOOLEAN NOT NULL`)

> *Champ historique non utilisé*. Vaut toujours `0`.

##### written_number (`INTEGER`)

> *Champ historique non utilisé*. Vaut toujours `null`.

##### expires_on (`INTEGER NULL`)

Horodatage du moment où l'adhésion périmera hors blockchain.

##### signature (`VARCHAR(50)`)

Signature du document d'adhésion.

##### expired (`INTEGER NULL`)

> *Champ historique non utilisé*. Vaut toujours `null`.

### Table `txs`

Registre des transactions. Contient à la fois les transactions en piscine et les transactions incluses dans un bloc. Lorsqu'une transaction de piscine est finalement incluse dans un bloc, le champ `written` est valorisé à `1`.

##### hash (`CHAR(64) NOT NULL`)

Empreinte SHA256 du document de transaction brut (non compact).

##### block_number (`INTEGER`)

Numéro de bloc du blockstamp.

##### locktime (`INTEGER NOT NULL`)

Variable `locktime` de la transaction.

##### version (`INTEGER NOT NULL`)

Numéro de version de la transaction.

##### currency (`VARCHAR(50) NOT NULL`)

Monnaie concernée par la transaction.

##### comment (`VARCHAR(255) NOT NULL`)

Commentaire éventuel pour la transaction.

##### time (`DATETIME`)

Horodatage du 

##### inputs (`TEXT NOT NULL`)

Tableau JSON des sources consommées par la transaction.

##### unlocks (`TEXT NOT NULL`)

Tableau JSON des clés de déverrouillage des `inputs`.

##### outputs (`TEXT NOT NULL`)

Tableau JSON des sources créées par la transaction.

##### issuers (`TEXT NOT NULL`)

Tableau JSON des émetteurs (ckés publiques) de la transaction.

##### signatures (`TEXT NOT NULL`)

Tableau JSON des signatures de la transaction.

##### recipients (`TEXT NOT NULL`)

Tableau JSON des destinataires (clés publiques) de la transaction.

##### written (`BOOLEAN NOT NULL`)

Booléen indiquant si la transaction a été écrite ou non.

##### removed (`BOOLEAN NOT NULL`)

> *Champ historique non utilisé*. Vaut toujours `0`.

##### received (`INTEGER NULL`)

> *Champ historique non utilisé*. Vaut toujours `null`.

##### output_base (`INTEGER NULL`)

Champ calculé : base du montant de sortie de la transaction.

##### output_amount (`INTEGER NULL`)

Champ calculé : montant de sortie de la transaction.

##### blockstamp (`VARCHAR(200) NULL`)

Blockstamp de la transaction.

##### len (`INTEGER NULL`)

Longueur compacte de la transaction.

##### blockstampTime (`INTEGER NULL`)

`medianTime` du bloc référencé par le blockstamp de la transaction.

### Table `peer`

##### version (`INTEGER NOT NULL`)

Numéro de version de la fiche de pair.

##### currency (`VARCHAR(50) NOT NULL`)

Nom de la monnaie ciblée par la fiche de pair.

##### status (`VARCHAR(10)`)

Statut du pair : 'UP' ou 'DOWN'.

##### statusTS (`INTEGER NOT NULL`)

Horodatage du statut.

##### hash (`CHAR(64)`)

Empreinte SHA256 du document de fiche de pair.

##### first_down (`INTEGER`)

Horodatage de la 1ère occurrence du statut 'DOWN' si le statut courant est 'DOWN'.

##### last_try (`INTEGER`)

Horodagate de la dernière tentative de connexion au pair.

##### pubkey (`VARCHAR(50) NOT NULL`)

Clé publique du nœud inscrit dans la fiche de pair.

##### block (`VARCHAR(60) NOT NULL`)

Blockstamp de la fiche de pair.

##### signature (`VARCHAR(100)`)

Signature du document de fiche de pair.

##### endpoints (`TEXT NOT NULL`)

Liste des points d'accès du nœud.

##### raw (`TEXT`)

Document en version brute.

### Table `wallet`

Table stockant la balance courante de chaque compte.

##### conditions (`TEXT NOT NULL`)

Identifiant du compte.

##### balance (`INTEGER NOT NULL`)

Balance courante, positive ou nulle.

### Table `meta`

Table de méta-informations sur la base de données. Ne contient qu'une seule ligne.

##### id (`INTEGER NOT NULL`)

Valeur `1`.

##### version (`INTEGER NOT NULL`)

Numéro de version.

### Table `b_index`

Table d'index pour les blocs. Enregistre une ligne calculée par bloc.

##### version (`INTEGER NOT NULL`)

Identique à `block.version`.

##### bsize (`INTEGER NOT NULL`)

Taille du bloc.

##### hash (`VARCHAR(64) NOT NULL`)

Identique à `block.hash`.

##### issuer (`VARCHAR(50) NOT NULL`)

Identique à `block.issuer`.

##### time (`INTEGER NOT NULL`)

Identique à `block.time`.

##### number (`INTEGER NOT NULL`)

Identique à `block.number`.

##### membersCount (`INTEGER NOT NULL`)

Identique à `block.membersCount`.

##### issuersCount (`INTEGER NOT NULL`)

Identique à `block.issuersCount`.

##### issuersFrame (`INTEGER NOT NULL`)

Identique à `block.issuersFrame`.

##### issuersFrameVar (`INTEGER NOT NULL`)

Identique à `block.issuersFrameVar`.

##### issuerDiff (`INTEGER NULL`)

Difficulté associée à l'émetteur du bloc (issuer).

##### avgBlockSize (`INTEGER NOT NULL`)

Taille moyenne des blocs précédents.

##### medianTime (`INTEGER NOT NULL`)

Identique à `block.medianTime`.

##### dividend (`INTEGER NOT NULL`)

Identique à `block.dividend`.

##### mass (`VARCHAR(100) NOT NULL`)

Masse monétaire calculée pour ce bloc.

##### unitBase (`INTEGER NOT NULL`)

Identique à `block.unitBase`.

##### powMin (`INTEGER NOT NULL`)

Identique à `block.powMin`.

##### udTime (`INTEGER NOT NULL`)

Horodatage du prochain Dividende Universel.

##### udReevalTime (`INTEGER NOT NULL`)

Horodatage de la prochaine réévaluation du Dividende Universel.

##### diffNumber (`INTEGER NOT NULL`)

Numéro du prochain bloc où la difficulté commune sera réévaluée.

##### speed (`FLOAT NOT NULL`)

Vitesse actuelle d'évolution de la blockchain (blocs/seconde).

##### massReeval (`VARCHAR(100) NOT NULL DEFAULT '0'`)

Masse monétaire lors de la dernière réévaluation du Dividende Universel.

### Table `i_index`

Table d'index concernant les identités. Enregistre de zéro à plusieurs lignes par bloc.

##### op (`VARCHAR(10) NOT NULL`)

Type d'opération : 'CREATE' ou 'UPDATE'.

##### uid (`VARCHAR(100) NULL`)

Pseudonyme de l'identité.

##### pub (`VARCHAR(50) NOT NULL`)

Clé publique de l'identité.

##### hash (`VARCHAR(80) NULL`)

Empreinte SHA256 du document d'identité.

##### sig (`VARCHAR(80) NULL`)

Signature du document d'identité.

##### created_on (`VARCHAR(80) NULL`)

Blockstamp de l'identité.

##### written_on (`VARCHAR(80) NOT NULL`)

Blockstamp du bloc où est écrite l'identité.

##### member (`BOOLEAN NULL`)

L'identité est-elle membre ou non.

##### wasMember (`BOOLEAN NULL`)

L'identité a-t-elle été membre ou non (note : champ inutile, sinon il n'y aurait pas d'enregistrement). Valeur `1`.

##### kick (`BOOLEAN NULL`)

L'identité doit-elle être exclue au prochain bloc ?

##### wotb_id (`INTEGER NULL`)

Identifiant interne de WoT. Alias pour la clé publique, sous forme d'entier.

##### writtenOn (`INTEGER NOT NULL DEFAULT 0`)

Numéro du bloc d'écriture.

### Table `c_index`

Table d'index pour les certifications. Enregistre zéro à plusieurs lignes par bloc.

##### op (`VARCHAR(10) NOT NULL`)

Type d'opération : 'CREATE' ou 'UPDATE'.

##### issuer (`VARCHAR(50) NOT NULL`)

Clé publique de l'émetteur de la certification.

##### receiver (`VARCHAR(50) NOT NULL`)

Clé publique du receveur de la certification.

##### created_on (`VARCHAR(80) NOT NULL`)

Blockstamp de la certification.

##### written_on (`VARCHAR(80) NOT NULL`)

Blockstamp du bloc contenant la certification.

##### sig (`VARCHAR(100) NULL`)

Signature du document de certification.

##### expires_on (`INTEGER NULL`)

Horodatage déterminant la date d'expiration de la certification une fois écrite en blockchain.

##### expired_on (`INTEGER NULL`)

Horodatage du moment où a expiré la certification en blockchain.

##### chainable_on (`INTEGER NULL`)

Horodatage du moment où la certification pourra être rejouée.

##### from_wid (`INTEGER NULL`)

Identifiant interne WoT de l'émetteur.

##### to_wid (`INTEGER NULL`)

Identifiant interne WoT du receveur.

##### writtenOn (`INTEGER NOT NULL DEFAULT 0`)

Numéro du bloc d'écriture.

### Table `m_index`

Table d'index des adhésions. Enregistre zéro à plusieurs enregistrements par bloc.

##### op (`VARCHAR(10) NOT NULL`)

Type d'opération : 'CREATE' ou 'UPDATE'.

##### pub (`VARCHAR(50) NOT NULL`)

Clé publique de l'émetteur de l'adhésion.

##### created_on (`VARCHAR(80) NOT NULL`)

Blockstamp de l'adhésion.

##### written_on (`VARCHAR(80) NOT NULL`)

Blockstamp du bloc d'écriture.

##### expires_on (`INTEGER NULL`)

Horodatage du moment où expirera l'adhésion.

##### expired_on (`INTEGER NULL`)

Horodatage du moment où a expiré l'adhésion, ou `null` si l'adhésion n'a pas encore expiré.

##### revokes_on (`INTEGER NULL`)

Horodatage du moment où l'adhésion sera implicitement révoquée.

##### revoked_on (`INTEGER NULL`)

Horodatage du moment où l'adhésion a implicitement été révoquée, ou `null` si l'adhésion n'a pas encore été implicitement révoquée.

##### leaving (`BOOLEAN NULL`)

La dernière adhésion est-elle de type « quitter » ?

##### revocation (`VARCHAR(80) NULL`)

Signature de la révocation d'identité, ou `null` sinon.

##### chainable_on (`INTEGER NULL`)

Horodatage du moment où l'adhésion pourra être rejouée.

##### writtenOn (`INTEGER NOT NULL DEFAULT 0`)

Numéro du bloc d'écriture.

### Table `s_index`

Table d'index pour les sources de transactions. Enregistre zéro à plusieurs lignes par bloc.

##### op (`VARCHAR(10) NOT NULL`)

Type d'opération : 'CREATE' ou 'UPDATE'.

##### tx (`VARCHAR(80) NULL`)

Empreinte SHA256 de la transaction source, ou `null` pour un dividende.

##### identifier (`VARCHAR(64) NOT NULL`)

Identifiant de la source : soit une empreinte SHA256 de transaction, soit une clé publique de membre.

##### pos (`INTEGER NOT NULL`)

Position de la source.

##### created_on (`VARCHAR(80) NULL`)

Blockstamp de la transaction.

##### written_on (`VARCHAR(80) NOT NULL`)

Blockstamp du bloc d'écriture.

##### written_time (`INTEGER NOT NULL`)

Horodatage du bloc d'écriture (champ `medianTime`).

##### amount (`INTEGER NULL`)

Montant de la source, dans la base de la transaction.

##### base (`INTEGER NULL`)

Base de la transaction (puissance de 10).

##### locktime (`INTEGER NULL`)

Durée de verrouillage de la transaction.

##### consumed (`BOOLEAN NOT NULL`)

Indique si la source a été consommée.

##### conditions (`TEXT`)

Conditions de déverrouillage de la source.

##### writtenOn (`INTEGER NOT NULL DEFAULT 0`)

Numéro du bloc d'écriture.

> Passer à la suite du tutoriel : [Chapitre 8 : Addons C/C++](../chapitre-8-addons).
