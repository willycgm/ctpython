# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 12:07:46 2021

@author: user
"""

"""
求使用者輸入一個範圍的整數 ex 10  [1-10]:
    (1)求4的倍數有哪些?
    (2)那些是質數?
"""
num = int (input ('使用者輸入: '))
#a=100
for i in range(2,num+1):
    if i % 4 ==0:
        print (i ,'\t是4的倍數')
        
print ('='*20)

print ('2-%d質數有'%(num))
for i in range(2,num+1):
    count = 0
    for j in range(2,i):
        
        if(i%j) == 0:
            count=1
            break
    if(count != 1):
        print (i ,end="\t")


