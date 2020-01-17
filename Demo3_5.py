# -*- coding: utf-8 -*-
# 这是一行注释
# createTime 2020/01/06
from sys import argv
script,filename = argv
text =open(filename)
print("Here's your file %r " % filename)
print(text.read())
file_again =input("type the filenage again:")
text_again =open(file_again)
print(text_again.read())
# 这是最后的注释！