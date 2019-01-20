# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 23:02:56 2019

@author: Chris Mueller
"""

def baseb(n, b):
    e = n//b
    q = n%b
    if n == 0:
        return '0'
    elif e == 0:
        return str(q)
    else:
        return baseb(e, b) + str(q)