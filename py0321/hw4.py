# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 16:18:45 2021

@author: user
"""

"""
由使用者輸入獲利金額
ex 31w
1.含10萬以內獎金10%  10w *10%
2.10w-20w 獎金 7%   10w *7%
3.20w-40w 獎金 3%   11w *3%
"""
#03/21完成
inmenoy = int(input('請輸入金額:'))
menoy = 0
if (inmenoy>200000):
    menoy += (inmenoy-200000) * 0.03
    menoy += (100000 * 0.07) + (100000 * 0.1)
elif (inmenoy>100000):
    menoy += (inmenoy-100000) * 0.07
    menoy += (100000 * 0.1) 
else:    
    menoy += (100000 * 0.1) 
    
print('獲利金額:',menoy)    