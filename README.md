# Duniter website

Public site available at https://duniter.org/fr

## Reproduce it locally

You may want to reproduce this website locally, for developement purposes for example. Here are the instructions.

Clone the sources

    git clone https://github.com/duniter/website_fr.git

Install python stuff

    cd website_fr
    virtualenv .
    source bin/activate
    pip install pelican pelican-youtube markdown beautifulsoup4

Install system dependencies for plantuml plugin (plantuml and GraphViz utilities) :

 * Install plantuml : use your package manager or http://plantuml.com/starting
 * Install GraphViz : use your package manager or http://www.graphviz.org/Download..php

Generate the site

    pelican

Serve it

    ./develop_server.sh start 8556

The website should be available at : http://localhost:8556

## Manage the development server

Parameters available
* default port: 8556
* start <port_number>
* restart <port_number>
* stop

If you want to use an another port number :
1) Edit the ```SITEURL``` variable in ```pelicanconf.py``` file
2) ./develop_server.sh {start|restart} <port_number>

## Generate production site

To permit a nice-looking license inclusion in the wiki, we use a pre-run script that should be ran before creating the site with pelican:


You just need to give the production configuration file to Pelican:

    pelican -s publishconf.py

You may want to change the production parameters, like the domain name: just edit `publishconf.py` and modify the `SITEURL` to whatever value you want.

For example if you want to host the site at `https://my.website.org`, set:

    SITEURL = u'https://my.website.org'

## Plantuml plugin documentation

 * Plantuml plugin documentation : https://github.com/Scheirle/pelican-plugins/tree/master/plantuml
 * Plantuml documentation: http://plantuml.com
 * Plantuml support DOT language of GraphViz: http://www.graphviz.org/Gallery.php
