'''
Created on 2020年1月6日

@author: Administrator
'''

x = "这里面有一个数字 %d" % 10
binary = "binary"
do_not = "don't"
y = "两个字符串放在一起 %s%s" % (binary,do_not)
print(x,end="")
print(y)

print("%r" % x)

hil = False
joke = "Isn't that funny %r"

print(joke % hil)

print ("?" * 10)
