#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 16:35:40 2020

@author: venky
"""
a=['2.3, 4, 1.3', '6.1, 9.0, 7.3']

b = [[float(j) for j in  i.split(',')] for i in a]

print(b)

#output [[2.3, 4.0, 1.3], [6.1, 9.0, 7.3]]

#patteern  program
x = 6

for i in range(1,x+1):
    print(' ' * (x - i), end = ' ')#spaces
    for j in range(i*2 -1):
        print(str(i), end= '')#digits
    print()    
    
#output    
"""
  1
   222
  33333
 4444444
 
 
numbers = [1, -4, 5, -9, 11] 
for number in numbers:
    if number == 0:
        print( "zero")
    else:
        if number > 0:
            print( "Postive")
        else:
            print ("Negative")
 """
    
def pos_neg(x):
    if number == 0:
        print( "zero")
    else:
        if number > 0:
            print( "Postive")
        else:
            print ("Negative")
            
            
numbers = [1, -4, 5, -9, 11] 
for number in numbers:
    pos_neg(number)   
    
    
#pattern program2

for row in range(1,15):
    for col in range(1,row+1):
        print('{:3}'.format(col), end = " ")
    print()    
    
    


count = int(input('Enter a number:'))
print('ready to go')
while count >= 0:
    print(count)
    count -= 1  
    
print("Blast of !!!!!!*****")    


#time table


def time_table():
    while True:
        try:
            x = int(input("Enter a number"))
            for row in range(x+1):
                for col in range(x+1):
                    print(f"{row*col:3}", end = " ")
                print()
          
        except ValueError:
            print("Ooops  Please Try again")
        choice = input("Do you want  try  another table y/n").lower()    
        if choice == 'no':
            break
       
    
     
    
    
time_table()   


 
    
 
    