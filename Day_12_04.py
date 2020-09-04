#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 12:25:07 2020

@author: venky
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. >Suppose the following input is supplied to the program:

1,2,3,4,5,6,7,8,9
Then, the output should be:

1,9,25,49,81
"""

lst = [str(int(i)**2) for i in input().split(',') if int(i) % 2]
print(",".join(lst))


lst = input().split(',')     # splits in comma position and set up in list

seq = []
lst = [int(i) for i in lst]  # converts string to integer
for i in lst:
        if i%2 != 0:
                i = i*i
                seq.append(i)


seq = [str(i) for i in seq]   # All the integers are converted to string to be able to apply join operation
print(",".join(seq))


"""
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:

D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:

D 300
D 300
W 200
D 100
Then, the output should be:

"""
total = 0
while True:
    s = input().split()
    if not s:            # break if the string is empty
        break
    cm,num = map(str,s)    # two inputs are distributed in cm and num in string data type

    if cm=='D':
        total+=int(num)
    if cm=='W':
        total-=int(num)

print(total)


account = 0
while True:
    action = input("Deposit/Whitdrow/Balance/Quit? D/W/B/Q: ").lower()
    if action == "d":
        deposit = input("How much would you like to deposit? ")
        account = account + int(deposit)
    elif action == "w":
        withdrow = input("How much would you like to withdrow? ")
        account = account - int(withdrow)
    elif action == "b":
        print(account)
    else:
        quit()
