#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# AUTHOR = u'Duniter'
SITENAME = u'Duniter'
SITEURL = u'https://duniter.org/fr'

PATH = 'content'
THEME = "pelican-themes/pelican-bootstrap3"
PAGES_SORT_ATTRIBUTE = 'order'

TIMEZONE = 'Europe/Paris'

# ABOUT_ME = '<div id="stb-container-1313" class="stb-container-css stb-black-container stb-collapsible stb-visible stb-image-big stb-ltr stb-border" style="margin: 10px 0px 10px 0px;"><div id="stb-caption-box-1313" class="stb-black-caption_box stb_caption stb-caption-box"><aside class="stb-caption-icon"><img src="http://www.creationmonetaire.info/wp-content/plugins/wp-special-textboxes/themes/stb-metro/earth.png"></aside><div id="stb-tool-1313" class="stb-tool"><img id="stb-toolimg-1313" src="http://www.creationmonetaire.info/wp-content/plugins/wp-special-textboxes/themes/stb-metro/minus.png" title="Hide"></div>J’accepte les Ğ1 !</div><div id="stb-body-box-1313" class="stb-black-body_box stb_body stb-body-box"><div style="margin-bottom: 15px;padding: 2px 2px; background-color: #e7f3fe;border-left: 6px solid #2196F3; font-size: 80%; color: black;">ID : Galuel<br>Ds1z6Wd8hNTexBoo3LVG2oXLZN4dC9ZWxoWwnDbF1NEW</div><center><a href="http://g1.duniter.org/cesium/#/app/wot/Ds1z6Wd8hNTexBoo3LVG2oXLZN4dC9ZWxoWwnDbF1NEW/Galuel"><img src="http://www.creationmonetaire.info/wp-content/uploads/2017/03/duniter_button.png" width="100"></a></center></div></div>'
FAVICON = 'images/duniter-logo.png'
SITELOGO = 'images/duniter-logo.png'
THUMBNAIL_DEFAULT = '/images/duniter-logo-bw.png'
# BANNER = 'images/duniter-logo.png'
# BANNER_SUBTITLE = 'This is my subtitle'
SITELOGO_SIZE = 36

DEFAULT_LANG = u'fr'

PLUGIN_PATHS = ['pelican-plugins/']
PLUGINS = ['i18n_subsites', 'tipue_search', 'pelican-page-hierarchy']

MARKDOWN = {
  'extension_configs': {
    'markdown.extensions.codehilite': { 'css_class': 'highlight' },
    'markdown.extensions.fenced_code': {},
    'markdown.extensions.extra': {},
    'markdown.extensions.toc': {}
  }
}

PYGMENTS_STYLE = 'default'

PATH_METADATA = 'pages/(?P<path>.*)\..*'

JINJA_EXTENSIONS = ['jinja2.ext.i18n']
I18N_SUBSITES = {
}

ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}.html'
PAGE_URL = 'pages/{slug}'
PAGE_SAVE_AS = 'pages/{slug}.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}.html'

BOOTSTRAP_THEME = 'readable'

DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')

ARTICLE_EXCLUDES = ['files']
STATIC_PATHS = ['images', 'content', 'files', 'files/licence_g1.rst', 'css']
CUSTOM_CSS = 'css/custom.css'


# Blogroll
LINKS = (('duniter.org', 'https://duniter.org/'),
         ('forum.duniter.org', 'https://forum.duniter.org/'),
         ('creationmonetaire.info', 'http://creationmonetaire.info/'),)

# Social widget
ACCEPTED_MENUS = ['comprendre',
         'obtenir-des-g1',
         'contribuer',
         'contact',
         'wiki',
         'a-propos',]

SOCIAL = (('Forum', 'https://forum.duniter.org', 'comment'),
          ('Salon XMPP', 'https://chat.duniter.org', 'comments'),
          ('Bugs', '/fr/wiki/rapporter-un-bug', 'bug'),
          ('Twitter', 'https://twitter.com/duniter'),
          ('GitHub', 'https://github.com/duniter'),
          ('Diaspora', 'https://framasphere.org/people/1949ee70f6bc0134e6b32a0000053625', 'asterisk'),
          ('RSS', '/fr/feeds/all.atom.xml'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

CC_LICENSE = "CC-BY-SA"

DISPLAY_ARTICLE_INFO_ON_INDEX = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
BOOTSTRAP_FLUID = False
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = False
SHOW_DATE_MODIFIED = True

GITHUB_USER = ''
GITHUB_SHOW_USER_LINK = True
GITHUB_SKIP_FORK = False
GITHUB_REPO_COUNT = 2

TWITTER_USERNAME = 'duniter'
