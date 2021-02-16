#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 15:01:32 2021

@author: parth
"""

def Convert(seq): 
    list1 = [] 
    list1[:0] = seq 
    return list1 


seq1 = input("Enter the Sequence: ")
seq2 = input("Enter the second sequence: ")
a = Convert(seq1)
b = Convert(seq2)

li = []
for i in range(len(a)):
    if a[i] != b[i]:
        li.append(1)
        
print(len(li))