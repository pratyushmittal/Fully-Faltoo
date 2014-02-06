date: 2012-12-26
layout: post
title: Mount NTFS partition automatically in Ubuntu
description: "Automatically mount NTFS partition in Ubuntu without ntfs-config"
link: http://askubuntu.com/questions/83461/automatically-mount-ntfs-drive-when-i-login
comments: True
slug: mount-ntfs-new
tags: "Ubuntu"

I had [earlier mentioned][old post] about the correct way of mounting NTFS partition using ntfs-config. However, recently I experienced a few crash errors and thus found this method easier to use.

Open Unity (using windows key) and type "Startup Applications"

> Then click on the Add button, Write a name for this operation such as "Mount ntfs drives", then in command input box, write `udisks --mount /dev/sda2`, to automount the ntfs partition.
> 
> **Note: You need to replace the /dev/sda2 with your actual NTFS partition number.**
> 
> You can get this number by `sudo blkid`

Below is the output of this command in my computer.

![Find NTFS partition number](http://fully-faltoo.com/uploads/ntfs-mount.png)

Since I had to mount the partition with the label "Storage", I entered this command:

    udisks --mount /dev/sda4

This auto mounts the partition on start-up with correct user permissions.

[old post]: http://fully-faltoo.com/2012/06/30/mount-ntfs/
