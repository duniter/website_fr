# Duniter website

Public site available at https://duniter.org/fr

## Reproduce it locally

You may want to reproduce this website locally, for developement purposes for example. Here are the instructions.

Clone the sources

    git clone https://github.com/duniter/website.git
    
Install python stuff

    cd website
    virtualenv .
    source bin/activate
    pip install pelican pelican-youtube markdown beautifulsoup4

Generate the site

    pelican

Serve it

    ./develop_server.sh restart 8556

The website should be available at http://localhost:8556.

## Generate production site

You just need to give the production configuration file to Pelican:

    pelican -s publishconf.py

You may want to change the production parameters, like the domain name: just edit `publishconf.py` and modify the `SITEURL` to whatever value you want.

For example if you want to host the site at `https://my.website.org`, set:

    SITEURL = u'https://my.website.org'
