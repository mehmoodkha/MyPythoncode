'''Take a number as input from the user.
Print all the squares of numbers from 1 to any large number.
The numbers printed should be less than
the number given as input by the user'''


num=int(input("Enter any number:"))

for i in range(1,num):
    print(i)
    squares=i*i

    print("squre of",i, "is",squares)
    i+=1
