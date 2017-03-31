# Duniter website

Public site available -- temporarily -- at https://dn2.cgeek.fr/fr. It aims at replacing https://fr.duniter.org.

## Reproduce it locally

You may want to reproduce this website locally, for developement purposes for example. Here are the instructions.

1. Clone the sources

    git clone https://github.com/duniter/website.git
    
2. Install python stuff

    cd website
    virtualenv .
    source bin/activate
    pip install pelican pelican-youtube markdown

3. Generate the site

    pelican

4. Serve it

    ./develop_server.sh restart 8556

The website should be available at http://localhost:8556.