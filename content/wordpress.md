Title: Visiting China - Tips
Date: 2015-04-15
Slug: multiple-wordpress
Status: draft
comments: true

I recently migrated all my Wordpress
installations spread across different web-hosts
to a single DigitalOcean server. This is a
brief step-by-step checklist for the reference purpose.


1. **Setup a LAMP stack**: [Follow this guide][do]
   for setting up mysql and apache configurations.
   [Mirror link][mirror].

2. **Take a backup of uploads on source server**:

   # cd into wp-content folder or source server
   zip -ruq uploads.zip uploads/
   mv uploads.zip uploads/

3. **Downloading media files**:

    # cd into wp-content folder on destination server
    wget http://website.com/wp-content/uploads/uploads.zip
    rm uploads
    unzip uploads.zip

4. Enable mod-rewrite
5. Update hosts
6. Import export
7. change dns
8. plugins, disqus
9. Settings -> Permalinks
10. Appearance


^1: I have a few Wordpress blogs at blog.screener.in,
dalal-street.in and a couple of others for
friends.

[do]: https://www.digitalocean.com/community/tutorials/how-to-set-up-multiple-wordpress-sites-on-a-single-ubuntu-vps
[mirror]: https://archive.today/GiU6l
