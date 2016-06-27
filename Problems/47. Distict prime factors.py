# -*- coding: utf-8 -*-
"""
Project Euler

Problem 47: distinct primes factors

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors.
What is the first of these numbers?

Analysis

"""


from time import time


def findPrimes(maxValueOfPrime):   #Sieve of Eratosthenes
    primes = []
    maxValueOfPrime = int(maxValueOfPrime)
    counter = 0
    primeValues = [True] * (maxValueOfPrime + 1)
    for aPrime in range(2,int(maxValueOfPrime**(1/2))+1):
        if primeValues[aPrime]:     #don't check if already rulled-out
            #print("Found a prime:", aPrime)
            if counter == 1000:
                counter = 0
                print("aPrime:", aPrime)
            for numToElim in range(aPrime*2,maxValueOfPrime+1,aPrime):
                primeValues[numToElim] = False
        counter += 1
    for aPrimeNo in range(2,len(primeValues)):
        if primeValues[aPrimeNo]:
            primes.append(aPrimeNo)
    return primes


def findPrimeFactors(aNumber, primesDict):      
    allFactors = findAllFactors(aNumber)
    primeFactors = []
    for aFactor in allFactors:
        if aFactor in primesDict:
            primeFactors.append(aFactor)
    return primeFactors


def findAllFactors(number):
    listOfFactors = set([number])
    testFactor = 2
    maxSingleFactorLimit = number**(0.5) + 1
    while testFactor < maxSingleFactorLimit:
        if number % testFactor == 0:
            listOfFactors.add(testFactor)
            listOfFactors.add(int(number/testFactor))
        testFactor += 1
    return listOfFactors


def findFactorExponents(aNumber, factors):
    aNumberReduced = aNumber
    factorAndExpon = []
    for aFactor in factors:
        expTry = 1
        while aNumberReduced % (aFactor ** expTry) == 0:
            expTry += 1
        factorAndExpon.append([aFactor, expTry-1])
    return factorAndExpon

if __name__ == '__main__':
    startTime = time()
    print("\n\n\n")

    maxPrimeToFind = int(2e5)
    primes = findPrimes(maxPrimeToFind)
    primeDict = {}
    for aPrime in primes:
        primeDict[aPrime] = True
        
    aStartNo = 643

    primeFactAndExpDict = {}
    for aNum in range(aStartNo, maxPrimeToFind):
        factorsTemp = findPrimeFactors(aNum, primeDict)
        primeFactAndExpDict[aNum] = findFactorExponents(aNum, factorsTemp)

    print("List and Dict populated with primes through", maxPrimeToFind)

    fourMemberSeqStart = []

    while True:
        aStartNo += 1
        if ((len(primeFactAndExpDict[aStartNo]) == 4) and
            (len(primeFactAndExpDict[aStartNo+1]) == 4) and
            (len(primeFactAndExpDict[aStartNo+2]) == 4) and
            (len(primeFactAndExpDict[aStartNo+3]) == 4)):
            fourMemberSeqStart.append(aStartNo)
            solFound = True
            for aFactorExpNo1 in primeFactAndExpDict[aStartNo]:
                for aFactorExpNo2 in primeFactAndExpDict[aStartNo+1]:
                    if aFactorExpNo1 == aFactorExpNo2:
                        solFound = False
                        break
                if not solFound:
                    break
                for aFactorExpNo3 in primeFactAndExpDict[aStartNo+2]:
                    if aFactorExpNo1 == aFactorExpNo3:
                        solFound = False
                        break
                if not solFound:
                    break
                for aFactorExpNo4 in primeFactAndExpDict[aStartNo+3]:
                    if aFactorExpNo1 == aFactorExpNo4:
                        solFound = False
                        break
                if not solFound:
                    break
            if not solFound:
                continue
            for aFactorExpNo2 in primeFactAndExpDict[aStartNo+1]:
                for aFactorExpNo3 in primeFactAndExpDict[aStartNo+2]:
                    if aFactorExpNo2 == aFactorExpNo3:
                        solFound = False
                        break
                if not solFound:
                    break
                for aFactorExpNo4 in primeFactAndExpDict[aStartNo+3]:
                    if aFactorExpNo2 == aFactorExpNo4:
                        solFound = False
                        break
            if not solFound:
                continue
            for aFactorExpNo3 in primeFactAndExpDict[aStartNo+2]:
                for aFactorExpNo4 in primeFactAndExpDict[aStartNo+3]:
                    if aFactorExpNo3 == aFactorExpNo4:
                        solFound = False
                        break
                if not solFound:
                    break
            if not solFound:
                continue
            #Solution Found, yea!
            break
                


    totalTime = time() - startTime
    print("\n\nThe first four consecutive integers to have four distinct"
          "prime factors are:", aStartNo, aStartNo+1, aStartNo+2, aStartNo+3)
    print("\nThe factors of them are:")
    print("  ", str(aStartNo)+":", primeFactAndExpDict[aStartNo])
    print("  ", str(aStartNo+1)+":", primeFactAndExpDict[aStartNo+1])
    print("  ", str(aStartNo+2)+":", primeFactAndExpDict[aStartNo+2])
    print("  ", str(aStartNo+3)+":", primeFactAndExpDict[aStartNo+3])
    print("No of four mem seq.:", fourMemberSeqStart)
    print("Time to find:", '{:,.3f}'.format(totalTime))

"""
Result:

The first four consecutive integers to have four distinctprime factors are: 134043 134044 134045 134046

The factors of them are:
   134043: [[3, 1], [7, 1], [491, 1], [13, 1]]
   134044: [[2, 2], [23, 1], [31, 1], [47, 1]]
   134045: [[5, 1], [17, 1], [19, 1], [83, 1]]
   134046: [[2, 1], [3, 2], [11, 1], [677, 1]]
No of four mem seq.: [134043]
Time to find: 37.521

"""
