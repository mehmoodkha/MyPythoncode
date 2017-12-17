
#!/usr/bin/python

''' Check if a given number is a fibonacci number.
If not, then print the closest fibonacci number to the given number
'''

check=int(input("Enter number to check if its a fibonacci number or Not: "))

num1 = 1
num2 = 1
count=0
while count <= check:
    fib_num=num1+num2
    num1=num2
    num2=fib_num
    #print("Fib no: ",fib_num)
    count += 1
    #print("Fib no new: ", fib_num)
    if fib_num==check:
        print(check,"is fibonacci number")
        break
