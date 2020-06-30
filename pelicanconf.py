#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

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

# Blogroll
LINKS = (('Pagina Siete (Bolivia)', 'http://www.paginasiete.bo'),
         ('Fundación Solón', 'https://www.fundacionsolon.org'),
         ('Rimay Pampa', 'http://www.rimaypampa.com'))

# Social widget
SOCIAL = [('Github', 'http://www.github.com/ericdanielarellano')]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# BlueIdea

GITHUB_URL='http://www.github.com/ericdanielarellano'

DISPLAY_PAGES_ON_MENU = True

USE_FOLDER_AS_CATEGORY = False
