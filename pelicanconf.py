#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from python_markdown_gh_emoji import GheEmoji

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
AUTHOR = 'Eric Arellano Martinez'
SITENAME = 'Erics Software Blog'
SITEURL = 'blog.ericarellano.tech'
THEME = 'themes/Papyrus'
THEME_STATIC_PATHS = ['static']

PATH = 'content'
LOCALE = 'en_us'

TIMEZONE = 'America/Los_Angeles'
DEFAULT_DATE = 'fs'
DEFAULT_LANG = 'en'
SUBTITLE = 'Terraform, Python, MLOps, Infrastructure as Code'
COPYRIGHT = '©2023'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['readtime', 'search', 'neighbors', 'pelican-toc']

# Site search plugin
SEARCH_MODE = "output"
SEARCH_HTML_SELECTOR = "main"

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
SOCIAL = [('github', 'http://www.github.com/edamsoft-sre'),
          ('twitter', 'http://twitter.com/x'),
          ('linkedin', 'https://www.linkedin.com/in/eric-arellano-martinez/')]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# BlueIdea
GITHUB_URL = 'http://www.github.com/edamsoft-sre'

DISPLAY_PAGES_ON_MENU = True
DIRECT_TEMPLATES = (('index', 'search', 'tags', 'categories', 'archives',))
PAGINATED_TEMPLATES = {'index': None, 'tag': None, 'category': None, 'author': None, 'archives': 24, }

USE_FOLDER_AS_CATEGORY = False

# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

TOC = {
    'TOC_HEADERS': '^h[1-4]',  # What headers should be included in
    # the generated toc
    # Expected format is a regular expression

    'TOC_RUN': 'true',  # Default value for toc generation,
    # if it does not evaluate
    # to 'true' no toc will be generated

    'TOC_INCLUDE_TITLE': 'true',  # If 'true' include title in toc
}

SHARE = (
    ("twitter", "https://twitter.com/intent/tweet/?text=Features&amp;url="),
    ("linkedin", "https://www.linkedin.com/sharing/share-offsite/?url="),
    ("reddit", "https://reddit.com/submit?url="),
    ("facebook", "https://facebook.com/sharer/sharer.php?u="),
    ("whatsapp", "https://api.whatsapp.com/send?text=Features - "),
    ("telegram", "https://telegram.me/share/url?text=Features&amp;url="),
)
INDEX_SAVE_AS='blog/index.html'
