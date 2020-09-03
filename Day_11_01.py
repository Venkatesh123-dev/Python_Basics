#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 12:54:17 2020

@author: venky

Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Main author's Solution: Python 2
"""
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x = int(raw_input())
print fact(x)

#My Solution: Python 3
#Using While Loop

n = int(input()) #input() function takes input as string type
                 #int() converts it to integer type
fact = 1
i = 1
while i <= n:
    fact = fact * i;
    i = i + 1
print(fact)

#Using For Loop

n = int(input()) #input() function takes input as string type
                #int() converts it to integer type
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)

#Using Lambda Function



n = int(input())
def shortFact(x): return 1 if x <= 1 else x*shortFact(x-1)
print(shortFact(n))

#

from functools import reduce

def fun(acc, item):
	return acc*item

num = int(input())
print(reduce(fun,range(1, num+1), 1))