#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 20:09:58 2020

@author: venky
"""

def my_list():
    while True:
        with open('shopping_list.txt','a+') as file:
            print("""type anytime
EXIT: to quit
LIST: To Read and Delete
""")
            item = input('enter item: ')
            if item == 'EXIT':
                break
            elif item == 'please tell':
                print(file.tell())
            elif item == 'LIST':
                file.seek(0)
##                print(file.read())
                items = list(enumerate(file.read().split(),1))
                for count, item in items:
                    print(f"{count:3d}) {item}")
##                remove = int(input('enter number to delete or 0 to continue: '))
                while True:
                    try:
                        remove = int(input('enter number to delete or 0 to continue: '))
                        if remove == 0:
                            break
##                            continue
                        else:
                            del items[remove - 1]
                            with open('shopping_list.txt', 'w') as file:
                                for item in items:
                                    file.write(item[1] + '\n')
                    except ValueError:
                        print("If you don't want to delete please enter 0")
                          
            else:
                file.write(item + '\n')
            

my_list()  