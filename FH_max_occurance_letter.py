#!/usr/bin/python
'''
Write a Python script that takes a file name as its argument.
In that file, find the line that has the maximum number of
occurrences of the letter
'''

import sys

filename= sys.argv[1]
filename="addition.py"
FH=open(filename)
text=FH.read()
lines=text.split("\n")

maxlist=list()
for line in lines:
    count=line.count("e")
    maxlist.append(count)
index=maxlist.index(max(maxlist))

print(lines[index],": This has max occurences of 'e'")


