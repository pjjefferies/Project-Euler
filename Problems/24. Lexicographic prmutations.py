# -*- coding: utf-8 -*-
"""
Project Euler

Problem 24: Lexicographic permutations

A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
6, 7, 8 and 9?

"""

from time import time
from math import factorial

if __name__ == '__main__':
    startTime = time()

    strToPerm = "0123456789"
    lenStrToPerm = len(strToPerm)
    solutionStr = ""
    permNoToFind = 1e6
    digitPosFound = []
    remainingStr = strToPerm[:]
    
    for aCharNo in range(len(strToPerm)):
        noPermSoFar = 1
        for aDigit in range(aCharNo):
            noPermSoFar += (factorial(lenStrToPerm - aDigit - 1)
                            * digitPosFound[aDigit])
        remainder = permNoToFind - noPermSoFar
        nextDigitNo = int((permNoToFind - noPermSoFar)
                          / factorial(lenStrToPerm - aCharNo - 1))
        solutionStr += remainingStr[nextDigitNo]
        digitPosFound.append(nextDigitNo)
        remainingStr = (remainingStr[:nextDigitNo]
                        + remainingStr[(nextDigitNo+1):])
        #print("aCharNo:", aCharNo, ", nextDigitNo:", nextDigitNo,
        #      ", solutinoStr:", solutionStr, ", remainingStr:", remainingStr,
        #      ", remainder:", remainder)
              

    totalTime = time() - startTime
    print("The", str(permNoToFind)+"th permutation of", strToPerm, "is",
          solutionStr)
    print("Time to find:", totalTime)

"""

Result

The 1000000.0th permutation of 0123456789 is 2783915460
Time to find: 0.0

"""
