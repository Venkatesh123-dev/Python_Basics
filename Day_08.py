#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 16:08:28 2020

@author: venky
"""
#  wtite programm to find out common  letters in two strings?

def common_letters():
    str1 = input("Enter a first string:")
    str2 = input("Enter a  second string:")
    s1 = set(str1)
    s2 = set(str2)
    l = s1 & s2
    return l


print(common_letters())


#write python program  for count frequency  in  word

from collections import Counter



def count_word(str1):
    #str1 = str.split()
    print(Counter(str1))

count_word("Welcome to Guru99 Tutorials!")


def freq_word():
    str1 = input("Enter a  string you want ot  check ?")
    lst = str1.split()
    d = {}
    
    for i in  lst:
        d[i] = d.get(i,0) + 1
    print(d)
    
    
freq_word()     
    

"""

    for i in  lst:
        if i not in d.keys():
            d[i] = 0
        d[i] = d[i]+1
         
    print(d) """
    
    
    

 
    





















    