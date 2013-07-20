date: 2012-06-30
slug: mount-ntfs
layout: post
title: Auto mount NTFS partitions in Ubuntu in easy correct way
description: Using ntfs-config to auto-edit fstab and then adding Recycle bin fix.
tags: 'Ubuntu', 'ntfs'


Modifying fstab manually has its own fears and thus I like ntfs-config to auto-mount NTFS partitions on Ubuntu. However, recent updates sometimes cause errors while running ntfs-config.

Fix for properly installing ntfs-config [via AskUbuntu][1]:

> Install ntfs-config from the Software Center, then it's just a matter of choosing which drives to mount and if you want to also write to the drives.
> 
> Apparently ntfs-config crashes. To fix that you have to do this:
> 
>       sudo mkdir -p /etc/hal/fdi/policy
>
> If you run ntfs-config, from the terminal you'll get an error about that directory which doesn't exist, so with that command you can create it and the program will work as intended.

Using above method has a defect though. When you delete a file from the mounted partition, it permanently deletes it instead of sending to rubbish-bin/thrash.

To fix above, you need to edit one line in fstab [via UbuntuForums][2]:

    sudo cp /etc/fstab /etc/fstab.bckup
    gksu gedit /etc/fstab

Now replace portion **after** ntfs-3g with:

    defaults,utf8,umask=007,uid=1000,gid=1000   0   1

thus the line may look like:

    UUID=286A0F8071DF401A   /media/Storage  ntfs-3g defaults,utf8,umask=007,uid=1000,gid=1000   0   1

Hope this saves a lot of head-banging in future.
[1]: http://askubuntu.com/questions/83461/automatically-mount-ntfs-drive-when-i-login
[2]: http://ubuntuforums.org/showthread.php?t=1637304
[new post]: http://fully-faltoo.com/2012/12/26/mount-ntfs-new/