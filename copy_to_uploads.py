#!/usr/bin/python3
import sys
import pathlib
import os
import subprocess


def _run(command):
    subprocess.run(command, check=True)


def copy_to_uploads(filepath):
    filename = os.path.basename(filepath)
    uploads = os.path.join(
        "/Users/pratyush/Websites/faltoo", "content", "uploads", filename
    )
    subprocess.run(["cp", filepath, uploads], check=True)
    # copy new path to clipboard
    new_path = f"/uploads/{filename}"
    subprocess.run(
        "pbcopy", universal_newlines=True, input=new_path, check=True
    )


copy_to_uploads(sys.argv[1])
