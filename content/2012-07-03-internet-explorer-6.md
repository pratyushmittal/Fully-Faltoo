date: 2012-07-03
slug: internet-explorer-6
layout: post
title: Dealing with Internet Explorer 6 issues
description: Best way to deal with Internet Explorer 6 users. Either to display warnings, block them or just do nothing
tags: "Internet Explorer", "web-designing"
truncate: 100


I have often spent hours trying to fix the interface for Internet Explorer users. Most of the time, it isn't worth it. A wonderful question was asked on StackExchange as to [what to do with the Internet Explorer 6 users] [1] - to block them or to warn them. The answer that I liked the most was to do neither, as **“IE6 users probably don't care about poorly rendered pages anyway since they are used to it.”**

> At my company, we neither display a warning nor a blocking message. We make the site usable in IE6, and that's enough. There's no need to wave your hands in the air and say "sorry, we don't have the time to make our site look pretty in your browser". IE6 users probably don't care about poorly rendered pages anyway since they are used to it - every other page they land on will look bad compared to how a modern browser would render the page.
> 
> 99% of the time, IE6 has problems with visuals, not functionality. We use the Prototype Javascript Framework to fix all the cross-browser functional incompatibilities. There doesn't exist an analogous CSS framework to fix all the visual incompatabilities, so we often find IE6 displaying something differently. A button may be 5 pixels shorter or a corner isn't rounded, for example. Our philosophy is to let these visual differences slide because websites are made for people to complete tasks, not gawk at pretty interface design. All the usability experts will attest that ugly design does not hamper usability.

With other major web-sites, including YouTube, Wordpress, Facebook...already showing upgrade messages, it looks like the best advice to follow.

Read the [complete discussion at StackExchange] [1] for other approaches too.

[1]: http://ux.stackexchange.com/questions/5296/blocking-ie6-deny-outright-or-warn-of-issues
