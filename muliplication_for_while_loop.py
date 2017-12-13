#!/usr/bin/python
''' Program to print multiplication table using for and while loop'''


num1=int(input("Enter no. to print multiplication Table using for loop: "))
print("Output Using FOR loop:\n ")
for i in range(1,10):
    print(i*num1)    

print("------------")

num2=int(input("Enter no. to print multiplication Table using WHILE loop: "))
print("Output Using WHILE loop:\n ")
count=1
while count <=10:
    print(num2*count)
    count+=1
