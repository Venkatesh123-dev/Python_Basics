#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 15:27:04 2020
double the given string 
@author: venky
#input:string()
#output:string()

"""

string = "venky"


vowel = "a,e,i,o,u,A,E,I,O,U"

def double(string):
    out =str()
    for i in range(len(string)):
        if (string[i] in vowel):
            out += string[i]*2
        else:
            out += string[i]
            
    print(out)


double(string)            
            

string = 'sequence'
vowel = ['a','e','i','o','u','A','E','I','O','U']
out = str()
for i in range(len(string)):
    if (string[i] in vowel):
        out += string[i]*2
    else:
        out += string[i]

print(out)

       