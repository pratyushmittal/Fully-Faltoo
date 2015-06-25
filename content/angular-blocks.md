Title: AngularJS - Adding content outside ng-view
Date: 2015-06-25
layout: post
comments: true


One of the common problem patterns in AngularJS is adding content outside the `ng-view`,
such as having context specific sidebars or toolbars.

I liked the solution of [Martin Atkins][martin]. He suggests using `block` like placeholders
for specifying insertions. This is my implementation based on it.

<script src="https://gist.github.com/pratyushmittal/92d1c5ca8f012cff074a.js"></script>

Complete implementation demo: [http://plnkr.co/edit/w0B0hK?p=preview][plnkr]

[martin]: http://apparently.me.uk/angularjs-view-specific-sidebars/
[plnkr]: http://plnkr.co/edit/w0B0hK?p=preview
