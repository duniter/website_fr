Title: Préconisations pour développer un client Duniter
Order: 1
Date: 2017-07-19
Tags: wiki, preconisations, client
Slug: wiki
Authors: galuel

## Consultation générale

Un client Duniter devrait par défaut proposer la consultation au minimum des paramètres théoriques et calculés :

* Paramètres de la monnaie (M, M/N, c, formule du Dividende, etc.)
* Paramètres de la Toile de Confiance (Nombre de signatures pour devenir membre, membre référent, temps, limites etc.)
* Paramètres de la blockchain (temps moyen de calcul de blocs, difficultés etc.)

* Consultation de la monnaie (y compris transactions en piscine)
* Consultation de la TdC (y compris certifications / adhésions / renouvellements en piscine)
* Consultation de la blockchain (noeuds, blocs...)

## Consultation de compte

La consultation de tout compte ne nécessitant que la clé publique du compte (ou l'ID unique) la consultation devrait pouvoir s'effectuer concernant tout compte sous les formats possibles, au choix et dans l'ordre :

* Par clé publique
* Par ID
* Par clé privée

## Emissions de documents Duniter

L'émission de documents Duniter, nécessitant toujours la saisie de la clé privée, ne devrait jamais par défaut se faire via un enregistrement de la clé privée, et devrait dans l'ordre toujours présenter des avertissements avant la signature (et surtout pas après !) :

* Présentation systématique de la licence Ğ1
* Présentation d'un avertissement rappelant le type de documents en cours de signature (demande d'adhésion, renouvellement, certification, transaction)
* Signature demandée + effacer toute trace de la clé privée de la mémoire une fois le document généré.
* Récapitulatif complet (ex : tel compte pubkey/ID certifie tel compte pubkey/ID, rappel des avertissements)
* Temps de latence minimum (ex : 10 secondes)
* Envoi définitif du document (ou annulation)
