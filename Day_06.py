#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 19:52:48 2020

@author: venky

scope  and  decarators
"""

#local global  bulit in functonaily
from string import ascii_lowercase  as lower

"""
key = {}

for i in range(len(lower)):
    key[lower[i]]  = 1+ i

"""

letters = lower

num = list(range(1,27))   

key = dict(zip(letters,num)) 
    

students = ["venky", "Raj", "Hello", "danny"]

s_dict = {student[0].lower(): student for student in  students}
print(s_dict)


#decarator function
def upper(func):
    def wrapper():
        return func().upper()
    return wrapper

@upper
def hi():
     return "Hi how  are you?"
    

print(hi())























