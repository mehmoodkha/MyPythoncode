#!/usr/bin/python

''' Take input from user till he enters number 0 '''
ctr=0
while True:
    num = int(input("Enter number : "))
    if num == 0:
        break
    if ctr==0:
        min=num
        max=num
        ctr=1
        continue

    if num > max:
        max=num
    if num < min:
        min=num


print("maximum is ", max)
print("minmum is ", min)
