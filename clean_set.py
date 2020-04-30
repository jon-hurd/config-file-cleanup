# simple (poorly written) but effective scipt for cleaning up PA config files that have extra CR's / LR's when copied from the CLI
# the correct way to save configs from the PA CLI without extra CR's is with the "set cli terminal width 500" command
# this assumes commands begin with "set"
# name your orginal config "org_config.txt" or rename below
# this will print to screen, pipe to a file like this to save: python3 clean_set.py > cleaned_config.txt

import re

f = open("org_config.txt", "r")
for x in f:
    if re.search(r'^set', x):
        part1 = x.rstrip()
        print(f'{part1}')
    else: 
        part2 = x.rstrip()
        print(f'{part1}{part2}')
f.close() 

