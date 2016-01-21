# -*- coding: utf-8 -*-
"""
Project Euler

Problem 16: Power digit sum

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?

"""

from time import time

if __name__ == '__main__':
    startTime = time()
    print("\n\n")
    n = 2**1000
    nString = str(n)
    nCharSum = 0
    for aChar in nString:
        nCharSum += int(aChar)



    totalTime = time() - startTime
    print("The sum of the digits of 2^1000 is", nCharSum)
    print("Time to find:", totalTime)


"""

Result

The sum of the digits of 2^1000 is 1366
Time to find: 0.0

"""