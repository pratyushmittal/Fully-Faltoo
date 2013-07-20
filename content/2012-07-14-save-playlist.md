date: 2012-07-14
slug: save-playlist
layout: post
title: Export or save songs from a playlist (Linux)
description: Save or export songs from a playlist of any media player including Rhythmbox
tags: "Ubuntu", "Terminal", "Rhythmbox"
comment: True


I often need to export a playlist items for saving them in a USB or just in a folder. [Found this useful one line command][1] for Terminal which exports or saves a play-list items as files.

> Export your playlist to a m3u file. I called it playlist.m3u  
> Open a terminal in the folder where you have saved the file.
> 
> Copy & paste this:  
> `sed "s/#.*//g" < playlist.m3u | sed "/^$/d" | while read line; do cp "${line}" '/path/to/output/folder/'; done`
> 
> Remember to change the path to your desired output folder.  
> Note: Terminal will not give any output whilst files are copied, just be patient ;)

[1]: http://askubuntu.com/questions/43643/how-can-i-export-all-the-mp3s-from-a-playlist-in-banshee
