# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 14:12:30 2021

@author: user
"""

"""
1.min=1 max=100
ans=90
輸入50   顯示51-100
2.如果猜錯5次離開
"""
import random
ans = random.randint(1, 100)
a = 1
b = 100
guess = 0
count = 1
while ans != guess:
    
    
    if count<=5:
        print ('第%d次開始猜'%(count),end='')
        guess = int(input('輸入%d-%d之間整數: '%(a,b)))
        if guess > ans:
            b = guess-1
            print ('猜小一點')
        elif guess < ans:
            a = guess+1
            print ('猜大一點')
        else:
            print ('猜對了')
            break
        count+=1 
    else:
        break
        
        