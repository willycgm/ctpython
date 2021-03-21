# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 11:20:58 2021

@author: user
"""
"""
由系統亂數產生 1-49 六個不重複的整數
請遞增排序印出
"""
#03/21完成
import random
data = list()

while True:
    r = random.randint(1, 49)
    if data.count(r) == 0: # 不重複加入
        data.append(r)
    if len(data) == 6: #6個離開
        break
    
data.sort() #排序
print(data)        