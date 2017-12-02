#!/usr/bin/python

print("\n Evaluate no of digit in given input and perform action \n")


def do_one_digit_oper():
    one=num+7
    print("Final output is ", one)

def do_two_digit_oper():
    two=num**5
    print("final output is ", two)

def do_three_digit_oper():
    new=int(input("Enter new Number: "))
    three=new+num
    print("Final outputis", three)
def get_number():
    number=int(input("Enter the number to check: "))

    return number

num=get_number()
if str.__len__ (str(num)) == 1:
    print("This number is ONE digit, Lets perform action as per request\n")
    do_one_digit_oper()
elif str.__len__(str(num)) == 2:
    print("This number is TWO digit, Lets perform action as per request\n")
    do_two_digit_oper()
elif str.__len__(str(num)) == 3:
    print("This number is THREE digit, Lets perform action as per request\n")
    do_three_digit_oper()
else:
    print(num)
