#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 19:47:53 2020

@author: venky
# Define a vowel_count function that accepts a string argument.
# The function should return the count of vowels in the string.
# The 5 vowels are "a", "e", "i", "o", and "u".
# You can assume the string will be in all lowercase.
#
# EXAMPLES:
# vowel_count("estate")        => 3
# vowel_count("helicopter")    => 4
# vowel_count("ssh")           => 0
"""
def vowel_count(word):
    alphabet = "aeiou"
    count = 0
    for i in word:
        if i in alphabet:
            count+= 1
        
    return count  

print(vowel_count("estate"))   
print(vowel_count("helicopter")) 
print(vowel_count("ssh"))  


  


