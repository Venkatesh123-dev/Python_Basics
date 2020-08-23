#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 18:24:40 2020

@author: venky
"""

num = [2, 3, 4, 5, 6, 7, 8,9]
def even_n(val):
    if (val%2==0):
        return val
    
    
even_list = list(filter(even_n,num)) 
print(even_list)   
        
    
    
def cube_n(value):
    return pow(value,3)


cube_list = list(map(cube_n,num))    
print(cube_list)


from functools import reduce

def product(a,b):
    return a * b


prod = reduce(product,num)
print("product of nums are" , prod)




#map and filter work on  function name  

#filter  discord the values  which  is not return  by  function name

#reduce apply rooling sequenc computaion to give function


