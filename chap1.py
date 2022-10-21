# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 13:51:46 2022

@author: 20222
"""

#练习1
#1）只有前面的一边括号时，运行时会出现”SyntaxError: unexpected EOF while parsing“的报错提示；只有后面的括号或者没有括号时，会出现“invalid syntax”的语法错误提示
#2）只有一个引号时，会出现“EOL while scanning string literal”的报错提示；没有引号时，会出现“invalid character”的非法字符报错提示
#3)在-2前加“+”，输出结果依然是-2，输入2++2，输出结果是4
#4）输入02时，会出现“SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers”的语法报错提示
#5）输入的两个值之间没有运算符时，会出现“invalid syntax”的语法报错



#练习2
#1)
sec=42
min=42
minsec=sec*60
print(minsec+sec)

#2)
km=10
mile=km*1.61
print(mile)

#3)
sec=42
min=42
minsec=sec*60
secmin=(minsec+sec)/60
sech=(minsec+sec)/3600
km=10
mile=km*1.61
#每英里耗时（分）
print(secmin/mile)
#每英里耗时（秒）
print((minsec+sec)/mile)
#英里/时
print(mile/sech)