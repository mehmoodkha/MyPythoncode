#!/usr/bin/python
''' Game of cricket, Enter details of game process'''

print("----------------------------------------------------")
print("Please enter game progress ball-by-ball: Lets Play")
print("----------------------------------------------------")

count=1
total=0
while count!=0:

    entry=input("Enter RUN/DOT/WKT: ")
    if entry == "4" or entry == "6":
        print("Awesome shot, You scored the boundry!!! ")
    elif entry=="1" or entry=="2" or entry=="3":
        print("Good shot for",entry,"runs!!")
    elif entry==".":
        entry=0
        print("Dot ball")
    elif entry=='':
        print("....Thats Out....")
        break
    elif entry==".":
        print("No Run... its a Dot ball")
    run=int(entry)
    total+=run
    count+=1
    balls=count
    if balls==7:
        print("\nOver finished!!! Starting next Next over")

print("-----------------------------")
print("You scored ",total,"runs in",balls,"balls")
print("-----------------------------")
