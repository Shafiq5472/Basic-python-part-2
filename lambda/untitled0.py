# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 20:57:12 2022

@author: SHA NU
"""

'''lambda arguments : expression'''

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#%%
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

