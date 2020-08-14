#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 21:14:48 2020

@author: venky

#What __init__ and self do in Python?
The __init__ and self are two keywords in python, which performs a vital role in the application.

To begin with, it is important to understand the concept of class and object.

Class

In Object-oriented programming, a class is a blueprint for creating objects of a particular data structure, provisioning the initial values for the state, and implementation of a behavior.

The user-defined objects are created using the class keyword.

Object

It is a basic unit of Object-Oriented Programming and each object is an instance of a particular class or subclass with class's methods or procedures and data variables.

With the above understanding,

__init__
__init__ is a reserved method in python classes. It is used to create an object of a class, something like a constructor in Java. This method when called creates an object of the class and it allows the class to initialize the attributes of the class.
"""
# A Sample class with init method 
class Country:     
    # init method or constructor 
    def __init__(self, name): 
        self.name = name 
    
    # Sample Method 
    def hello(self): 
        print('Hello, my name is', self.name) 
    
c = Country('India') 
c.hello()

"""
In the above example, the line c = Country('India') invokes the method __init__ and creates an object c, which can then further invoke the method hello()."""

"""
self
The word self is used to represent the instance of the class. Using self, the attributes and the methods of the class can be accessed."""
class Country:     
    # init method or constructor 
    def __init__(self, name): 
        self.name = name 
    
    # Sample Method 
    def hello(self): 
        print('Hello, my name is', self.name) 
"""
Output
No output

In the above example, name is the attribute of the class Country and it can be accessed by using the self keyword."""
