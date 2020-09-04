#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 18:07:50 2020

@author: venky
"""
def eval_expression(arr):
    stack=[]
    operator=["+","-","*","/","%"]

    for item in arr:
        if item not in operator:
            stack.append((item))
        else:
            first=int(stack.pop())
            sec=int(stack.pop())

            if(item=="+"):
                stack.append(sec + first)

            if (item == "-"):
                stack.append(sec - first)

            if (item == "*"):
                stack.append(sec * first)

            if (item == "/"):
                stack.append(sec / first)

            if (item == "%"):
                stack.append(sec % first)

    return stack[-1]

A =   ["2", "1", "+", "3", "*"]
print(eval_expression(A))