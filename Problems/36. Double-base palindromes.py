# -*- coding: utf-8 -*-
"""
Project Euler

Problem 36: Double-base palindromes

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)

"""

"""

Analysis

binary palindromes must be odd if no leading zeros

palindromes can be gerated from xyz -> xyzzyx and/or xyzyx

To get to 1,000,000 (7 digits), evaluate up to abc -> ab,cba and abc,cba
which covers up to 999,999


"""

from time import time

def isAPalindrome(aString):
    aString = str(aString)[:]
    while len(aString) > 1:
        if aString[0] != aString[-1]:
            return False
        aString = aString[1:-1]
    return True


if __name__ == '__main__':
    startTime = time()
    print("\n\n\n")
    doublePalindromeList = []
    maxNumToEval = int(1e6 - 1)
    maxNumHalfToEval = 999
    
    for aNumHalf in range(1, maxNumHalfToEval+1):
        aNumHalfStr = str(aNumHalf)
        if int(aNumHalfStr[0]) % 2 == 0:
            continue
        #First option
        aNum = int(aNumHalfStr[:-1] + aNumHalfStr[::-1])
        if isAPalindrome(aNum):
            aNumBin = bin(aNum)[2:]
            #print("Found a decimal palindrom:", aNum, aNumBin)
            if isAPalindrome(aNumBin):
                doublePalindromeList.append((aNum, aNumBin))
        #Second Option
        aNum = int(aNumHalfStr[:] + aNumHalfStr[::-1])
        if isAPalindrome(aNum):
            aNumBin = bin(aNum)[2:]
            #print("Found a decimal palindrom:", aNum, aNumBin)
            if isAPalindrome(aNumBin):
                doublePalindromeList.append((aNum, aNumBin))

    
    doublePalindromeSum = 0
    for aPalindromePair in doublePalindromeList:
        doublePalindromeSum += aPalindromePair[0]


    totalTime = time() - startTime
    print("\n\nThe sum of all double-base palindromes less than 1,000,000 is",
          doublePalindromeSum, ". They are as follows:\n", doublePalindromeList)
    print("Time to find:", '{:,.3f}'.format(totalTime))


"""
Result:

The sum of all double-base palindromes less than 1,000,000 is 872187 . They are
as follows: [(1, '1'), (3, '11'), (33, '100001'), (5, '101'), (7, '111'),
(9, '1001'), (99, '1100011'), (313, '100111001'), (585, '1001001001'),
(717, '1011001101'), (7447, '1110100010111'), (9009, '10001100110001'),
(15351, '11101111110111'), (32223, '111110111011111'),
(39993, '1001110000111001'), (53235, '1100111111110011'),
(53835, '1101001001001011'), (585585, '10001110111101110001'),
(73737, '10010000000001001')]

Time to find: 0.012

"""