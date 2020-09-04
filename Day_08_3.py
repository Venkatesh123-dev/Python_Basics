#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 17:41:21 2020

@author: venky
"""
#Find Out Pairs with given sum in an array in python  time complexity O(n log n)

def twosum(arr,sum):
    arr.sort()
    left=0
    right=len(arr)-1
    while(left<=right):
        if(arr[left]+arr[right]>sum):
            right=right-1
        elif(arr[left]+arr[right]<sum):
            left=left+1
        elif(arr[left]+arr[right]==sum):
            print("Values of pair are",arr[left],"&", arr[right])
            right=right-1
            left=left+1
            
            
          
            
arr=[5,7,4,3,9,8,19,21]
sum=17
twosum(arr,sum)   




def twosum_hashmap(arr,sum):
    dict={}
    for i in range(len(arr)):
        if(sum - arr[i] in dict):
            return [sum-arr[i],arr[i]]
        elif(arr[i] not in dict):
            dict[arr[i]]=i


arr=[5,7,4,3,9,8,19,21]
sum=17
s=twosum_hashmap(arr,sum)
print(s)






#threesum
def threeSum(arr, target):
    arr.sort()
    size=len(arr)
    max=float('inf')
    res=0
    i=0
    while i<size:
        start = i + 1
        end= size -1
        while start < end:
            sum = arr[i] + arr[start] + arr[end]
            diff = abs(sum - target)
            if diff == 0:
                return sum
            if diff < max:
                max = diff
                res = sum
            if sum <= target:
                start += 1
            else:
                end -= 1
        i=i+1
    return res

arr= [7,12,3,1,2,-6,5,-8,6]
target = 5
print(threeSum(arr,target))
       