#!/usr/bin/python

'''Ask the user to enter a number.
Find the number of digits in that number'''

number=int(input("Enter the number to find no of digits in that no: "))
string_number=str(number)

print("Output:",number,"is",len(string_number),"digit number")
