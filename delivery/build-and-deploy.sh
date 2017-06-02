#!/usr/bin/env bash

echo "Récupération des modifications..."
git pull origin master

echo "Installation de Pelican"
virtualenv .
source bin/activate
pip install pelican pelican-youtube markdown beautifulsoup4

echo "Génération du site"
pelican -s publishconf.py

echo "Copie des fichiers..."
cp -R output/* ../fr/

echo "Génération de duniter.org/fr terminée."
