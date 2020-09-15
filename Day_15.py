#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 16:30:03 2020
#itertools.product()
@author: venky

A = [1, 2]
B = [3, 4]

AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
"""

from itertools import product

A =  [int(x) for x in input().split() ]
B =  [int(y) for y in input().split() ]

print (*product(A,B))


from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in product(a,b):
    print(i, end = " ")
    
#itertools.permutations()
"""
print list(permutations(['1','2','3'],2))
[('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2') 
Sample Input

HACK 2
Sample Output

AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH

"""

from itertools import permutations


s,n = input().split()
s = sorted(s)
n  = int(n)

for i in list( permutations(s,n)):
    print(''.join(i))
   
    
import itertools
string, permutation_size = input().split()
for permutation in itertools.permutations(sorted(string), int(permutation_size)):
    print(''.join(permutation))



#itertools.combinations()
"""
Sample Input

HACK 2
Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK
"""
import itertools
from itertools import combinations


s,n = input().split()
s = sorted(s)
n  = int(n)

for length in range(1,n+1):
    for combination in  itertools.combinations(s,length):
        print(''.join(combination))


#second approach
import itertools
sk = input().split()
s = sk[0]
k = int(sk[1])

for i in range(1,k+1):
    output = list(itertools.combinations(sorted(s),i))
    for i in output:
        for m in i:
            print(m, end = '')

        print()    
    

#itertools.combinations_with_replacement()
"""
Sample Input

HACK 2
Sample Output

AA
AC
AH
AK
CC
CH
CK
HH
HK
KK

"""
import itertools

string,combination_size = input().split()

for combination  in itertools.combinations_with_replacement(sorted(string),int(combination_size)):
    print(''.join(combination))










   