#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import os
import requests

if __name__ not in ("__main__", "ppsupdater"):
    print("The updater should only be run by PyPerfScore as ppsupdater!")
    exit("updater_ran_wrongly")

try:
    with open("lang/preferred.ppslng") as langfile:
        langfile_contents = eval(langfile.read())
        strings = langfile_contents[10]
        could_not_import_ver = langfile_contents[2]
        del langfile_contents
except Exception as e:
    print("Error: could not import language into ppsupdater! ({}: {error_message})".format(type(e).__name__, error_message=e))
    exit("failed_to_import_language")

from sys import argv
args = argv.copy()
del argv

def argument(argument_to_search_for):
    if not argument_to_search_for in args:
        for arg in args:
            if arg[0:len(argument_to_search_for)+1] == argument_to_search_for+"=":
                return arg.split("=", 1)[1]
        return False
    else:
        return True

try:
    with open("ver") as version_file:
        version = version_file.read().strip()
except OSError:
    print(could_not_import_ver)
    version = "0.0.0"

base_path_remote = "https://raw.githubusercontent.com/Stehlampe2020/PyPerfScore/{release}/" # The remote base path. → "{}some_file".format(base_path_remote)
base_path_local = "./" # The local base path. "./" refers to the current working directory. Later I will make a detector for the absolute path. → "{}some_file".format(base_path_local)

requested_ver = argument("--ver")
requested_path = argument("--path")

if requested_ver:
    if requests.get(base_path_remote.format(release=str(requested_ver))+"files.list").status_code == 200:
        base_path_remote = base_path_remote.format(release=requested_ver)
    else:
        print(strings[5].format(release=requested_ver))
        if argument("--exit"):
            exit()
        base_path_remote = base_path_remote.format(release="main")
else:
    base_path_remote = base_path_remote.format(release="main")

if requested_path:
    if not requested_path[-1] == "/":
        requested_path += "/"
    if os.path.isdir(requested_path):
        try:
            os.mkdir("".join([requested_path, "lang"]))
        except FileExistsError:
            pass # If the directory already exists, just go on.
        base_path_local = requested_path
        version = "--path" # Tell the program that it's not installed yet where --path specifies it. This works by changing the version string to one that's definetly not the target version!

try:
    latest_ver = requests.get("{}ver".format(base_path_remote)).text.strip()
except ConnectionError as e:
    print(strings["conn_error"].format(strings["dl_types"][0], e))
    
if version != latest_ver:
    print(strings[1].format(ver_old=version, ver_new=latest_ver)) # Notify the user that a newer version is available.

    # Check for files to be downloaded:
    files_to_download = requests.get("{}files.list".format(base_path_remote)).text.strip().split("\n")
    prev_filename = None
    for filename in files_to_download:
        filename = filename.split("#")[0].strip() # This line removes possible comments from the file list by just taking everything before the first hashmark.
        if filename[-1] == "/":
            try:
                os.mkdir(filename) # If there's a directory in files.list (recognizable by the / at the end of the name): create it if it doesn't exist yet.
            except FileExistsError:
                pass
        if "→" in filename:
            name, target = filename.split("→", 1) # The 1 is just there to make sure that the filename string isn't split on more than one location.
            try:
                os.symlink(target, base_path_local+name) # Create links specified in files.list if they're not existing yet.
            except FileExistsError:
                pass
        if not "→" in filename and not filename[-1] == "/":
            with open("".join([base_path_local, filename]), "w") as file: # open the full local path.
                if prev_filename:
                    print(strings[3].format(round((files_to_download.index(filename) / 100) / (len(files_to_download) / 100) * 100, 1), filename + len(prev_filename)*" "), end="\r") # The length of the previous file name is important to make the output nicer, with no stray characters at the end of the line.
                else:
                    print(strings[3].format(0.0, filename), end="\r")
                file.write(requests.get("".join([base_path_remote, filename])).text)
            prev_filename = filename
    print(strings[3].format(100.0, strings[4]))
    
    os.chmod("".join([base_path_local, "ppsupdater.py"]), 0o775) # Make `ppsupdater.py` executable.
    os.chmod("".join([base_path_local, "PyPerfScore.py"]), 0o775) # Make `PyPerfScore.py` executable.
    
    raise SystemExit(strings[0]) # Notify the user that a restart of PyPerfScore is necessary and then quit.
else:
    print(strings[2]) # Notify the user that they use the newest version.
