#!/usr/bin/python
'''Ask the user to enter a number.
- If the user enters a number as 5, then
generate the following string :
- 00001111222233334444

 If the user enters the number as 3, then
generate the following string :
- 001122'''

num=int(input("Enter number: "))
list1=[]
for i in range(num):
    out=(str(i)*(num-1))
    list1.append(out)

output="".join(list1)
print(output)
