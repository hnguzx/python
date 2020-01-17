'''
Created on 2020年1月8日

@author: Administrator
'''
from pip._vendor.distlib.compat import raw_input
# print("how old are you?"),
age = raw_input("how old are you?")
print("How tall are you?"),
height = raw_input() 
print("how much do you weight"),
# weight = raw_input()
weight = input()
print("so,you're %r old,%r tall and %r heavy," % (age,height,weight))

