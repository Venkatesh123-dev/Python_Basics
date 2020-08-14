#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 20:03:12 2020

@author: venky


# Define a find_my_letter function that accepts two arguments: a string and a character
# The function should return the first index position of the character in the string
# The function should return a -1 if the character does not exist in the string
#
# EXAMPLES:
# find_my_letter("dangerous", "a")    => 1
# find_my_letter("bazooka", "z")      => 2
# find_my_letter("lollipop", "z")     => -1
"""
def find_my_letter(word,chracter):
    return word.find(chracter)

print(find_my_letter("dangerous", "a") )
print(find_my_letter("bazooka", "z"))
print(find_my_letter("lollipop", "z")) 
