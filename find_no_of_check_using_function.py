#!/usr/bin/python

print("\nwhich number is a 2 digit and which is a 3 digit number USING FUNCTION\n")


def perform_check(number):
    if str.__len__(number) == 2:
        print (number, "is two digit ")
    elif str.__len__(number) == 3:
        print (number, "is three digit.")
    else:
        print (number)


def get_numer():
    number=raw_input("Enter the number to check: ")  # input and raw_input in python2 & 3 is different.
    return number

num1=get_numer()
num2=get_numer()
perform_check(num1)
perform_check(num2)
