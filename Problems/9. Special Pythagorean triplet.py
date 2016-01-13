# -*- coding: utf-8 -*-
"""
Project Euler

Problem 9

Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

************

What do we know:
    1 <= a <= 332
    251 < b < 500
    
    from relations above, a = (10^6 - 2000*b) / (2000 - 2b)
                 and      c = 1000 - a - b

"""
#from math import sqrt
from time import time

if __name__ == '__main__':
    startTime = time()
    
    sumOfABC = 1000

    for b in range(int(sumOfABC/4+1), int(sumOfABC/2+1)):
        a = ((sumOfABC**2-2*sumOfABC*b)/(2*sumOfABC-2*b))
        c = sumOfABC - a - b
        if ((a + b + c) == sumOfABC and a % 1 == 0):
            a = int(a)
            c = int(c)
            break

    totalTime = time() - startTime
    print("a:", a, ", b:", b, ", c:", c, ", a + b + c =", a+b+c)
    print("a * b * c =", a*b*c)
    print("Time to find:", totalTime)
