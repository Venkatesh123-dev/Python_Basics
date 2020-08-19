#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 11:58:30 2020

@author: venky
"""
"""
#Nested loops
for i in range(5):
    for j in range(i):#startig from 0 if i = 0, j=0, if i=1, j= 0,1
        print(j)


for i in range(5):
    print(i, end= " ")
    
""" 
    
def is_divisor(num,div):
    if num %div == 0:
        print("is  divisor")
    else:
        print("Not divisor")
    
    
is_divisor(4,2)
is_divisor(9,4)    


num = [0,1,2,3]
reverse_num = num
reverse_num.reverse()
print(reverse_num)

def factors(x):
    d = [i for i in range(1,x+1) if x %i == 0]
    return d

print(factors(18))
    













