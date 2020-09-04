#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 12:06:49 2020

@author: venky
"""
#Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.
values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2 == 0) and (int(s[1])%2 == 0) and (int(s[2])%2 == 0) and (int(s[3])%2 == 0):
        values.append(s)
print ",".join(values)

lst = []

for i in range(1000,3001):
    flag = 1
    for j in str(i):          # every integer number i is converted into string
        if ord(j)%2 != 0:     # ord returns ASCII value and j is every digit of i
            flag = 0          # flag becomes zero if any odd digit found
    if flag == 1:
        lst.append(str(i))    # i is stored in list as string

print(",".join(lst))
OR

def check(element):
    return all(ord(i)%2 == 0 for i in element)  # all returns True if all digits i is even in element

lst = [str(i) for i in range(1000,3001)]        # creates list of all given numbers with string data type
lst = list(filter(check,lst))                   # filter removes element from list if check condition fails
print(",".join(lst))


# map() digits of each number with lambda function and check if all() of them even
# str(num) gives us opportunity to iterate through number by map() and join()
print(','.join([str(num) for num in range(1000, 3001) if all(map(lambda num: int(num) % 2 == 0, str(num)))]))




lst = [str(i) for i in range(1000,3001)]
lst = list(filter(lambda i:all(ord(j)%2 == 0 for j in i), lst))   # using lambda to define function inside filter function
print(",".join(lst))