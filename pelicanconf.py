# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# À propos de moi
AUTHOR = 'HS-157'
SITENAME = "HS-157.moe moe kyun !"
SITESUBTITLE = "Je suis un chanceux parmi les uns, et un malheureux parmi les autres..."
SITEURL = 'http://hs-157.moe'
TIMEZONE = "Europe/Paris"

# Met les articles dans cette catégorie par défaut
DEFAULT_CATEGORY = 'Mets une catégorie, putain !'

# Gestion des liens
ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_PATHS = ['p']
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'
CATEGORY_URL = 'c/{slug}'
CATEGORY_SAVE_AS = 'c/{slug}/index.html'
TAG_URL = 't/{slug}'
TAG_SAVE_AS = 't/{slug}/index.html'

AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True
WITH_FUTURE_DATES = True
LOAD_CONTENT_CACHE = False

GZIP_CACHE = True

DEFAULT_LANG = "fr"
REVERSE_CATEGORY_ORDER = True
LOCALE = "fr_FR.utf8"
DEFAULT_PAGINATION = 100
DEFAULT_ORPHANS = 10
DEFAULT_DATE = 'fs'
DATE_FORMATS = {'fr': '%d/%m/%y',}

# Gestion des flux rss
FEED_ALL_RSS = 'rss/all.xml'
CATEGORY_FEED_RSS = 'rss/c_%s.xml'
TAG_FEED_RSS = 'rss/t_%s.xml'
FEED_ATOM = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TAG_FEED_ATOM = None

LINKS = (('Benvii', "http://www.benvii.com/"),
         ('Guigui Show', "http://www.guiguishow.info/"),
         ('H2L29', "http://h2l29200.tk/"),
         ('Maison du Libre', "http://mdl29.net/"),
         ('Pelican', "http://blog.getpelican.com/"),)

SOCIAL = (('Twitter', 'http://twitter.com/HS_157'),
          ('Github', 'http://github.com/HS-157'),)

GITHUB_URL = 'http://github.com/hs-157/'

STATIC_PATHS = ['img', 'extra/favicon.ico', 'media']
EXTRA_PATH_METADATA = {
		    'extra/favicon.ico': {'path': 'favicon.con'},
			    }

#THEME_STATIC_DIR = 'Mannitan'
#THEME = 'Mannitan'
