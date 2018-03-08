#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Bianca Ploch'
SITENAME = 'A CS Blog'
SITEURL = ''

SITESUBTITLE = 'A magical \u2728 Pelican theme'
# SITEIMAGE = '/images/profile_cropped.jpg width=200 height=200'
HIDE_AUTHORS = True

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

LOAD_CONTENT_CACHE = False
DELETE_OUTPUT_DIRECTORY = True

ARTICLE_URL = 'posts/{date:%Y}{date:%m}{date:%d}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'themes/pelican-alchemy/alchemy'

# Blogroll
# LINKS = (('About me', '#'),)

# ICONS
ICONS = (
    ('github', 'https://github.com/MissMuffin'),
    ('email', 'bianca.ploch@student.htw-berlin.de'),
    ('linkedin', 'www.linkedin.com/in/bianca-ploch-b739528a'),
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 11

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

#ignore checkpoints created by running jupyter
IGNORE_FILES = ['.ipynb_checkpoints']
