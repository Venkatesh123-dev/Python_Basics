#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 12:48:22 2020

@author: venky

Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
Consider use range(#begin, #end) method.
"""
#Solution: Python 2

l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

#print (','.join(l))
#Solution: Python 3

#Using for loops

for i in range(2000,3201):
    if i%7 == 0 and i%5!=0:
        print(i,end=',')
print("\b")

#Using generators and list comprehension
#print(*(i for i in range(2000, 3201) if i%7 == 0 and i%5 != 0), sep=",")