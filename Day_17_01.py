#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 16:17:08 2020

@author: venky
"""
a = "the fox jumps over the lazy dog"
x =  ''.join(x for x in reversed(a))
print(x)


def isPalindrome(word: str) -> bool:
    if(word == word[::-1]):
        return True
    return False


#Question: Write a program that prints the number for 1 to 50, for number multiple of 2 print fizz instead of a number, for numbers multiple of 3 print buzz, for numbers which are multiple of both 2 and 3 fizzbuzz.
def fizzbuzzfn(num) -> str:
    mod_2 = (num % 2 == 0) 
    mod_3 = (num % 3 == 0)
    if (mod_2 or mod_3):
        return (mod_2 * 'Fizz') + (mod_3 * 'Buzz')
    return str(num)
print('\n'.join([fizzbuzzfn(x) for x in range(1,51)]))


#First Duplicate word Given a string find the first duplicate word, example string: “this is just a wonder, wonder why do I have this in mind”
string = "this is just a wonder, wonder why do I have this in mind"
def firstduplicate(string: str) -> str:
    import re
    cleanStr = re.sub("[^a-zA-Z -]", "", string)
    
    words = cleanStr.lower().split(" ")
    seen_words = set()
    for word in words:
        if word in seen_words:
            return word
        else: 
            seen_words.add(word)
    return None
firstduplicate(string)

#Write a function that gives the sum of all fibonacci numbers from 0 to n.
def fibonacci(n: int) -> int:
    # fib series don't exist < 0 
    # might want to throw an error or a null 
    # for that
    if n <= 0: 
        return 0
    if n == 1: 
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
def naiveFibSum(n: int) -> int:
    return sum([fibonacci(x) for x in range(0, n+1)])
def sumFib(n: int) -> int:
    return fibonacci(n + 2) -1



#Python | Find closest number to k in given list
  
def closest(lst, K): 
      
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))] 
      
# Driver code 
lst = [3.64, 5.2, 9.42, 9.35, 8.5, 8] 
K = 9.1
print(closest(lst, K)) 


#given_value = 2
a_list = [1, 5, 8]
absolute_difference_function = lambda list_value : abs(list_value - given_value)

closest_value = min(a_list, key=absolute_difference_function)

print(closest_value)
OUTPUT