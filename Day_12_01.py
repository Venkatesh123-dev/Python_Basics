#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 12:03:20 2020

@author: venky
"""
#Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:
"""
hello world and practice makes perfect and hello world again
Then, the output should be:

again and hello makes perfect practice world
"""

s = raw_input()
words = [word for word in s.split(" ")]
print " ".join(sorted(list(set(words))))
#Python 3

word = input().split()

for i in word:
    if word.count(i) > 1:    #count function returns total repeatation of an element that is send as argument
        word.remove(i)     # removes exactly one element per call

word.sort()
print(" ".join(word))

OR

word = input().split()
[word.remove(i) for i in word if word.count(i) > 1 ]   # removal operation with comprehension method
word.sort()
print(" ".join(word))

OR

word = sorted(list(set(input().split())))              #  input string splits -> converting into set() to store unique
                                                       #  element -> converting into list to be able to apply sort
print(" ".join(word))

OR
inp_string = input("Enter string: ").split()
out_string = []
for words in inp_string:
    if words not in out_string:
        out_string.append(words)
print(" ".join(sorted(out_string)))