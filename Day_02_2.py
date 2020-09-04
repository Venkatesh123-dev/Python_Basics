#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 21:27:17 2020

@author: venky


How to read/process command line arguments in Python?

The official way of reading or processing the command line arguments is by using the argparse from ArgumentParser module.

The argparse module enables is implementing the user-friendly command-line interfaces. The program defines the arguments it requires, and argparse will ascertain how to parse those out of the sys.argv? The argparse also generates the help and usage messages and issues errors when the users give the program invalid arguments."""

import argparse

parser = argparse.ArgumentParser(description='Process the numbers')
parser.add_argument('integers',metavar='N', type=int, nargs='+', help='an integer for addition')
parser.add_argument('--sum',dest='addition', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')
args = parser.parse_args()
print(args.addition(args.integers))

Case 1: running the method without passing the arguments

    python argparse_example.py 
    usage: argparse_example.py [-h] [--sum] N [N ...]
    argparse_example.py: error: the following arguments are required: N
Case 2: Running the method passing the -h as argument

    python argparse_example.py -h
    usage: argparse_example.py [-h] [--sum] N [N ...]

    Process the numbers

    positional arguments:
      N           an integer for addition

    optional arguments:
      -h, --help  show this help message and exit
      --sum       sum the integers (default: find the max)
Case 3: Running the method passing the numbers (returns max of list of numbers)

    python argparse_example.py 1 2 3 4
    4
Case 4: Running the method passing the –sum argument as an argument, along with list of numbers

    python argparse_example.py 1 2 3 4 --sum
    10
