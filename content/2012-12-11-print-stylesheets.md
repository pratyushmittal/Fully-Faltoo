date: 2012-12-11
layout: post
title: Controlling the print style-sheets [CSS]
description: Control page breaks and alignment using print stylesheets
tags: "CSS"

There are some very useful CSS2 features which allow the authors to get control on how the pages are printed.

### Avoid the page breaks just after headings

    h1, h2, h3, h4, h5, h6 { page-break-after : avoid }

> page-break-after properties accept the auto, always, avoid, left, and right keywords.
>
> The keyword auto is the default, it lets the browser generate page breaks as needed. The keyword always forces a page break before or after the element, while avoid suppresses a page break immediately before or after the element. The left and right keywords force one or two page breaks, so that the element is rendered on a left-hand or right-hand page.

### Prevent just a line of the paragraph from moving onto next page

    @page {
        orphans:4;
        widows:2;
    }

>The `orphans` property specifies the minimum number of lines of a paragraph that must be left at the bottom of a page.
>
>The `widows` property specifies the minimum number of lines of a paragraph that must be left at the top of a page.

**[TutorialsPoint][] covers many other features for better print pages. Bookmarked it for long!**

[TutorialsPoint]: http://www.tutorialspoint.com/css/css_paged_media.htm