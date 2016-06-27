# -*- coding: utf-8 -*-
"""
Project Euler

Problem 23: Non-abundant sums

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers is
less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.

"""

from time import time

def findFactorsBruteForce(aNum):
    factors = set()
    maxToTry = int(aNum ** (1.0/2.0))
    for numToTry in range(1, maxToTry + 1):
        if aNum % numToTry == 0:
            factors.add(numToTry)
            factors.add(int(aNum / numToTry))
    factors.discard(aNum)
    return factors


if __name__ == '__main__':
    startTime = time()

    maxLimitToTry = 28123
    abundantNums = []
    
    for aNum in range(1, maxLimitToTry +1):         #Find abundant nums -> list
        aNumFactors = findFactorsBruteForce(aNum)
        aNumFactorSum = 0
        for aFactor in aNumFactors:
            aNumFactorSum += aFactor
        if aNumFactorSum > aNum:
            abundantNums.append(aNum)
    print(len(abundantNums), "abundant numbers less than", maxLimitToTry)
            
    
    nonAbundantSumList = [True] * (maxLimitToTry + 1)
    #"""
    maxLimitToTryHalf = int(maxLimitToTry / 2)
    for anAbundantNo1 in abundantNums:
        if anAbundantNo1 % 1000 == 0:
            print("anAbundantNo1:", anAbundantNo1)
        if anAbundantNo1 > maxLimitToTryHalf:
            break
        for anAbundantNo2 in abundantNums:
            aPotNonAbundantSum = anAbundantNo1 + anAbundantNo2
            if aPotNonAbundantSum > maxLimitToTry:
                break
            nonAbundantSumList[aPotNonAbundantSum] = False
    """
    for aNum in range(maxLimitToTry + 1):
        if aNum % 1000 == 0:
            print("aNum:", aNum)
        aNumHalf = int(aNum / 2) + 1
        for anAbundantNo in abundantNums:
            if anAbundantNo > aNumHalf:
                #print("Out of range, next")
                break
            if ((aNum - anAbundantNo) in abundantNums):
                #print("found one:", aNum)
                nonAbundantSumList[aNum] = False
                break
    """
    nonAbundantSums = []
    nonAbundantSumsSum = 0
    for aNum in range(1,len(nonAbundantSumList)):
        if nonAbundantSumList[aNum]:
            nonAbundantSums.append(aNum)
            nonAbundantSumsSum += aNum

    totalTime = time() - startTime
    print("The total of all of the positive integers which cannot be written",
          "as the sum of two abundant numbers is", nonAbundantSumsSum)
    #print("The values are:", nonAbundantSums)
    print("Time to find:", totalTime)

"""

Result

The total of all of the positive integers which cannot be written as the sum of
two abundant numbers is 4179871
Time to find: 15.774901151657104

"""
