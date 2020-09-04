#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 21:09:45 2020

@author: venky
"""

#What does if __name__ == '__main__': do in Python?

def main():
    print("module_name :{}".format(__name__))
    
if __name__ == "__main__":
    main()
else:
    print("run from import")



