# -*- coding: utf-8 -*-
# 这是一行注释
# createTime 2020/01/06

#导入外部方法
from sys import argv
#拆包
script,input_file = argv
#方法定义
def print_all(file):
#打印从文件中读取到的内容
    print("方法：print_all执行",file.read())
    
#方法定义
def rewind(file):
#移动文件读取指针到指定位置。
    print("方法：rewind执行")
    file.seek(0)
    
#方法定义
def print_a_line(line_acont,file):
#打印读取位置和当前位置的内容
    print("方法：print_a_line执行")
    print(line_acont,file.readline())
    
#读取一个文件
current_file = open(input_file)
print("方法：open执行，")

#打印信息
print("First let‘s print the whole file:\n")
#调用自定义方法，打印文件的所有信息
print_all(current_file)

print("Now let's rewind ,kind of like a tape")
rewind(current_file)

print("Now let's print three lines:")
current_line = 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)

print("重新开始！")
rewind(current_file)

current_line += 1
print_a_line(current_line,current_file)
# 这是最后的注释！