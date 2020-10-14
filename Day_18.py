#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Encapsulation in Python
Created on Tue Oct 13 17:41:08 2020
In this python programming video tutorial  you will learn about encapsulation in detail.

In an object oriented python program, you can restrict access to methods and variables. This can prevent the data from being modified by accident and is known as encapsulation.There are two type access specifiers one is private and another is public.Public methods and variables can be accessible outside the class also.But we cant access private methods outside the class and private variables can be modified only inside the class.

Objects can hold crucial data for your application and you do not want that data to be changeable from anywhere in the code. Encapsulation is helpful in this case.Two underscore at the beginning of method or variable indicates that it is private.
@author: venky
"""
#Public Method
class Animal:
    def __init__(self,name):
        self.name = name
        
     
        
class dog(Animal):
    def display(self):
        print(self.name)
        
        
d = dog('baybydog')
d.display()        
         
    
    
#Prtivate method[Enclapsulation]

"""
class Car:
    def __init__(self):
        self.__updatesoftware()   #<------ Private method Because starting of word we have '__ two underscores'
        
    def drive(self):
        print("driving")
        
        
    def __updatesoftware(self):
        print("Updatingsoftware")
        
        
        
blackcar = Car()
blackcar.drive()
print("----::-------")
print("This is Enclapsulation Example")
    
#    """   

# class Car:
#     # def __init__(self):
#     #     self.__updatesoftware()   #<------ Private method Because starting of word we have '__ two underscores'
        
#     # def drive(self):
#     #     print("driving")
        
        
#     def __updatesoftware(self):
#         print("Updatingsoftware")
        
        
        
# blackcar = Car()
# blackcar.__updatesoftware
# print("----::-------")
# print("This is Enclapsulation Example can not call  private methods outside of class ")




###Private variable can modify only with in calss, can't modify outside class



class car():
    __maxspeed = 0
    __name = ""
    
    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Roolsroyce"
        
    def drive(self):
        print('dirve')   
        print(self.__maxspeed)


    def setspeed(self,speed):
        self.__maxspeed = speed
        print(self.__maxspeed)
        
redcar = car()
redcar.drive()
redcar.setspeed(00)
        
     


class car2():
    __maxspeed2 = 0
    __name2 = ""
    
    def __init__(self):
        self.__maxspeed2 = 200
        self.__name2 = "Roolsroyce"
        
    def drive2(self):
        print('dirve2')   
        print(self.__maxspeed2)


    # def setspeed(self,speed):
    #     self.__maxspeed = speed
    #     print(self.__maxspeed)
        
redcar2 = car2()
redcar2.drive2()

"""
Here we have changed private variable outside the class but it's  value dosen't changed
"""                     
redcar2.__maxspeed2 = 100
redcar2.drive2()
    