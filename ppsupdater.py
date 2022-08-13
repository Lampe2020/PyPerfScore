import requests

if __name__ == "__main__":
    print("Please don't run the updater seperately, use `pyperfscore --update` for that!")
    exit("updater_ran_seperately")
elif __name__ != "ppsupdater":
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

try:
    with open("ver") as version_file:
        version = version_file.read().strip()
except OSError:
    print(could_not_import_ver)
    version = "0.0.0"

base_path_remote = "https://github.com/Stehlampe2020/PyPerfScore/raw/main/" # The remote base path. → "{}some_file".format(base_path_remote)
base_path_local = "./" # The local base path. "./" refers to the current working directory. Later I will make a detector for the absolute path. → "{}some_file".format(base_path_local)

try:
    latest_ver = requests.get("{}ver".format(base_path_remote)).text.strip()
except ConnectionError as e:
    print(strings["conn_error"].format(strings["dl_types"][0], e))
    
if version != latest_ver:
    print(strings[1].format(ver_old=version, ver_new=latest_ver)) # Notify the user that a newer version is available.
    
    # Check for files to be downloaded:
    files_to_download = requests.get("{}files.list".format(base_path_remote)).text.strip().split("\n")
    for filename in files_to_download:
        with open("".join([base_path_local, filename]), "w") as file:
            print(strings[3].format(filename))
            file.write(requests.get("".join([base_path_remote, filename])).text)
    
    raise SystemExit(strings[0]) # Notify the user that a restart of PyPerfScore is necessary and then quit.
else:
    print(strings[2]) # Notify the user that they use the newest version.
