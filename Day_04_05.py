#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 19:13:24 2020

@author: venky
"""


def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
     
    return True    



test = [3, 6, 11, 32]
for num in test:
    print(f"{num} is a prime number {is_prime(num)}")
    
    
    
def nth_prime(x):
    num = 3
    prime = 2
    if x ==1:
        return 2
    while prime < x:
        num += 2
        if is_prime(num):
            prime += 1
    print(num) 

nth_prime(10) 

primes  = [i for i in range(1,101) if  is_prime(i)]
print(primes)    




import random

while   True:
    number = random.randint(1,20)
    print(number)
    try:
        guess = int(input("Enter a number"))
        while guess!=number:
            if guess > number:
                print("Please enter a small number")
                guess = int(input("Enter a number"))
            else:
                print("Please enter a larger  number")
                guess = int(input("Enter a number"))
                
        else:
            print("You guess the correct number")
    except ValueError:
        print("oops  Please  enter correct number")

    choice = input("Do you want to play again ? y/n :").lower()
    if choice == 'n':
        break        
                   
                
   
def leap_year(x):
    if x %4 == 0:
        if x % 100 == 0:
            if  x % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return  False
    
years = [1992, 1600, 2000, 2020]
for year in years:
    print(year,leap_year(year))    
                 
   
        
        
    
        
    
    
    
    
    
    
    
   























 