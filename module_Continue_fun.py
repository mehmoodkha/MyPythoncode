#!/usr/bin/python
# Name of this script/module is module_Countinue_fun
def reuse():
    value=input("Do you want to continue:")
    if value.lower()=="yes":
        print("Continue")
        return True
    else:
        return False

if __name__=="__main__":
    reuse()

'''
Exapmle use of this module in following program: 

from module_Continue_fun import reuse 


while True:
    print("Lets add two numbers")
    a = int(input("First num: "))
    b = int(input("Second num: "))
    print("Addition is: ", a + b)
    if reuse()==False:
        break
'''


