#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 18:48:37 2021

@author: parth
"""
k = int(input("k = "))
m = int(input("m = "))
n = int(input("n = "))

t = k + m + n

A = ((k/t)*((k-1)/(t-1))) + ((k/t)*(m/(t-1))) + ((k/t)*(n/(t-1))) + ((m/t)*(k/(t-1))) + ((1/2)*(m/t)*(n/(t-1))) + ((3/4)*(m/t)*((m-1)/(t-1))) + ((n/t)*(k/(t-1))) + ((1/2)*(n/t)*(m/(t-1)))

print(A)
