# -*- coding: utf-8 -*-
# 这是一行注释
# createTime 2020/01/06
def print_two(*args):
    arg1,arg2 = args
    print("arg1 = %r ,arg2 = %r" % (arg1,arg2))
    
def print_two_again(arg1,arg2):
    print("arg1 = %r ,arg2 = %r" % (arg1,arg2))
    
def print_one(agr):
    print("arg: %r" % agr)
    
def print_zero():
    print("nothing")

print_zero()
print_one("一个参数")
print_two("有*的1","有*的2")
print_two_again("两个参数的1","两个参数的2")

# 这是最后的注释！