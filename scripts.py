import os
import re
import sys
import time
import subprocess
import datetime as dt

CONTENT_FOLDER = "content"
OUTPUT_FOLDER = "docs"
PREVIEW_FOLDER = "preview"


def _prepare(command):
    output_folder = OUTPUT_FOLDER if command == "commit" else PREVIEW_FOLDER

    # Remove output folder
    subprocess.run(["rm", "-rf", output_folder])

    # Create random folder in output
    random_folder = os.path.join(output_folder, "random")
    subprocess.run(["mkdir", "-p", random_folder])

    # copy CNAME file
    # CNAME file must be in root of output folder
    cname_path = os.path.join(output_folder, "CNAME")
    subprocess.run(["cp", "CNAME", cname_path])


def preview():
    "Shows what will be output"
    server = subprocess.Popen(
        [
            "pelican",
            CONTENT_FOLDER,
            "--listen",
            "--autoreload",
            "--output",
            PREVIEW_FOLDER,
        ]
    )
    time.sleep(2)
    subprocess.run(["open", "http://localhost:8000"])
    server.communicate()


def commit():
    "Commit changes"
    subprocess.run(
        [
            "pelican",
            CONTENT_FOLDER,
            "--settings",
            "publishconf.py",
            "--output",
            OUTPUT_FOLDER,
        ]
    )

    subprocess.run(["git", "status"])

    ask = input("Do you want to continue? Type 'yo' to continue:")
    if not ask == "yo":
        exit()

    subprocess.run(["git", "add", ".", "-A"])
    subprocess.run(["git", "commit", "-m", "Auto committing changes"])
    subprocess.run(["git", "push"])


def _to_slug(title):
    slug = re.sub("[^a-z]+", "-", title.lower())
    slug = slug.strip("-")
    return slug


def new_post():
    slug = sys.argv[2] or input("Slug: ")
    slug = _to_slug(slug)
    date = dt.date.today()
    filename = f"{date}-{slug}.md"
    filepath = os.path.join("content", filename)
    content = [
        f"title: {slug}",
        f"date: {date}",
        f"status: draft",
        "",
        "",
        "[in what capacity]",
        "[in what style]",
        "[how much are you going to cover]",
        "[what is one take away from it]",
    ]
    content = "\n".join(content)
    if not os.path.isfile(filepath):
        with open(filepath, "w") as f:
            f.write(content)
    subprocess.run(["/usr/local/bin/code", filepath])


if __name__ == "__main__":
    options = {
        "preview": preview,
        "commit": commit,
        "new-post": new_post,
        "new_post": new_post,
        "new": new_post,
    }
    name = sys.argv[1]
    func = options[name]
    _prepare(name)
    func()
