# -*- coding: utf-8 -*-
"""
Project Euler

Problem 34: Digit factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

"""

"""

Analysis

What is max?

X: max = 9! = 362,880
...
X,XXX,XXX: max = 7 x 9! = 2,540,160 - OK - this is max value
XX,XXX,XXX: max = 8x9! = 2,903,040 - NG


"""

from time import time
from math import factorial


if __name__ == '__main__':
    startTime = time()
    print("\n\n\n")

    solutions = []
    for aNum in range(10,2540160+1):
        aNumFactSum = 0
        for aDigit in str(aNum):
            aNumFactSum += factorial(int(aDigit))
            if aNumFactSum == aNum:
                solutions.append(aNum)

    solutionsSum = sum(solutions)

    totalTime = time() - startTime
    print("\n\nThe sum of all numbers which are equal to the sum of the",
          "factorial of their digits is", str(solutionsSum)+". The numbers",
          "are", solutions)
    print("Time to find:", '{:,.3f}'.format(totalTime))


"""
Result:

The sum of all numbers which are equal to the sum of the factorial of their
digits is 40730. The numbers are [145, 40585]
Time to find: 19.983

"""