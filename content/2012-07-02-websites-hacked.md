date: 2012-07-02
slug: websites-hacked
layout: post
title: How Labnol might have been hacked
description: Thinking about how Labnol.org was hacked and what we should do to protect ourselves.
tags: "hacking", "blogging", "passwords"
truncate: 100
comments: enabled


<p>It was a sad day today as the most popular Indian tech-blog, around 7 years old one, was hacked. Worst of all, all the content was deleted.</p>

<blockquote class="twitter-tweet"><p>Difficult times. Hackers have deleted all my websites.</p>&mdash; Amit Agarwal (@labnol) <a href="https://twitter.com/labnol/status/219317563564367872" data-datetime="2012-07-01T06:32:36+00:00">July 1, 2012</a></blockquote>
<script src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<p>Amit Agarwal, has been a path setter for many-many bloggers in India today. He is one of my web-super-heroes too. I got inspired from his quality content and his passion to always pursue & develop new ideas.</p>

<p>As all the details are not yet available, I kept wondering about how it might had happened and how we can protect ourselves. <i>I am not a hacker, but I do code web-applications and thus will try to explain how things work. The common hacking tricks are:</i></p>

<p><strong>1. Walking through the door - getting your keys (or passwords):</strong> This is probably the most dangerous as the hacker gets your password. The passwords are stored at two places, one with the user (in his brain) and another at servers of the websites to authenticate the user. Good websites store "hashed" passwords on their servers. "Hashed" means that a user's password is encrypted using an irreversible algorithm.</p>

<p>Thus say your password is: <code>panther</code><br>
then it might be stored in database as <code>b0d86da2d5b3aa15b61df214489f7c12</code> using MD5 encryption.</p>

<p>Even if the hacker gets access to the password through a website’s server (MySQL injection or other ways), the hacker only receives an encryption and not the original plain password. However, though the above is irreversible, what hackers do is they do the encryption of all the dictionary words or the common passwords using above algorithm and then compare the resulting values. For this reason we are recommended not to keep dictionary words as passwords.</p>

<p>If your password is not a dictionary word or other common password, then it is less likely that hacker can get your password through some website’s server (eg. recent LinkedIn or LastPass leaks).</p>

<p>The other trick from the book is brute-attack. What hacker does here is that he tries all the possible combinations as the password to get the access. It is like trying a bunch of keys to get through the door using all possible combinations. Since the possible combinations can be unlimited, thus brute force is also used only for dictionary words or common passwords. Ever wondered why all the banking sites require you to have that extra numerical number and an upper-case letter? Brute-force attack precaution is the reason as it increases the number of combinations possible.</p>

<p>I am sure, Amit must have had strong passwords making both the above unlikely.</p>

<p><strong>2. Wearing a mask - phishing or click-jacking:</strong> Phishing is where the hacker creates a replica of a web-site’s login page, but instead, when a user types the password, it sends the password to the hacker. For this reason, browsers highlight the main domain now days. Best protection is to always look at the url before entering passwords, and preferably to type the url yourself.</p>

<p>Click-jacking is the un-solicited link which shows something and takes somewhere else.</p>
<p>Click-jack Example: <a href="http://www.facebook.com" id="fbtwt">http://www.facebook.com</a></p>

<p>clicking above Facebook link will actually take to twitter.com (even though it shows as facebook.com in the status bar on hovering over the above link). A hacker often sends such click-jack links through emails. The user clicks on the link and lands on the phishing page to enter the password. For this reason, we are advised not to click un-solicited links in the emails.</p>

<p><strong>3. Sea-surfing - CSRF Attacks:</strong> In CSRF attacks, the hacker makes a user perform actions without his knowledge. We have often heard users complaining that they followed someone on Twitter/Facebook without their knowledge, or sent a change password requests without actually doing it. This type of attack is more of a weakness of a web-site than of a user. What happens behind the scenes is say the hacker posts an image somewhere, can be on his blog or some common forum. However, instead of actually putting the url of the image, he puts an un-intended link there. Thus when user opens that page, the browser sends a request to that page to fetch the image, and instead of fetching the image, it performs the action without a users knowledge. Jeff Atwood has <a href="http://www.codinghorror.com/blog/2008/10/preventing-csrf-and-xsrf-attacks.html">explained the concept in detail</a> on his page.</p>

<p>CSRF attacks can be much more frightening than we imagine. I checked through some of the very good web-hosts admin/billing panel and found the vulnerability there. A little technical job and the hacker can make users send a request for adding new email, or theoretically even delete unwanted files, or perform other such actions, without their knowing.</p>

<p>In CSRF attacks, the user’s browser cookies play an important role as the user is supposed to be logged into his account. Thus the protection is to log-out after the work (even if working from your own computer) from data-sensitive websites. While big websites like Facebook or Gmail have much of protection against CSRF, most other common websites are not that well protected. In browser settings, one can check the option to automatically clear cookies on closing the browser.</p>

<p><strong>4. Other ways:</strong> Other ways are mostly about getting access to a users computer. It can be through key-loggers, unsecured public wifi connections or other networking tricks.</p>

<p>Till the time the actual details are available, I assume that it might have been a phishing attack that compromised Amit’s password. As more details about the attack are made available, I will update this post.</p>

<p>I pray for a quick recovery of all his websites. Best of luck Amit!!!</p>

<p><strong>Update:</strong> During a <a href="https://twitter.com/Blogsdna/status/219684771360538624">conversation with BlogsDNA</a> on Twitter, he explained about a PHP exploit which can allow a hacker run shell commands using a PHP script. A good example about such attack is <a href="http://www.unix.com/302239668-post1.html">this script</a>. The only protection is "never to trust a user's entered data." The Murphy's law in general applies with unusual force in the web-world:</p>
<blockquote>Anything that can go wrong, will go wrong.</blockquote>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
<script type="text/javascript">
$('#fbtwt').live("click", function(e) {
    e.preventDefault();
    e.stopPropagation();
    window.location = "https://twitter.com";
    return false;
});
</script>
