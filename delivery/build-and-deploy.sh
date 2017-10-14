#!/usr/bin/env bash

echo "Récupération des modifications..."
git stash
git pull origin master

echo "Récupération de la licence..."
if [[ ! -d ./G1 ]]; then
  git clone https://github.com/duniter/G1.git
fi

echo "Copie de la licence..."
cd G1
git pull origin master
cd ..
cp ./G1/license/license_g1-fr-FR.rst content/files/licence_g1.txt

echo "Installation de Pelican"
virtualenv .
source bin/activate
pip install pelican pelican-youtube markdown beautifulsoup4

echo "Prégénération de la licence dans le wiki"
python replace.py

echo "Génération du site"
pelican -s publishconf.py

echo "Copie des fichiers..."
cp -R output/* ../fr/

echo "Génération de duniter.org/fr terminée."
