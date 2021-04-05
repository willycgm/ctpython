# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 16:00:40 2021
@author: user
"""

'''
巴斯卡三角形
1
11
121
1331
14641
'''
'''
import random
rows = int(input('Enter the amount of row: '))
columns = int(input('Enter the amount of column: '))
List = [] # 宣告一個一維串列
for i in range(rows):
    List.append([]) # 令其轉為二維串列形式
    for j in range(columns):
        # 將亂數產生的值放入串列中
        List[i].append(random.randint(1, 100))
# 使用 for 迴圈來印出串列
for i in range(len(List)):
    for j in range(len(List[i])):
        print('%5d' %(List[i][j]), end = '')
    print()
'''
indata = int(input("階數:"))
data = list()
for i in range(indata):  #0 - 5
    data.append([]) # 令其轉為二維串列形式
    #[[],[],[],[],[]]
    for j in range(0,i+1):
        data[i].append(0)	
        
data[0][0] = 1
for i in range(1,indata):
    data[i][0] = 1
    data[i][i] = 1
 	
for i in range(2,indata):
    for j in range(1,i):
        #上一層的(前&後相加)        
        data[i][j] = data[i-1][j-1] + data[i-1][j]
		
print (data)   

for i in range(indata):
    for j in range(0,i+1):
        print (data[i][j] ,end=" ")
    print () 