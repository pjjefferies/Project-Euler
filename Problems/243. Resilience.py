# -*- coding: utf-8 -*-
"""
Project Euler

Problem 243: Resilience

A positive fraction whose numerator is less than its denominator is called a
proper fraction.
For any denominator, d, there will be d−1 proper fractions; for example,
with d = 12:
1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 , 7/12 , 8/12 , 9/12 , 10/12 , 11/12 .

We shall call a fraction that cannot be cancelled down a resilient fraction.
Furthermore we shall define the resilience of a denominator, R(d), to be the
ratio of its proper fractions that are resilient; for example, R(12) = 4/11 .
In fact, d = 12 is the smallest denominator having a resilience R(d) < 4/10 .

Find the smallest denominator d, having a resilience R(d) < 15499/94744 .
"""

from time import time
from functools import reduce
from contextlib import suppress
# import csv
# import pandas as pd

verbose = True


def findPrimes(maxValueOfPrime):   # Sieve of Eratosthenes
    maxValueOfPrime = int(maxValueOfPrime)
    counter = 0
    dispIncr = maxValueOfPrime / 10
    primeValues = [True] * (maxValueOfPrime + 1)

    for numToElim in range(4, maxValueOfPrime+1, 2):
        primeValues[numToElim] = False

    for aPrime in range(3, maxValueOfPrime+1, 2):
        if primeValues[aPrime]:     # don't check if already rulled-out
            if counter >= dispIncr:
                counter = 0
                print("aPrime:", aPrime, "of", maxValueOfPrime)
            for numToElim in range(aPrime*2, maxValueOfPrime+1, aPrime):
                primeValues[numToElim] = False
        counter += 1
    primes = [aPrimeNo for aPrimeNo in range(2, len(primeValues))
              if primeValues[aPrimeNo]]
    return primes


"""
def findPrimeFactors(number, primesList):
    listOfFactors = []
    reducedNumber = number
    # maxSingleFactorLimit = int(number**(0.5)) + 1
    maxSingleFactorLimit = int(number) + 1
    for aPrime in primesList:
        # print("aPrime:", aPrime, ", maxSingleFactorLimit:",
        # maxSingleFactorLimit)
        if aPrime > maxSingleFactorLimit:
            break
        if reducedNumber % aPrime == 0:
            listOfFactors.append(aPrime)
            # listOfFactors.add(aPrime)
            reducedNumber = int(reducedNumber / aPrime)
            # listOfFactors.add(reducedNumber)
            if reducedNumber in primesList:
                listOfFactors.append(reducedNumber)
                break
            # print("listOfFactors after adding", aPrime, ":", listOfFactors,
            # "in", number)
    listOfFactors.sort()
    # listOfFactors.discard(1)
    if 1 in listOfFactors:
        listOfFactors = listOfFactors[1:]
    # listOfFactors = list(listOfFactors)
    # listOfFactors.sort()
    return listOfFactors


def findAllPrimeFactors(maxNumber, primesList):
    factorsDict = {}
    dispIncr = maxNumber / 10
    for i in range(1, maxNumber+1):
        if (i % dispIncr == 0):
            print("Finding factor of", i, "out of", maxNumber)
        factorsDict[i] = findPrimeFactors(i, primesList)
    return factorsDict


def fracCanBeReduced(numerator, denominator, factorsDict, primesList):
    if numerator not in factorsDict:
        factorsDict[numerator] = findPrimeFactors(numerator, primesList)
    numFacts = factorsDict[numerator]
    for factor in factorsDict[denominator]:
        if factor in numFacts:
            return True
    return False
"""

def fracCanBeReducedPrimeProdDen(int aNum, int[:] ShortPrimesList):
    cdef int aPrime
    for aPrime in ShortPrimesList:
        if aNum % aPrime == 0:
            return True
    return False


def calcResilience(int denominator, int[:] primesInDenominator):
    cdef int resiliantFractionCount = 0
    cdef int numerator
    cdef double resilience

    for numerator in range(1, denominator):
        if not(fracCanBeReducedPrimeProdDen(numerator,
                                            primesInDenominator)):
            resiliantFractionCount += 1
    resilience = float(resiliantFractionCount) / float(denominator-1)
    return resilience


def findSinglePrimeDenRange(maxPrimeToFind, primeList):
    minSolution = [1, 0]
    for primeCountInDen in range(2, maxPrimeToFind):
        denominator = reduce(lambda x, y: x*y, primesList[:primeCountInDen])
        if denominator not in factorsDict:
            factorsDict[denominator] = primesList[:primeCountInDen]
        print("Denom:", denominator, flush=True)

        primesInDenominator = primesList[:primeCountInDen]
        resilience = calcResilience(denominator, primesInDenominator)

        print('New Resilience Found: Denom.:', str(denominator) +
              ', Resilience:', str(resilience) +
              ', Resilience Ratio:', resilience/resilience_limit,
              flush=True)

        if resilience < minSolution[1]:
            secondBestSolution = minSolution
            minSolution = [denominator, resilience]
        if resilience < resilience_limit:
            return minSolution, secondBestSolution


def findMultPrimeDenRange(minSolution, secondBestSolution,
                          factorsDict, primesList):
    for denMultiplier in range(
            2, int(minSolution[0] / secondBestSolution[0]) + 1):
        denominator = secondBestSolution[0] * denMultiplier
        factorsDict[denominator] = (factorsDict[minSolution[0]] +
                                    [denMultiplier])
        with suppress(ValueError):
            factorsDict[denominator].remove(1)
        print("Denom:", denominator, flush=True)

        primesInDenominator = factorsDict[secondBestSolution[0]]
        resilience = calcResilience(denominator, primesInDenominator)

        print('New Resilience Found: Denom.:', str(denominator) +
              ', Resilience:', str(resilience) +
              ', Resilience Ratio:', resilience/resilience_limit,
              flush=True)

        if resilience < resilience_limit:
            return denominator, resilience


if __name__ == '__main__':
    startTime = time()
    print("\n\n")

    maxDenom = int(1e8)
    resilience_limit = 15499/94744     # 0.1635881955585578

    maxPrimeToFind = 100
    primesList = findPrimes(maxPrimeToFind)
    print("Found", len(primesList), "primes between 2 and", maxPrimeToFind,
          "\n\n")

    factorsDict = {}
    bestSolFoundList = []
    dispIncr = int(maxDenom / 100)

    minSolution, secondBestSolution = findSinglePrimeDenRange(maxPrimeToFind,
                                                              primesList)

    denominator, resilience = findMultPrimeDenRange(
        minSolution, secondBestSolution, factorsDict, primesList)

    totalTime = time() - startTime
    print("Denominator:", denominator, ", Resilience:", resilience
          # fractionCount, "\n",
          # "Fraction List:", fracList
          )
    print("Time to find:", '{:,.3f}'.format(totalTime))

"""
Result:


Time to find: 0.664

"""
