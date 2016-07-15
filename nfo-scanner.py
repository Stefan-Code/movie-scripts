#!/usr/bin/env python3
import subprocess
import sys
import os

print('starting... (This may take a while)')

result = subprocess.check_output("find . -type f -iname '*.nfo'", shell=True)
resultfiles = [filename for filename in result.decode('utf-8').split('\n') if filename]
print('found {} nfo files'.format(len(resultfiles)))

badfiles = []
for nfofile in resultfiles:
    with open(nfofile, 'rb') as f:
        content = f.read()
        if not b'tinyMediaManager' in content:
            badfiles.append(nfofile)
print('found {} bad nfo files'.format(len(badfiles)))
print('Do you want to see a list of files? [y/n]')
answer = input()
if answer == 'y':
    print('\n'.join(badfiles))
