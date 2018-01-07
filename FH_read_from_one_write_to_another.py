#!/usr/bin/python
'''Write a Python script that takes a file name as its argument.
Write the contents of this file to another file such that,
each sentence is stored on a new line.'''

import sys

filename=sys.argv[1]

FH=open(filename)
all_lines=FH.read()
lines=all_lines.split(".")

FHN=open("newfile",'w+')

for line in lines:
    FHN.write(line+"\n")

