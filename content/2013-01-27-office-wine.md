date: 2013-01-27
layout: post
title: Installing Office 2010 on Ubuntu using Wine 1.5
description: "Follow WineHQ official page to easily install Microsoft Office 2010 on Wine 1.5.x"
tags: "Ubuntu"
comments: True

I tried various guides on installing Microsoft Office 2010 on Ubuntu using Wine (1.5.22) but none worked. In each case the installer failed the midway. However, since the [official Wine page][official] gives it a rating of Platinum, I finally read through the page and it worked.

Bookmarking the relevant extracts for future.

> Make sure all dependencies of Wine are installed on your system, including winbind.

1. Installed the latest Wine version (1.5.22) using Synaptic. It auto installed wine-mono mentioned in the original article.

2. Installed ttf-mscorefonts (i.e. the windows fonts).

    > Install Office 2010 to a clean wineprefix--no winetricks or other tweaks, and no other applications installed. Do not change the Windows version in winecfg; it should remain at the default setting of XP.

3. Reset WineTricks changes: WineTricks >> Select the default wineprefix >> Delete all data and applications. Start WineTricks again to recreate default prefix.

    > After installing, set riched20 to native, builtin in winecfg to enable Powerpoint to start and selection boxes to display correctly. Do not use winetricks; Office installs its own riched20 to a private directory, and the one installed by winetricks is insufficient.

4. Run winecfg >> Libraries >> add riched20 >> edit to select native.

Have been using the the above for quite some time now. It is very stable and looks even more beautiful than on Windows :).

**[Official Wine Page][official]**

[official]: http://appdb.winehq.org/objectManager.php?sClass=version&iId=17336