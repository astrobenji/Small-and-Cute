'''
quotate.py

Takes in: a .txt file

Spits out: a .txt file where every line begins with >, and is <=79 characters long.

Useful for writing rejoinders!

Usage:

python quotate.py -f <filename.txt> > <result.txt>

Created by: Benjamin Metha
Last updated: Jan 22, 2021
'''

import argparse 

parser = argparse.ArgumentParser()

parser.add_argument("-f",
                    "--filename",
                    help="Name of the text file",
                    required=True,
                    type=str,
                    dest='fname',
                    nargs=1)

args = parser.parse_args()

for i in args.fname:
        file = open(i, 'r')
        
lines = file.readlines()
for line in lines: 
    if len(line) < 78:
        print('> ' + line)
        continue
    else:
        words = line.split()
        subline = '>'
        while(words):
            if len(subline) + len(words[0]) < 80:
                subline += ' ' + words.pop(0)
            else:
                print(subline)
                subline = '> ' + words.pop(0)
        print(subline)
        
