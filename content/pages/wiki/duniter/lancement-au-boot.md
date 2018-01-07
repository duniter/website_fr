Title: Lancement au démarrage de la machine
Order: 9
Date: 2018-01-07
Slug: commandes
Authors: vit

Scripts de lancement au démarrage de la machine.

## Systemd

### Version simple

*Testée sur Lubuntu 16.04 32bits.*

Cette version est destinée à une installation manuelle d'après les sources Duniter.
Avec nodejs installé et géré par NVM.

Créer un fichier de service pour systemd :

    sudo nano /etc/systemd/system/duniter-g1-test.service

Et y mettre le script suivant :

    [Unit]
    Description=Duniter g1-test node
    After=network.target

    [Service]
    # Should be set to web in order to start with web GUI
    Environment="DUNITER_WEB=web"
    # Config path
    Environment="DUNITER_HOME=/home/your_user/.config/duniter"
    # Database name
    Environment="DUNITER_DATA=duniter_default"

    # If using a key file, DUNITER_OPTS can be defined like so:
    #Environment="DUNITER_OPTS=--keyfile /etc/duniter/keys.yml"
    Environment="DUNITER_OPTS="

    # NVM and NODEJS
    Environment=NODE_VERSION=6
    Environment=NODE_ENV=production
    Environment=PATH=/home/your_user/.nvm/versions/node/v6.11.4/bin

    Group=your_group
    User=your_user
    Type=forking

    # Duniter install path
    WorkingDirectory=/home/your_user/Logiciels/duniter-g1-test

    # Commands
    ExecStart=/home/your_user/Logiciels/duniter-g1-test/bin/duniter ${DUNITER_WEB}start --home ${DUNITER_HOME} --mdb ${DUNITER_DATA} $DUNITER_OPTS
    ExecReload=/home/your_user/Logiciels/duniter-g1-test/bin/duniter ${DUNITER_WEB}restart --home ${DUNITER_HOME} --mdb ${DUNITER_DATA} $DUNITER_OPTS
    ExecStop=/home/your_user/Logiciels/duniter-g1-test/bin/duniter stop --home ${DUNITER_HOME} --mdb ${DUNITER_DATA}
    Restart=on-failure

    [Install]
    WantedBy=multi-user.target

Remplacer `your_group` et `your_user` par l'utilisateur et le groupe qui lance le processus.
Adapter les chemins selon votre installation.

A chaque modification du fichier, vous devez avertir systemd avec cette commande :

    sudo systemctl daemon-reload

Tester le lancement du service :

    sudo systemctl start duniter-g1-test.service

Stopper le service :

    sudo systemctl stop duniter-g1-test.service

Activer le lancement du service au démarrage de la machine :

    sudo systemctl enable duniter-g1-test.service

Redémarrer la machine pour vérifier que Duniter se lance correctement.

En cas de problème, vérifier les logs de Duniter et ceux de systemd :

    journalctl -xe

### Version avec scripts shell

[Version avec gestion plus avancée de NVM](https://diaspora-fr.org/posts/2703333)
