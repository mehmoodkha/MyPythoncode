#!/usr/bin/python

''' Program to print multiplication table using for and while loop'''

def using_for(num1):
    print("Output Using FOR loop:\n ")
    for i in range(1,10):
        print(i*num1)

def using_while(num2):
    print("Output Using WHILE loop:\n ")
    count=1
    while count <=10:
        print(num2*count)
        count+=1

def get_number():
    num1=int(input("Enter no. to print multiplication number using FOR loop: "))
    num2=int(input("Enter no. to print multiplication number using WHILE loop: "))
    return num1,num2

num1,num2=get_number()
print(num1,num2)
using_for(num1)
print("------------")
using_while(num2)


