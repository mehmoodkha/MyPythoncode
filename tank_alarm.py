#!/usr/bin/python

""" Program to send notification about tank utilization"""

def do_action(present, redmark, bluemark):
    if present >= redmark:
        print("Alarm: Tank level is High, Please close the valve ")
    elif present <= bluemark:
        print("Sendiing SMS to to bye more liquid")
    else:
        print("Current level is ", level)


def get_current_level():
    cur_lev=int(input("What is the current level of tank : "))
    return cur_lev

capacity = 900
high = (80*capacity)/100
low =  (20*capacity)/100
level = get_current_level()
do_action(level, high, low)

