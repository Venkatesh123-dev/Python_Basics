#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 11:34:32 2020
Hacker rank problesm
@author: venky
"""
Input Format
The first line contains the first integer a, b, and the second line contains the second integer, .

Output Format
Print the result as described above.

Sample Input

177
10
Sample Output

17
7
(17, 7)

Help on built-in function divmod in module __builtin__:

divmod(...)
    divmod(x, y) -> (quotient, remainder)
    
    Return the tuple (x//y, x%y).  Invariant: div*y + mod == x.
(END)


#Mod Divmod
d = divmod(int(input()), int(input()))
print(*d, d, sep='\n')

a = int(input())
b = int(input())
print(a // b)
print(a % b)
print (divmod(a,b))


#Power - Mod Power - Hacker Rank Solution

a, b, m = [int(input()) for _ in range(3)]
print(pow(a, b), pow(a, b, m), sep='\n')

#Integers Come In All Sizes



a,b,c,d = [ int(input()) for _ in range(4)]
print( a ** b + c ** d )
"""
#Triangle Quest
1
22
333
4444
55555
......"""

for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((pow(10,i)//9)*i)
    
for i in range(1, int(input())):  # More than 2 lines will result in 0 score. Do not leave a blank line also
    print(i * ((pow(10, i) - 1) // 9))    
    
"""
Triangle Quest 2
1
121
12321
1234321
123454321

"""    

for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((pow(10,i)//9)** 2) 
    