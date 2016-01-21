# -*- coding: utf-8 -*-
"""
Project Euler

Problem 20: Factorial digit sum

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!


"""

from time import time
from math import factorial

if __name__ == '__main__':
    startTime = time()
    print("\n\n")

    n = factorial(100)
    nString = str(n)
    nStringDigitSum = 0
    for aDigit in nString:
        nStringDigitSum += int(aDigit)

    totalTime = time() - startTime
    print("The sum of the digits in 100! is", nStringDigitSum)
    print("Time to find:", totalTime)


"""
One-line version

reduce(lambda x, y: x + y, [int(i) for i in str(reduce(lambda x, y: x * y, range(1, 100)))])

"""


"""

Result

The sum of the digits in 100! is 648
Time to find: 0.0

"""