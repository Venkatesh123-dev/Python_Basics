#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 12:59:32 2020

@author: venky

With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8

Then, the output should be:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

"""
n = int(raw_input())
d = dict()
for i in range(1,n+1):
    d[i] = i * i
print (d)

#Solution: Python 3:

#Using for loop
n = int(input())
ans = {}
for i in range (1,n+1):
    ans[i] = i * i
print(ans)

#Using dictionary comprehension
n = int(input())
ans={i : i*i for i in range(1,n+1)}
print(ans)

num = int(input("Number: "))
print(dict(list(enumerate(i * i for i in range(num+1)))))