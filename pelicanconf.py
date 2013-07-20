#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Pratyush Mittal'
SITENAME = u'A Fully-Faltoo Blog'
SITEURL = 'http://fully-faltoo.com'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (
    ('Hacker News',
        "To keep updated with the latest tech developments",
        "http://news.ycombinator.com/"),
    ('LifeHacker',
        "Collection of the best life hacks",
        "http://lifehacker.com"),
    ('Screener.in',
        'A Stock Screener and stock analysis tool I am working on',
        'http://www.screener.in'),
    ('WebTrickz',
        "My cousin Mayur's Blog for the best 'web-tricks'",
        'http://www.webtrickz.com'),
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 7

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Blog Specific
TAGLINE = "Pratyush's Diary"
# :Menus
DISPLAY_PAGES_ON_MENU = True
# :Navigation Menu
MENUITEMS = (('@faltoo', 'http://twitter.com/faltoo'),)


# Author
AUTHOR_SAVE_AS = False
ABOUT_AUTHOR = ("My name is Pratyush Mittal. "
                "I am a Chartered Accountant living in Lucknow, India. "
                "I love to create financial web-applications and "
                "write Python programs. "
                "I blog about stocks at "
                "<a href='http://dalal-street.in'>Dalal-Street</a>.")


# Reading Settings
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'


# Screen Readers
FEED_ATOM = None
FEED_RSS = ('feed.rss')
FEED_DOMAIN = ("http://feeds.feedburner.com/fullyfaltoo")
TRANSLATION_FEED = None
CATEGORY_FEED_ATOM = None


# Writing Settings
JINJA_EXTENSIONS = ['pyjade.ext.jinja.PyJadeExtension']
THEME = "theme/faltoo"
STATIC_PATHS = ["uploads", "tumblr_files"]
FILES_TO_COPY = (
    ('root/CNAME', 'CNAME'),
    ('root/favicon.ico', 'favicon.ico'),
)


# Integrations
DISQUS_SITENAME = "fully-faltoo"
GOOGLE_ANALYTICS = "UA-2456523-1"
