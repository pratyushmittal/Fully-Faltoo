import os
import sys
import time
import subprocess

CONTENT_FOLDER = "content"
OUTPUT_FOLDER = "output"
PREVIEW_FOLDER = "preview"


def _prepare(command):
    output_folder = OUTPUT_FOLDER if command == 'commit' else PREVIEW_FOLDER

    # Remove output folder
    subprocess.run([
        "rm", "-rf", output_folder
    ])

    # Create random folder in output
    random_folder = os.path.join(output_folder, "random")
    subprocess.run([
        "mkdir", "-p", random_folder
    ])


def preview():
    "Shows what will be output"
    server = subprocess.Popen([
        'pelican', CONTENT_FOLDER,
        '--listen',
        '--autoreload',
        "--output", PREVIEW_FOLDER,
    ])
    time.sleep(2)
    subprocess.run(['open', 'http://localhost:8000'])
    server.communicate()


def commit():
    "Commit changes"
    subprocess.run([
        "pelican", CONTENT_FOLDER,
        "--settings", "publishconf.py",
        "--output", OUTPUT_FOLDER,
    ])

    subprocess.run(["git", "status"])

    ask = input("Do you want to continue? Type 'yo' to continue:")
    if not ask == 'yo':
        exit()

    subprocess.run([
        "git", "add", ".", "-A"
    ])
    subprocess.run([
        "git", "commit", "-m", "Auto committing changes"
    ])
    subprocess.run([
        "git", "push"
    ])


if __name__ == "__main__":
    options = {
        'preview': preview,
        'commit': commit,
    }
    name = sys.argv[1]
    func = options[name]
    _prepare(name)
    func()