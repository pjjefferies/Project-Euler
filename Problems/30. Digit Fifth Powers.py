# -*- coding: utf-8 -*-
"""
Project Euler

Problem 30: Digit fifth powers

Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.

"""

from time import time


if __name__ == '__main__':
    startTime = time()
    powToUse = 5
    listOfNumbers = []
    fifthPow = {}
    for i in range(10):
        fifthPow[str(i)] = i ** 5

    for aNum in range(1000, 1000000):
        aNumString = str(aNum)
        aTempNum = 0
        for aChar in aNumString:
            aTempNum += fifthPow[aChar]
        if aNum == aTempNum:
            listOfNumbers.append(aNum)
    
    sumOfDigits = 0
    for aNum in listOfNumbers:
        sumOfDigits += aNum
    
    totalTime = time() - startTime
    print("The sum of all the numbers that can be written as the sum of fifth",
          "powers of their digits is", sumOfDigits, ". The numbers are:",
          listOfNumbers)
    print("Time to find:", totalTime)


"""
Result:

The sum of all the numbers that can be written as the sum of fifth powers of
their digits is 443839 . The numbers are: [4150, 4151, 54748, 92727, 93084,
194979]
Time to find: 3.055577993392944

"""