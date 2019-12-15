#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Pratyush Mittal'
SITENAME = 'Blog of Faltoo Things'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    (
        'Screener.in',
        'This is where I spend most of my time',
        'https://www.screener.in'
    ), (
        'Pinboard',
        'What I am reading?',
        'https://pinboard.in/u:pratyush',
    ), (
        'StackOverflow',
        'Questions and answers',
        'https://stackoverflow.com/users/232649/pratyush',
    ), (
        'Twitter',
        'This is where I follow my heroes',
        'https://twitter.com/faltoo',
    ),
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# OWN SETTINGS FROM HERE
# Options are given here: http://docs.getpelican.com/en/stable/settings.html

# Sitemap
PLUGINS_PATHS = ["pelican-plugins"]
PLUGINS = ['sitemap', 'random_article', ]
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Reading Settings
TYPOGRIFY = True
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)
CATEGORY_SAVE_AS = False
CATEGORIES_SAVE_AS = False
TAG_SAVE_AS = False
TAGS_SAVE_AS = False
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'
RANDOM = 'random/index.html'

# Writing Settings
THEME = "theme/faltoo"
READERS = {'html': None, 'rst': None}
PATH = "content"
STATIC_PATHS = ["uploads", "tumblr_files", "root", ]
EXTRA_PATH_METADATA = {
    'root/CNAME': {'path': 'CNAME'},
    'root/google726cfb66a8285a50.html': {'path': 'google726cfb66a8285a50.html'},
    'root/favicon.ico': {'path': 'favicon.ico'},
}
