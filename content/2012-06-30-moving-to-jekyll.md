date: 2012-06-30
slug: moving-to-jekyll
layout: post
title: Moving to Jekyll
description: Migrating blog from Tumblr to Jekyll
tags: "blogging", "tumblr", "Jekyll", "GitHub"


Fully-Faltoo blog is now hosted on GitHub using Jekyll engine. Primary difference between traditional web-blogs (Wordpress, Tumblr or any other) and Jekyll is that Jekyll web-blog is a static blog. While in other engines, the page is generated dynamically on each request, Jekyll pages are pre-saved as HTML.


**Why I love it?**

Cause it gives all the customization in a very easy (hackable) way. I can use my favourite text-editor to write posts, I can use mark-down and using custom scripts I can publish posts in seconds.

Another major advantage is that it is YAML based. It does not use any database and thus you can add new fields on the fly.


**Migration guides**

- [Jekyll Bootstrap guide] [1] was a perfect guide to set-up the blog.
- Jekyll comes preloaded with [migrations scripts] [2] to import data from all the major blog engines. I used it to migrate my data from Tumblr to Jekyll.
- Then I used a quick Python script to add missing post-titles as Tumblr didn't provide titles for all the fields.
- Customized the theme.
- Pushed GIT.

**So you can expect lots of geeky posts in the upcoming weeks.** Stay tuned for updates.


[1]: http://jekyllbootstrap.com/usage/jekyll-quick-start.html
[2]: https://github.com/mojombo/jekyll/wiki/Blog-Migrations
