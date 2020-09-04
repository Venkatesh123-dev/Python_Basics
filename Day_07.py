#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 21:22:18 2020

@author: venky
"""
#map function

grade = [6,7,7, 8]

def add(x):
    return x+1

new_grade = list(map(add,grade))
print(new_grade)

new_grade_ = list(map(lambda x:x+1, grade))
print(new_grade_)


#longset substring

x = "abaagbhcoz"

sub = x[0]

long,length = sub, 1

for i in x[1:]:
    if ord(sub[-1]) <= ord(i):
        sub+= i
        
    print(sub)   
    
    
    
import sys

print(sys.argv)    


#itertools  combinations

from itertools  import combinations as com 

letters = "ABCDEFGH"

x = com (letters,4)

y = [''.join(i) for i in x]

print(y)


from itertools  import accumulate,count

import operator


x = list(range(1,5))

y = list(accumulate(x,operator.add))
print(y)

y = list(accumulate(x,operator.mul))


print(y)






