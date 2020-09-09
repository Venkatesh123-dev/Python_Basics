#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 18:55:12 2020

@author: venky
Define a function which can compute the sum of two numbers.
"""
def SumFunction(number1, number2):
	return number1 + number2

print(SumFunction(1,2))

sum = lambda n1,n2 : n1 + n2      # here lambda is use to define little function as sum
print(sum(1,2))

conv = lambda x : str(x)
n = conv(10)
print(n)
print(type(n))            # checks the type of the variable


#Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
def printDict():
    dict={i:i**2 for i in range(1,21)}   # Using comprehension method and
    print(dict)

printDict()

def printList():
    lst = [i ** 2 for i in range(1, 21)]
    print(lst)

printList()


#Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.


def printList():
    lst = [i ** 2 for i in range(1, 21)]

    for i in range(5):
        print(lst[i])

printList()


def squares(n):
    squares_list = [i**2 for i in range(1,n+1)]
    print(squares_list[0:5])
squares(20)

#Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.

def squares(n):
    squares_list = [i**2 for i in range(1,n+1)]
    print(squares_list[-5:])
squares(20)

#Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.

def printList():
    lst = [i ** 2 for i in range(1, 21)]
    for i in range(5,20):
        print(lst[i])

printList()

def printTupple():
    lst = [i ** 2 for i in range(1, 21)]
    print(tuple(lst))

printTupple()

def square_of_numbers():
    return tuple(i ** 2 for i in range(1, 21))

print(square_of_numbers())

#With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.
tpl = (1,2,3,4,5,6,7,8,9,10)

for i in range(0,5):
    print(tpl[i],end = ' ')
print()
for i in range(5,10):
    print(tpl[i],end = ' ')
    
#Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

tpl = (1,2,3,4,5,6,7,8,9,10)
tpl1 = tuple(i for i in tpl if i%2 == 0)
print(tpl1)    

#Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".


text = input("Please type something. --> ")
if text == "yes" or text == "YES" or text == "Yes":
    print("Yes")
else:
    print("No")
    
    
#Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

li = [1,2,3,4,5,6,7,8,9,10]
squaredNumbers = map(lambda x: x**2, li)  # returns map type object data
print(list(squaredNumbers))               # converting the object into list


#Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))
print evenNumbers


def even(x):
    return x%2==0

def squer(x):
    return x*x

li = [1,2,3,4,5,6,7,8,9,10]
li = map(squer,filter(even,li))   # first filters number by even number and the apply map() on the resultant elements
print(list(li))


#Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
evenNumbers = filter(lambda x: x%2==0, range(1,21))
print evenNumbers

def even(x):
    return x%2==0

evenNumbers = filter(even, range(1,21))
print(list(evenNumbers))

squaredNumbers = map(lambda x: x**2, range(1,21))
print squaredNumbers

def sqr(x):
    return x*x

squaredNumbers = list(map(sqr, range(1,21)))
print (squaredNumbers)    


