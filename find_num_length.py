#!/usr/bin/python

print("\nwhich number is a 2 digit and which is a 3 digit number\n")
num1=input(" Enter first number: ")
num2=input(" Enter second number: ")

if num1.__len__() == 2:
    print("First number is two digit. ")
elif num1.__len__() == 3:
    print ("First Number is three digit. ")
else:
    print("First number is ", num1)

if num2.__len__() == 2:
    print ("Second number is two digit.")
elif num2.__len__() ==3:
    print ("Second numer is three digit.")
else:
    print ("Secont number is ", num2)

