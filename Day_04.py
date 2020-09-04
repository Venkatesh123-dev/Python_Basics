#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 10:49:02 2020
palindrome checking
@author: venky
"""

def pal(x):
    x = x.lower()
    if x==x[::-1]:
        return  True
    else:
        return False
    
print(pal("bob"))
print(pal("madam"))  
print(pal("venky"))   


from tabulate import tabulate

""" Instagram Example """
def print_formater():
    data = {"Name": ["James Smith", "Maria Garcia", "Jane Doe"],
            "Age": [27, 19, 99],
            "Gender": ["Male", "Female", "Female"]}
    return tabulate(data, headers="keys", tablefmt="github")

print(print_formater()) 


def pure_example(header):
    data = [["Header 1", "Header 2", "Header 3"],
            ["Element 1", "value_1", "value_2"],
            ["Element 2", "value_1", "value_2"], 
            ["Element 3", "value_1", "value_2"], 
            ["Element 4", "value_1", "value_2"]]
    return tabulate(data, headers=header)

print(pure_example("firstrow"))




def real_example(header):
    data = {"Name": ["Alice", "Bob", "Jane"],
            "Age": [22, 44, 66]}
    return tabulate(data, headers=header)

print(real_example("keys"))




name = [i.strip() for i in input("enter a names  with seperated with comma:").split(',')]
print(name)
