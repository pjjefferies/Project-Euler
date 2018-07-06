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
# from p243_Resilience_cython import fracCanBeReducedPrimeProdDen
# from p243_Resilience_cython import calcResilience
# import csv
import numpy as np
# import pandas as pd

verbose = True


def facts(n, primesList):
    """
    Adapted from Axel Brzostowski on projecteuler.net
    """
    d = 0
    fs = []
    while n > 1:
        if n % primesList[d] == 0:
            fs += [[primesList[d], 0]]
            while n % primesList[d] == 0:
                n /= primesList[d]
                fs[-1][1] += 1
        d += 1
        if d >= len(primesList) and n != 1:
            print('d:', d, '\nfs:', fs, '\nn:', n)
            raise ValueError('Please send more primes')
    return fs


def phi(n, primesList):  # Totient Functon
    fs = facts(n, primesList)
    p = 1
    for f in fs:
        p *= (f[0]-1) * f[0]**(f[1]-1)
    return p


def calcResilience(denominator,
                   primesInDenominator):
    return phi(denominator, primesInDenominator) / (denominator - 1)


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


def findSinglePrimeDenRange(maxPrimeToFind, primeList):
    minSolution = [1, 10]  # [denominator, resilience]
    for primeCountInDen in range(2, maxPrimeToFind):
        single_start_time = time()
        denominator = reduce(lambda x, y: x*y, primesList[:primeCountInDen])
        if denominator not in factorsDict:
            factorsDict[denominator] = primesList[:primeCountInDen]
        print("\nDenom:", denominator, flush=True)

        primesInDenominator = np.array(primesList[:primeCountInDen])
        print('primesInDenominator:', primesInDenominator, flush=True)

        resilience = calcResilience(denominator,
                                    primesInDenominator)

        print('New Resilience Found: Denom.:', str(denominator) +
              ', Resilience:', str(resilience) +
              ', Resilience Ratio:', str(resilience/resilience_limit) +
              ', Time to Find:', time()-single_start_time,
              flush=True)

        if resilience < minSolution[1]:
            secondBestSolution = minSolution
            minSolution = [denominator, resilience]
        print('minSolution:', minSolution, '\nsecondBestSolution:',
              secondBestSolution)
        if resilience < resilience_limit:
            return minSolution, secondBestSolution


def findMultPrimeDenRange(minSolution, secondBestSolution,
                          factorsDict, primesList):
    for denMultiplier in range(
            2, int(minSolution[0] / secondBestSolution[0]) + 1):
        mult_start_time = time()
        denominator = secondBestSolution[0] * denMultiplier
        factorsDict[denominator] = (factorsDict[minSolution[0]] +
                                    [denMultiplier])
        with suppress(ValueError):
            factorsDict[denominator].remove(1)
        print("\nDenom:", denominator, flush=True)

        primesInDenominator = np.array(factorsDict[secondBestSolution[0]])
        print('primesInDenominator:', primesInDenominator, flush=True)

        resilience = calcResilience(denominator,
                                    primesInDenominator)

        print('New Resilience Found: Denom.:', str(denominator) +
              ', Resilience:', str(resilience) +
              ', Resilience Ratio:', str(resilience/resilience_limit) +
              ', Time to Find:', time()-mult_start_time,
              flush=True)

        if resilience < resilience_limit:
            return denominator, resilience


if __name__ == '__main__':
    startTime = time()
    print("\n\n")

    maxDenom = int(1e8)
    resilience_limit = 15499/94744     # 0.1635881955585578

    maxPrimeToFind = 30
    # maxPrimeToFind = 6469693230
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

Denom: 6
primesInDenominator: [2 3]
New Resilience Found: Denom.: 6, Resilience: 0.4,
Resilience Ratio: 2.445164204142203, Time to Find: 0.018001794815063477
minSolution: [6, 0.4]
secondBestSolution: [1, 10]

Denom: 30
primesInDenominator: [2 3 5]
New Resilience Found: Denom.: 30, Resilience: 0.27586206896551724,
Resilience Ratio: 1.686320140787726, Time to Find: 0.01700139045715332
minSolution: [30, 0.27586206896551724]
secondBestSolution: [6, 0.4]

Denom: 210
primesInDenominator: [2 3 5 7]
New Resilience Found: Denom.: 210, Resilience: 0.22966507177033493,
Resilience Ratio: 1.4039220310864322, Time to Find: 0.013000726699829102
minSolution: [210, 0.22966507177033493]
secondBestSolution: [30, 0.27586206896551724]

Denom: 2310
primesInDenominator: [ 2  3  5  7 11]
New Resilience Found: Denom.: 2310, Resilience: 0.2078822000866176,
Resilience Ratio: 1.2707652858253111, Time to Find: 0.0189971923828125
minSolution: [2310, 0.2078822000866176]
secondBestSolution: [210, 0.22966507177033493]

Denom: 30030
primesInDenominator: [ 2  3  5  7 11 13]
New Resilience Found: Denom.: 30030, Resilience: 0.19181457924006792,
Resilience Ratio: 1.1725453574760303, Time to Find: 0.11900472640991211
minSolution: [30030, 0.19181457924006792]
secondBestSolution: [2310, 0.2078822000866176]

Denom: 510510
primesInDenominator: [ 2  3  5  7 11 13 17]
New Resilience Found: Denom.: 510510, Resilience: 0.18052571061430847,
Resilience Ratio: 1.103537513803603, Time to Find: 1.5990898609161377
minSolution: [510510, 0.18052571061430847]
secondBestSolution: [30030, 0.19181457924006792]

Denom: 9699690
primesInDenominator: [ 2  3  5  7 11 13 17 19]
New Resilience Found: Denom.: 9699690, Resilience: 0.1710240400491191,
Resilience Ratio: 1.0454546519397214, Time to Find: 30.088719367980957
minSolution: [9699690, 0.1710240400491191]
secondBestSolution: [510510, 0.18052571061430847]

Denom: 223092870
primesInDenominator: [ 2  3  5  7 11 13 17 19 23]
New Resilience Found: Denom.: 223092870, Resilience: 0.16358819608886738,
Resilience Ratio: 1.0000000032417349, Time to Find: 701.7691841125488
minSolution: [223092870, 0.16358819608886738]
secondBestSolution: [9699690, 0.1710240400491191]

Denom: 6469693230
primesInDenominator: [ 2  3  5  7 11 13 17 19 23 29]
New Resilience Found: Denom.: 6469693230, Resilience: 0.15794722312636564,
Resilience Ratio: 0.9655172403306268, Time to Find: 20738.704892396927
minSolution: [6469693230, 0.15794722312636564]
secondBestSolution: [223092870, 0.16358819608886738]

Denom: 446185740
primesInDenominator: [ 2  3  5  7 11 13 17 19 23]
New Resilience Found: Denom.: 446185740, Resilience: 0.16358819572223038,
Resilience Ratio: 1.000000001000516, Time to Find: 1398.0950620174408

Denom: 669278610
primesInDenominator: [ 2  3  5  7 11 13 17 19 23]
New Resilience Found: Denom.: 669278610, Resilience: 0.16358819560001805,
Resilience Ratio: 1.0000000002534428, Time to Find: 2074.6608078479767

Denom: 892371480
primesInDenominator: [ 2  3  5  7 11 13 17 19 23]
New Resilience Found: Denom.: 892371480, Resilience: 0.16358819553891188,
Resilience Ratio: 0.9999999998799062, Time to Find: 2779.266157388687
Denominator: 892371480 , Resilience: 0.16358819553891188

Time to find: 27,724.499 s = 462.075 m = 7.7 h

Time to find using Totient Function: 0.290 s

"""
