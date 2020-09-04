#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 12:39:05 2020

@author: venky

import string

letters = string.ascii_lowercase
nums  = list(range(1,27))

key = dict(zip(letters,nums))
print(key)


word = "happy"

count = sum([key[i] for i in word])
print(count)

print(key['h'])
print(key['a'])
print(key['p'])
print(key['p'])
print(key['y'])
#print(key['0'])



x = ' '
a = "abcdefg"

place = 0
while len(x)<4:
    x +=a[place]
    print(a[place])
    place += 1
    print(x,place)



#count method
dad = "dadaddadaddadad"
count = 0
for i in range(len(dad)):
     if dad[i:i+3] =="dad":
         count+= 1
         
print(count)         
        

#find method

x = "abcdefga"

print(x.find('a'))
print(x.find('c'))
print(x.find('d'))
print(x.find('e'))
print(x.find('h'))
print(x.find('a',1))
#find('a',1) return  second postion  of  a
"""
#sub_string  find method 1
dad = "dadaadadaddad"
count,place = 0, 0

while dad.find('dad', place) >=0:
    place = dad.find('dad', place) + 1
    count += 1
    
print(count)


dad = "dadaadadaddad"
sub = 'dad'
mom = 'mom'

##sub_string  find method 2
def sub_string(s,sub):
    count,place = 0,0
    while s.find(sub,place) >= 0:
        place = s.find(sub,place) + 1
        count += 1
    return '{} happen {} times'.format(sub,count)

print(sub_string(dad,sub))  
print(sub_string(dad,mom))  
        
    
#format phone numbers

def phone_number():
    x = input("Enter a  phone number:")
    print("{}-{}-{}".format(x[:3],x[3:6],x[6:]))   
    
phone_number()    










