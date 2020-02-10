import sys
import time
import subprocess


def preview():
    "Shows what will be output"
    server = subprocess.Popen(['pelican', 'content', '--listen', '--autoreload'])
    time.sleep(2)
    subprocess.run(['open', 'http://localhost:8000'])
    server.communicate()


def commit():
    "Commit changes"
    run("pelican content -s publishconf.py")
    print('git status')
    print('do you want to continue?')
    run('git add . -A')
    run('git commit -m "Auto commiting changes"')
    run('git push')


if __name__ == "__main__":
    options = {
        'preview': preview,
        'commit': commit,
    }
    name = sys.argv[1]
    func = options[name]
    func()