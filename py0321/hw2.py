# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 15:45:59 2021

@author: user
"""
"""
1.由系統產生7個亂數 1-100可重複,遞增排序印出 ex:[10,7,6,100,2,10,90]
2.由使用者輸入當中的值,去尋找串列中的值用2分法顯示尋找過程
"""
#03/21完成
import random
data = []
#data = [38, 39, 42, 53, 57, 76, 92]
#data = [2,9,30,32,38,47,61,69,79,81]

for i in range(1,8):
    data.append(random.randint(1, 100))
data.sort()#遞增排序

print (data)    
# 0,1,2,3,4,5,6, 
sumdata = len(data)#data長度
num = (sumdata // 2) #對半
indata = int(input('請選要找個值:'))
count=0
if data.count(indata) != 0:
    while True:  
        count += 1
        if data[num] == indata: 
            break
        if data[num] > indata:
            del data[num:]
            print ('第%d次'%count,data) 
        else:
            del data[:num+1]#把比對的索引值刪除
            print ('第%d次'%count,data)     
        num = len(data)  // 2            
    print('總共找了%d次'%count)
else:
    print ('索引值沒有%d'%indata)    
