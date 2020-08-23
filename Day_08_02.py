#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 16:41:42 2020

@author: venky

#Conversion of two list into Dictionary Using Python

def list_to_dict():
    keys = [1, 2, 3]
    values = ['one','Two','three']
    result = dict(zip(keys,values))
    print(result)
    
    
list_to_dict()    


def dict_to_tuple():
    x = {1: 'one', 2: 'Two', 3: 'three'}
    for i in x.items():
        print(i)
        
        
dict_to_tuple()
"""
#FIND MISSING NUMBER IN AN ARRAY IN PYTHON

def get_missing_summation(a):
    n=a[-1]
    sum1=0
    total=n*(n+1)//2
    sum1=sum(a)
    print(total-sum1)

a=[1,2,3,5,6,7]
get_missing_summation(a)        