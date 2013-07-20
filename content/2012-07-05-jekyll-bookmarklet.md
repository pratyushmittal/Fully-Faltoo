date: 2012-07-05
slug: jekyll-bookmarklet
layout: post
title: Jekyll bookmarklet [AutoKey script]
description: Create Jekyll blog post in one click using auto-key bookmarklet.
comments: true
tags: "Jekyll", "bookmarklet", "autokey"
truncate: 29


Since I have [moved to Jekyll] [1] I have been writing a lot many posts. A major reason is the easy with which I can write the posts now.

I created a small AutoKey script:

    import datetime
    import time
    import sys
    import re

    # EDIT & CUSTOMIZE the following two lines
    location = '/home/pratyush/Websites/pratyushmittal.github.com/'
    text_editor = 'sublime-text-2 -n'


    def to_slug(text):
        new_name = text.lower().replace(' ', '-')
        new_name = re.sub('-+', '-', new_name)
        pattern = re.compile('[^a-z0-9-]+')
        new_name = pattern.sub('', new_name).strip('-')
        return new_name

    keyboard.send_keys("<ctrl>+c")
    text = clipboard.get_selection()
    text = '\n'.join(['> ' + line for line in text.split('\n')])

    keyboard.send_keys("<ctrl>+l")
    time.sleep(1)
    keyboard.send_keys("<ctrl>+c")
    time.sleep(1)
    link = clipboard.get_selection()
    cb, post_title = dialog.input_dialog("New Blog Post", "Content: %s \nLink: %s\nPost Title:" % (text[:140], link))
    if not post_title:
       sys.exit()
    cb, slug_title = dialog.input_dialog("New Blog Post", "Slug Title", '%s' % post_title)
    slug_title = to_slug(slug_title)

    time_stamp = output = system.exec_command("date")
    postname = '%s-%s' % (datetime.datetime.now().strftime("%Y-%m-%d"), slug_title)
    post_url = '%s_posts/%s.md' % (location, postname)
    with open(post_url, 'w') as post:
        content = '---\ndate: %s\nlayout: post\ntitle: %s\ndescription: \nlink: %s\ntags: [""]\n---\n\n%s\n\n' % (time_stamp, post_title, link, text)
        post.write(content)

    system.exec_command("%s %s" % (text_editor, post_url), getOutput=False)

I have set the keyboard shortcut for the above as `<super>+b`. It asks for a title, automatically creates a post in your specified directory and opens it in your favourite text editor.

I know the above is ***not a bookmarklet*** and the title is mis-worded. But after setting up Jekyll, that was the first thing I searched for. It landed me on a [blog-post by Jonathan] [2] who had written a similar script but only for Mac. Using his idea, I wrote the above script for AutoKey which works well on Ubuntu (or any Linux distribution).

There is also a [pure browser-based bookmarklet too] [3], written by Kester. It lets you write the post-content right from the browser.

[1]: http://fully-faltoo.com/2012/06/30/moving-to-jekyll
[2]: http://jonathanbuys.com/04-05-2011/Jekyll_Bookmarklet.html
[3]: http://www.justkez.com/jekyll-post-creator/
