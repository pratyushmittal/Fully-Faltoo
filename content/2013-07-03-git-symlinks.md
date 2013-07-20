date: 2013-07-06
layout: post
title: Relative symlinks in Git using subtree
description: Git does not follow the symlinks. Thus we use sub-trees to share common directories between projects.
tags: 'git','python','subtree'
code: true
comments: true


I have two separate projects and both use a common set of directories. Since both the projects are under active development, I symlinked the common files. Thus the changes were incorporated in both the projects. **However, git *does not* follow the symbolic links and instead saves its contents.**

To solve it I:

1. Copied one of the projects into the another as a subdirectory using subtree.
2. Created symlinks from inside this subtree directory.
3. Changed the absolute paths of symbolic links into relative paths.
4. Automated all of the above into a script.

## Detailed steps

**Step 1:** Subtree is useful (and better than submodule) for including a project into another project as a subdirectory. The main advantage is that the changes are both downstream as well as upstream. I followed [this post][tutorial] to include the project as subtree sub-directory.

**Step 2:** Next step was to convert all the old symlinks (directly from main project) to symlinks from the new subtree directory. To find all the symbolic links in a directory use `$ find /path -type l`.

**Step 3:** The symlinks created usually contain absolute file paths (even though they might be in the same git project). Use the [symlinks utility][symlinks] to convert all the symlinks from absolute paths to relative paths.

    :::bash
    $ sudo apt-get install symlinks
    $ symlinks -tscr .  # Preview changes
    $ symlinks -scr .   # Execute changes

**Step 4:** To automate all of the above, I compiled and saved the above commands in a fab file to run while committing the changes.

    :::python
    def sync_down():
        """Syncs downstream from remote to local branch"""
        local("git checkout remote_branch")
        local("git pull")
        local("git checkout master")
        local('git merge --squash -s subtree '
              '--no-commit '
              'remote_branch')
    
    
    def sync_up():
        """Syncs upstream from local to remote branch"""
        local("git checkout remote_branch")
        local('git merge --squash -s subtree '
              '--no-commit '
              'master')
        local('git add . -A')
        local('git commit -m "Merged changes from remote"')
        local("git push remote remote_branch:master")
        local("git checkout master")


    def sync_all():
        local("symlinks -scr .")
        sync_down()
        sync_up()


I agree that this is a very hacky way to achieve a simple following of symlinks. However, all the [other][stack1] [workarounds][stack2] looked as bad. 


[symlinks]: http://bashscripts.org/forum/viewtopic.php?f=8&t=457
[tutorial]: http://www.codeproject.com/Articles/562950/GitplusSubtreeplusMergeplus-e2-80-93TheplusQuickpl
[stack1]: http://stackoverflow.com/questions/86402/how-can-i-get-git-to-follow-symlinks
[stack2]: http://stackoverflow.com/questions/1500772/getting-git-to-follow-symlinks-again
