'''Ask the user to enter a number.
- If the number is a single digit number, add 7 to it,
and print the number in its unit’s place
- If the number is a two digit number, raise the number to the power of 5,
and print the last 2 digits
- If the number is a three digit number, ask user to enter another number.
Add the 2 numbers and print the last 3 digits'''


def get_num():
    number=input("Please enter number : ")
    return number

def per_oper1():

    oper1_num=int(number) + 7
    oper1_num_str=str(oper1_num)
    print("Lets add 7 to given no: Output is: ", oper1_num)
    print("Number at units place is:",oper1_num_str[-1:])

def per_oper2():
    oper2_num=int(number)**5
    oper2_num_str=str(oper2_num)
    print("Lets add mul of 5 to given no: Output is: ", oper2_num_str)
    print("Last two digits are:",oper2_num_str[-2:])

def per_oper3():
    new_num=int(input("Enter new number: "))
    oper3_num=int(number) + new_num
    oper3_num_str=str(oper3_num)
    print("Addition is ", str(oper3_num))
    print("Last three digits are:",str(oper3_num_str[-3:]))

number=get_num()
if len(number) == 1:
    print("Its one digit no, lets perform action now:")
    per_oper1()
elif len(number)==2:
    print("Its two digit no, lets perform action now:")
    per_oper2()
elif len(number)==3:
    print("Its three digit no, lets perform action now:")
    per_oper3()
else:
    print("number is ",number)
