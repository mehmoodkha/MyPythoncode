#!/usr/bin/python
''' program for search and replace : strings '''

orig_text=input("Please enter the text to start with: ")
search=input("Which word you want to search in given text: ")
replace=input("What new word it shoud replace with: ")

output=orig_text.find(search)

if output >= 0:
    print("\n Given word",search,"found in given text.")
    print("lets replace it now with",replace)
    print("\n New text is: ",orig_text.replace(search,replace))

elif output== -1:
    print("\n",search,"Not found in given text ")

