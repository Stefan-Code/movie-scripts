#!/usr/bin/env python3
import subprocess
import sys
import os

def touch(directory, file='.nomedia'):
    filepath = os.path.join(directory, file)
    #print('touching file', filepath)
    subprocess.call(['touch', filepath])

result = subprocess.check_output("find . -type d -iname '*extra*' | sed '/extrafanart/d' | xargs -0 echo", shell=True)
resultdirs = [dirname for dirname in result.decode('utf-8').split('\n') if dirname]

print(len(resultdirs), 'items in queue')
print('Press [q] to exit anytime')

# loop over the matched directories
for dirname in resultdirs:
    # dont ask if a .nomedia file already exists
    if os.path.isfile(os.path.join(dirname, '.nomedia')):
        #print(dirname, 'already has a .nomedia file, skipping.')
        continue
    print('do you want to place a nomedia file in:')
    print(dirname)
    print('y or n ?')
    answer = input()
    if answer == 'y':
        print('placing .nomedia')
        touch(dirname)
    elif answer == 'q':
        print('Farewell!')
        sys.exit(1)
    else:
        print('no file will be placed')
    print()  # newline so it looks nice
