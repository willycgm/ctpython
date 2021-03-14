# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 11:16:11 2021

@author: user
"""
"""

*****
****
***
**
*
**
***
****
*****

"""
inp = int(input('輸入:'))
for j in range(inp,0,-1):
    for k in range(0,j):
        print ('*' ,end='')
    print ()
for j in range(1,inp):
    for k in  range(0,j+1):
        print ('*' ,end='')
    print ()    
        
        