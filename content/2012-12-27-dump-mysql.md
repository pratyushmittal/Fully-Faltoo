date: 2012-12-27
layout: post
comments: true
title: Dump and restore all MySQL databases in one command
description: Create backups of databases easily in one command or use them to migrate the data to another computer
slug: dump-mysql
tags: "MySQL"

Came across this [wonderful discussion][stackoverflow] on StackOverflow, for dumping all the MySQL databases from command line.

**For dumping:**
    
    mysqldump -u username -p --all-databases > alldbs.sql

**For restoring:**

    mysql -u username -p < alldbs.sql

The advantage is that it is very quick, and you do not lose the user privileges.


[stackoverflow]: http://stackoverflow.com/questions/328922/transfer-mysql-database-to-another-computer/4819610#4819610