# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 23:02:56 2019

@author: Chris Mueller
"""

def baseb(n, b):
    if isinstance(n, str):
        try:
            n = int(n)
        except ValueError:
            raise ValueError('Strings submitted must be convertable to ints')
    if isinstance(n, float) and str(int(n)) != str(n)[:-2]:
        raise ValueError('Supplied number to convert does not convert to ' +
                         'integer well. Please consider submitting values ' +
                         'larger than 1e15 with exponents or as string')
    e = int(n//b)
    q = int(n%b)
    if n == 0:
        return '0'
    elif e == 0:
        return str(q)
    else:
        return baseb(e, b) + str(q)