#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 12:14:34 2020

@author: venky

Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:

hello world! 123
Then, the output should be:

LETTERS 10
DIGITS 3 """

s = raw_input()
d = {"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print "LETTERS", d["LETTERS"]
print "DIGITS", d["DIGITS"]

word = input()
letter,digit = 0,0

for i in word:
    if ('a'<=i and i<='z') or ('A'<=i and i<='Z'):
        letter+=1
    if '0'<=i and i<='9':
        digit+=1

print("LETTERS {0}\nDIGITS {1}".format(letter,digit))



word = input()
letter, digit = 0,0

for i in word:
    if i.isalpha(): # returns True if alphabet
        letter += 1
    elif i.isnumeric(): # returns True if numeric
        digit += 1
print(f"LETTERS {letter}\n{digits}") # two different types of formating method is shown in both solution




import re

input_string = input('> ')
print()
counter = {"LETTERS":len(re.findall("[a-zA-Z]", input_string)), "NUMBERS":len(re.findall("[0-9]", input_string))}

print(counter)


"""
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Suppose the following input is supplied to the program:

Hello world!
Then, the output should be:

UPPER CASE 1
LOWER CASE 9
"""

s = raw_input()
d = {"UPPER CASE":0, "LOWER CASE":0}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print "UPPER CASE", d["UPPER CASE"]
print "LOWER CASE", d["LOWER CASE"]


word = input()
upper,lower = 0,0

for i in word:
    if 'a'<=i and i<='z' :
        lower+=1
    if 'A'<=i and i<='Z':
        upper+=1

print("UPPER CASE {0}\nLOWER CASE {1}".format(upper,lower))

word = input()
upper,lower = 0,0

for i in word:
        lower+=i.islower()
        upper+=i.isupper()

print("UPPER CASE {0}\nLOWER CASE {1}".format(upper,lower))


word = input()
upper = sum(1 for i in word if i.isupper())           # sum function cumulatively sum up 1's if the condition is True
lower = sum(1 for i in word if i.islower())

print("UPPER CASE {0}\nLOWER CASE {1}".format(upper,lower))



"""

Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

Suppose the following input is supplied to the program:

9
Then, the output should be:

11106

"""

a = raw_input()
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
n4 = int( "%s%s%s%s" % (a,a,a,a) )
print n1+n2+n3+n4


a = input()
total = int(a) + int(2*a) + int(3*a) + int(4*a)  # N*a=Na, for example  a="23", 2*a="2323",3*a="232323"
print(total)


from functools import reduce
x = input('please enter a digit:')
reduce(lambda x, y: int(x) + int(y), [x*i for i in range(1,5)])


























