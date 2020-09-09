#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 18:47:30 2020

@author: venky

Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

Suppose the following input is supplied to the program:

7
Then, the output should be:

0
7
14  """

class Divisible:

    def by_seven(self, n):
        for number in range(1,n + 1):
            if number % 7 == 0: yield number


divisible = Divisible()
generator = divisible.by_seven(int(input("Please insert a number. --> ")))
for number in generator:
    print(number)
    
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.    


from collections import Counter

ss = input().split()
ss = Counter(ss)         # returns key & frequency as a dictionary
ss = sorted(ss.items())  # returns as a tuple list

for i in ss:
    print("%s:%d"%(i[0],i[1]))
    
ss = input().split()
word = sorted(set(ss))     # split words are stored and sorted as a set

for i in word:
    print("{0}:{1}".format(i,ss.count(i)))  
    
    
  
def pow(n,p):
    '''
    param n: This is any integer number
    param p: This is power over n
    return:  n to the power p = n^p
    '''

    return n**p

print(pow(3,4))
print(pow.__doc__)    

class Car:
    name = "Car"

    def __init__(self,name = None):
        self.name = name

honda=Car("Honda")
print("%s name is %s"%(Car.name,honda.name))

toyota=Car()
toyota.name="Toyota"
print("%s name is %s"%(Car.name,toyota.name))
    