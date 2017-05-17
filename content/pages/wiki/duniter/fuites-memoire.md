Title: Fuites mémoire
Order: 9
Date: 2017-05-11
Slug: fuites-memoire
Authors: cgeek

Il se peut que Duniter manifeste une utilisation trop élevée de la mémoire de sa machine : ceci peut être dû à une fuite mémoire.

Aussi, la version *Duniter Server* dispose d'un mécanisme permettant d'analyser la mémoire consommée par Duniter.

## Enregistrement de l'empreinte mémoire

À tout moment, il est possible d'enregistrer la consommation détaillée de Duniter en termes de mémoire (Linux seulement). On parle de produire un *heapdump*, ou rapport de mémoire utilisée.

Pour produire ce dump, déterminer l'identifiant de processus de Duniter :

    ps aux | grep duniter
    
Puis notez cet identifiant. Imaginons qu'il s'agisse du PID `12345`. Alors pour produire le heapdump, lancer la commande : 

    kill -USR2 12345
    
Un fichier nommé `heapdump-<id>.heapsnapshot` sera alors créé sur la machine, soit dans votre répertoire HOME, soit dans le répertoire depuis lequel Duniter a été lancé, soit encore à la racine `/` du système.

Ce fichier peut ensuite être exploité dans divers outils comme les [Chrome Dev Tools](https://developer.chrome.com/devtools).
