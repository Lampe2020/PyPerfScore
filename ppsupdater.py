#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import os
import requests

if __name__ not in ('__main__', 'ppsupdater'):
    print('The updater should only be run by PyPerfScore as ppsupdater!')
    exit('updater_ran_wrongly')

try:
    with open('lang/preferred.ppslng') as langfile:
        langfile_contents = eval(langfile.read())
        strings = langfile_contents[10]
        could_not_import_ver = langfile_contents[2]
        del langfile_contents
except Exception as e:
    print(f'Error: could not import language into ppsupdater! ({type(e).__name__}: {e})')
    exit('failed_to_import_language')

from sys import argv
args = argv.copy()
del argv

def argument(argument_to_search_for):
    if not argument_to_search_for in args:
        for arg in args:
            if arg[0:len(argument_to_search_for)+1] == argument_to_search_for+'=':
                return arg.split('=', 1)[1]
        return False
    else:
        return True

try:
    with open('ver') as version_file:
        ver_strings = version_file.read().strip()
        if len(ver_strings) > 5:
            ver_strings = eval(ver_strings)
        else:
            ver_strings = {'number': ver_strings, 'type': None, 'nickname': None}
    if argument('--link-in-PATH'):
        ver_strings['number'] = '--link-in-PATH'
except OSError:
    print(could_not_import_ver)
    ver_strings = {'number': '0.0.0'}
    ver_strings['type'] = 'vnotfound'
    ver_strings['nickname'] = None

base_path_remote = 'https://raw.githubusercontent.com/Stehlampe2020/PyPerfScore/{release}/' # The remote base path. → f'{base_path_remote}some_file'
base_path_local = './' # The local base path. './' refers to the current working directory. Later I will make a detector for the absolute path. → f'{base_path_local}some_file'

requested_ver = argument('--ver')
requested_path = argument('--path')

if argument('--link-in-PATH'):
    requested_path = '/usr/share/PyPerfScore/'

if requested_ver:
    if requested_ver in ('latest-stable', 'stable'):
        vstrings = requests.get(''.join([base_path_remote.format(release='main'), 'versions.list']))
        if not vstrings:
            print(strings[6])
            exit('could_not_get_ver_strings')
        else:
            requested_ver = eval(vstrings.text)['latest-stable']
    elif requested_ver == 'latest':
        requested_ver = 'main'
    if requests.get(base_path_remote.format(release=str(requested_ver))+'files.list'):
        base_path_remote = base_path_remote.format(release=requested_ver)
    else:
        print(strings[5].format(release=requested_ver))
        if argument('--exit'):
            exit()
        base_path_remote = base_path_remote.format(release='main')
else:
    base_path_remote = base_path_remote.format(release='main')

if requested_path:
    if not requested_path[-1] == '/':
        requested_path += '/'
    if not os.path.isdir(requested_path):
        try:
            os.mkdir(requested_path)
        except FileExistsError:
            pass # If the directory already exists, just go on.
    base_path_local = requested_path
    ver_strings['number'] = '--path' # Tell the program that it's not installed yet where --path specifies it. This works by changing the version string to one that's definetly not the target version!

try:
    latest_ver = requests.get(f'{base_path_remote}ver').text.strip()
    if len(latest_ver) > 5:
        latest_ver = eval(latest_ver)['number']
except ConnectionError as e:
    print(strings['conn_error'].format(strings['dl_types'][0], e))
    exit()
    
if ver_strings['number'] != latest_ver:
    print(strings[1].format(ver_old=ver_strings['number'], ver_new=latest_ver)) # Notify the user that a newer version is available.

    # Check for files to be downloaded:
    files_to_download = requests.get(f'{base_path_remote}files.list').text.strip().split('\n')
    prev_filename = None
    for filename in files_to_download:
        filename = filename.split('#')[0].strip() # This line removes possible comments from the file list by just taking everything before the first hashmark.
        if filename[-1] == '/':
            try:
                os.mkdir(''.join([base_path_local, filename])) # If there's a directory in files.list (recognizable by the / at the end of the name): create it if it doesn't exist yet.
            except FileExistsError:
                pass
        if '→' in filename:
            name, target = filename.split('→', 1) # The 1 is just there to make sure that the filename string isn't split on more than one location.
            try:
                os.symlink(target, base_path_local+name) # Create links specified in files.list if they're not existing yet.
            except FileExistsError:
                pass
        if not '→' in filename and not filename[-1] == '/':
            with open(''.join([base_path_local, filename]), 'w') as file: # open the full local path.
                if prev_filename:
                    print(strings[3].format(round((files_to_download.index(filename) / 100) / (len(files_to_download) / 100) * 100, 1), filename + len(prev_filename)*' '), end='\r') # The length of the previous file name is important to make the output nicer, with no stray characters at the end of the line.
                else:
                    print(strings[3].format(0.0, filename), end='\r')
                file.write(requests.get(''.join([base_path_remote, filename])).text)
            prev_filename = filename
    print(strings[3].format(100.0, strings[4]))
    
    os.chmod(''.join([base_path_local, 'ppsupdater.py']), 0o775) # Make `ppsupdater.py` executable.
    os.chmod(''.join([base_path_local, 'PyPerfScore.py']), 0o775) # Make `PyPerfScore.py` executable.
    
    if argument('--link-in-PATH'):
        print('Creating commands...')
        for filename, target in ('pyperfscore', 'PyPerfScore.py'), ('ppsupdater', 'ppsupdater.py'):
            try:
                with open(f'/bin/{filename} --link-in-PATH', 'w') as ppsfile:
                    ppsfile.write("""#!/bin/bash
    {}{} --link-in-path $@""".format(base_path_local, target))
                    os.chmod('/bin/{}'.format(filename), 0o775)
            except Exception as e:
                print(': '.join([type(e).__name__, str(e)]))
    
    raise SystemExit(strings[0]) # Notify the user that a restart of PyPerfScore is necessary and then quit.
else:
    print(strings[2]) # Notify the user that they use the newest version.
