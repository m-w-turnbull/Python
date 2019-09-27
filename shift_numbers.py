#!/usr/bin/env python3

list1 = [1, 2, 3, 12, 9, 9, 6]
list2 = []

def shift_nums():
    try:
        list2.append(list1.pop(0))
    except IndexError:
        exit()
    else:
        check_sums()

def check_sums():
    if sum(list1) == sum(list2):
        print(str(list2) + " = " + str(list1) + " TRUE" )
        exit()
    else:
        print(str(list2) + " = " + str(list1) + " FALSE" )
        shift_nums()

if __name__ == "__main__":
    shift_nums()
