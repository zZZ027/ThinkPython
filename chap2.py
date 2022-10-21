# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 16:34:54 2022

@author: 20222
"""

#练习1
#1）输入42=n时，会出现SyntaxError: cannot assign to literal的语法报错
#2）好像是合法的
#3）已分号结尾好像不会发生什么
#4）不会发生什么，但是没有必要打分号
#5)输入xy时，会显示“name 'xy' is not defined”，


#练习2
#1）
import math
r=5
V=4/3*math.pi*r**3
print(V)

#2)
Bk=24.95
Df1=3
Dfr=0.75
n=60
total=Bk*(1-0.4)*n+Df1+Dfr*(n-1)
print(total)

#3)

h0=6
min0=52
minh=h0*60+min0
min1=8
min2=7
sec1=15
sec2=12
secmin1=sec1/60
secmin2=sec2/60
P1=min1+secmin1
P2=min2+secmin2
L1=1
L2=3
L3=1
mint=L1*P1+L2*P2+L3*P1
minl=minh+mint
import math
H1=minl/60
H=math.floor(H1)
M1=minl-H*60
M=math.floor(M1)
S1=(minl-H*60-M)*60
S=math.floor(S1)
print(H,M,S)
