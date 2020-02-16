#!.venv/bin/python
import sys
import os
import subprocess

def copy_to_uploads(filepath):
    filename = os.path.basename(filepath)
    uploads = os.path.join("content", "uploads", filename)
    subprocess.run(["cp", filepath, uploads])
    # copy new path to clipboard
    new_path = f"/uploads/{filename}"
    subprocess.run("pbcopy", universal_newlines=True, input=new_path)


copy_to_uploads(sys.argv[1])
