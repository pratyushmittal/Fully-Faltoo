date: 2013-07-20
layout: post
title: Fixing Lenovo touchpads on Ubuntu
comments: True
description: Lenovo touchpads are often very jumpy and imprecise on Ubuntu. This configuration fixes it in an easy way.

I recently moved from Dell Studio to Lenovo's Thinkpad Edge E430 laptop. It is an all-Intel machine and thus the drivers support is quite good. Initially the touchpad felt over sensitive as the cursor jumped a few pixels on clicks. Luckily, it is a common [touchpad issue on Lenovo machines][solution] and easily fixable.

Create the following config file in `/usr/share/X11/xorg.conf.d/50-thinkpad-touchpad.conf` (create `xorg.conf.d` directory if it doesn't exist):

    Section "InputClass"
            Identifier "touchpad"
            MatchProduct "SynPS/2 Synaptics TouchPad"
            Driver "synaptics"
            # fix touchpad resolution
            Option "VertResolution" "100"
            Option "HorizResolution" "65"
            # increment noise cancellation factor
            Option "HorizHysteresis" "50"
            Option "VertHysteresis" "50"
    EndSection

Different Lenovo laptops may require different tweaking. Above works best for Edge series. Other configs are available **[here][solution]**.

[solution]: https://bugs.launchpad.net/ubuntu/+source/xserver-xorg-input-synaptics/+bug/1042069

