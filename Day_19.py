#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 10:42:32 2020
oopsss
@author: venky
"""

class User:
    def log(self):
        print(self)
        
        
class Teacher(User):
    print("I am a Teacher")        

class Customer(User):
    
    def log(self):
        print('I am a customer')
        
        
    def __init__(self,name,membership_type):
        self.name = name
        self.membership_type = membership_type
       
        
        
    @property    
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        self._name = name
        
    def update_membership(self,new_membership):
        self.membership_type = new_membership
        
        
        
    def __str__(self):
        return  self.name + " " + self.membership_type
    
    def print_all_customers(customers):
        for customer in customers:
            print(customer)
        
    __repr__ = __str__    
# c = Customer("venky", "Gola")
# print(c.name,c.membership_type)        


# customers = [Customer('calab','gold'),
#             Customer('venky','branze'),
#             Teacher()]
# print(customers[1].membership_type)
# customers[1].update_membership('silver')
# print(customers[1].membership_type)

# Customer.print_all_customers(customers)
# customers[0].log()





Users = [Customer('calab','gold'),
            Customer('venky','branze'),
            Teacher()]
for user in Users:
    user.log()

