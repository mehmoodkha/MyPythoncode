#!/usr/bin/python

'''Program to take file as input and work on it
Get the name of the text file from the user.
Check if all the sentences in that text file begin with a capital letter.
'''

file_name=input("Enter file name: ")

FH=open(file_name)
complete_text=FH.read()
all_sentences=complete_text.split(".")
small=0
caps=0
for sentence in all_sentences:
    sentence=sentence.replace(" ","")
    first_word=sentence[:1]
    if first_word==first_word.upper():
        caps+=1

    elif first_word!=first_word.upper():
        #print(first_word)
        small+=1



if small > 0:
    print("All senctences are NOT begining with capital letter")
else:
    print("All senctences are begining with capital letter")