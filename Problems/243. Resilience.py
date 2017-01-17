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
#import csv
#import pandas as pd

verbose = True

def findPrimes(maxValueOfPrime):   #Sieve of Eratosthenes
    primes = []
    maxValueOfPrime = int(maxValueOfPrime)
    counter = 0
    dispIncr = maxValueOfPrime / 10
    primeValues = [True] * (maxValueOfPrime + 1)
    for numToElim in range(4, maxValueOfPrime+1, 2):
        primeValues[numToElim] = False
    for aPrime in range(3, maxValueOfPrime+1, 2):
        if primeValues[aPrime]:     #don't check if already rulled-out
            if counter >= dispIncr:
                counter = 0
                print("aPrime:", aPrime, "of", maxValueOfPrime)
            for numToElim in range(aPrime*2, maxValueOfPrime+1, aPrime):
                primeValues[numToElim] = False
        counter += 1
    for aPrimeNo in range(2,len(primeValues)):
        if primeValues[aPrimeNo]:
            primes.append(aPrimeNo)
    return primes


def findFactors(number, primesList):
    listOfFactors = set([])
    maxSingleFactorLimit = int(number**(0.5)) + 1
    for aPrime in primesList:
        #print("aPrime:", aPrime, ", maxSingleFactorLimit:", maxSingleFactorLimit)
        if aPrime > maxSingleFactorLimit:
            break
        if number % aPrime == 0:
            listOfFactors.add(aPrime)
            listOfFactors.add(int(number/aPrime))
            #print("listOfFactors after adding", aPrime, ":", listOfFactors, "in", number)
    listOfFactors.discard(1)
    listOfFactors = list(listOfFactors)
    listOfFactors.sort()
    return listOfFactors


def findAllPrimeFactors(maxNumber, primesList):
    factorsDict = {}
    dispIncr = maxNumber / 10
    for i in range(1, maxNumber+1):
        if (i % dispIncr == 0):
            print("Finding factor of", i, "out of", maxNumber)
        factorsDict[i] = findFactors(i, primesList)
    return factorsDict


def fracCanBeReduced(numerator, denominator, factorsDict):
    numFacts = factorsDict[numerator]
    for factor in factorsDict[denominator]:
        if factor in numFacts:
            return True
    return False


if __name__ == '__main__':
    startTime = time()
    print("\n\n")

    maxDenom = int(1e7)
    resilience_limit = 15499/94744     #0.1635881955585578
    
    maxPrimeToFind = maxDenom
    primesList = findPrimes(maxPrimeToFind)
    print("Found", len(primesList), "primes between 2 and", maxPrimeToFind, "\n\n")
    """
    primesDict = {}
    for aPrime in primes:
        primesDict[aPrime] = True    
    """

    factorsDict = findAllPrimeFactors(maxDenom, primesList)
    minSolution = [1, 0]
    bestSolFoundList = []
    dispIncr = int(maxDenom / 100)
    
    for denominator in range(13, maxDenom+1):
        if denominator % dispIncr == 0:
            print("Denom:", denominator)
        fracList = []
        fractionCount = 0
        fractionCountMax = int(resilience_limit * denominator)+1
        nextDenom = False
        for numerator in range(1, denominator):
            if not(fracCanBeReduced(numerator, denominator, factorsDict)):
                fractionCount += 1
                if fractionCount >= fractionCountMax:
                    nextDenom = True
                    break
                fracList.append(str(numerator)+"/"+str(denominator))
        if nextDenom:
            continue
        resilience = float(fractionCount) / float(denominator)
        if resilience < minSolution[0]:
            minSolution = [resilience, denominator]
            bestSolFoundList.append([denominator, resilience, fracList,
                                    resilience/resilience_limit])
            print("New Min resilience found:", bestSolFoundList[-1][0], ", ",
                  bestSolFoundList[-1][1], len(bestSolFoundList[-1][2]),
                  bestSolFoundList[-1][3])
        if resilience < resilience_limit:
            break
        #else:
        #    break
    
    if nextDenom and denominator == maxDenom:
        print("Solution not found up to denominator", maxDenom)
                
    

    
    totalTime = time() - startTime
    print("Denominator:", denominator, ", Resilience:", fractionCount, "\n",
          "Fraction List:", fracList)
    print("Time to find:", '{:,.3f}'.format(totalTime))

"""
Result:


Time to find: 0.664

"""
