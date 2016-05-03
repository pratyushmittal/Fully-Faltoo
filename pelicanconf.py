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
RELATIVE_URLS = False


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

# Sitemap
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


# Screen Readers
FEED_ATOM = None
FEED_RSS = ('feed.rss')
FEED_DOMAIN = ("http://feeds.feedburner.com/fullyfaltoo")
TRANSLATION_FEED = None
CATEGORY_FEED_ATOM = None


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


# Integrations
DISQUS_SITENAME = "fully-faltoo"
GOOGLE_ANALYTICS = "UA-2456523-1"
