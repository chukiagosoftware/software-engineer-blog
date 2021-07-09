#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from ghe_emoji import GheEmoji

MARKDOWN = {
    'extensions': [GheEmoji.load_from_github()],
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.toc': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}
AUTHOR = 'Eric Arellano'
SITENAME = 'Software Engineering Blog'
SITEURL = 'www.ericarellano.tech'
THEME = 'themes/pelican-blueidea'
PATH = 'content'
LOCALE = 'en_us'

TIMEZONE = 'America/New_York'
DEFAULT_DATE = 'fs'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Links
LINKS = (('Pagina Siete', 'http://www.paginasiete.bo'),
         ('Fundación Solón', 'https://www.fundacionsolon.org'),
         ('Rimay Pampa', 'http://www.rimaypampa.org')
         )

# Social widget
SOCIAL = [('Github', 'http://www.github.com/edam-software')]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# BlueIdea
GITHUB_URL='http://www.github.com/edam-software'

DISPLAY_PAGES_ON_MENU = True

USE_FOLDER_AS_CATEGORY = False

PLUGINS = [
    'pelican_youtube'
]

# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    }