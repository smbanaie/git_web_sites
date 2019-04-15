#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'مجتبی بنائی'
SITENAME = 'وب سایت درس مهندسی نرم\u200cافزار پیشرفته'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Tehran'

DEFAULT_LANG = 'Persian'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DISPLAY_PAGES_ON_HOME = True
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}.html'
CATEGORY_URL = 'category/{slug}/index.html'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}/index.html'
TAG_SAVE_AS = 'tag/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


THEME = 'themes/html5up-editorial'


STATIC_PATHS = ['images']
PLUGINS = ['neighbors']