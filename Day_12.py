#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:54:16 2020

@author: venky

Write a program that calculates and prints the value according to the given formula:

Q = Square root of [(2 _ C _ D)/H]

Following are the fixed values of C and H:

C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma separated input sequence is given to the program:

100,150,180
The output of the program should be:

18,22,24 """

import math
c = 50
h = 30
value = []
items = [x for x in raw_input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print ','.join(value)


from math import sqrt

C,H = 50,30

def calc(D):
    return sqrt((2*C*D)/H)

D = input().split(',')                     # splits in comma position and set up in list
D = [str(round(calc(int(i)))) for i in D]  # using comprehension method. It works in order of the previous code
print(",".join(D))


from math import sqrt
C,H = 50,30

def calc(D):
    return sqrt((2*C*D)/H)

print(",".join([str(int(calc(int(i)))) for i in input().split(',')]))








#_Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i _ j.*

Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5

Then, the output of the program should be:

[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.

x,y = map(int,input().split(','))
lst = []

for i in range(x):
    tmp = []
    for j in range(y):
        tmp.append(i*j)
    lst.append(tmp)

print(lst)


#second
x,y = map(int,input().split(','))
lst = [[i*j for j in range(y)] for i in range(x)]
print(lst)


#Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
"""
Suppose the following input is supplied to the program:

without,hello,bag,world
Then, the output should be:

bag,hello,without,world
"""
items = [x for x in raw_input().split(',')]
items.sort()
print ','.join(items)
 #Python 3

lst = input().split(',')
lst.sort()
print(",".join(lst))


#Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:
"""
Hello world
Practice makes perfect
Then, the output should be:

HELLO WORLD
PRACTICE MAKES PERFECT
"""

lines = []
while True:
    s = raw_input()
    if s:
        lines.append(s.upper())
    else:
        break

for sentence in lines:
    print sentence
#Python 3

lst = []

while True:
    x = input()
    if len(x)==0:
        break
    lst.append(x.upper())

for line in lst:
    print(line)
OR

def user_input():
    while True:
        s = input()
        if not s:
            return
        yield s

for line in map(str.upper, user_input()):
    print(line)













