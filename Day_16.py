#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:03:33 2020
Compress the String!


@author: venky

Sample Input

1222311
Sample Output

(1, 1) (3, 2) (1, 3) (2, 1)
"""
from itertools import groupby

for key, group in groupby(input()):
    print((len(list(group)), int(key)), end=' ')
    
from itertools import groupby
s = input()
for key,group in groupby(s):
    a = len(list(group)),int(key)
    print(tuple(a), end = ' ')    
    
"""
Iterables and Iterators
Sample Input

4 
a a c d
2
Sample Output

0.8333
"""   
from itertools import combinations
n = int(input())
l = input().split()
m = int(input())
count = 0
for i in combinations(l,m):
    if 'a' in i:
        count += 1

print(count/len(list(combinations(l,m))))     



from itertools import combinations

n = int(input())
array = input().split()
k = int(input())

comb_list = list(combinations(array, k))
a_list = [e for e in comb_list if 'a' in e]
print(len(a_list) / len(comb_list))    