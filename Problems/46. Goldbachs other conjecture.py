# -*- coding: utf-8 -*-
"""
Project Euler

Problem 46: Goldbach's other conjecture

It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?

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



if __name__ == '__main__':
    startTime = time()
    print("\n\n\n")

    maxPrimeToFind = 1e6
    primes = findPrimes(maxPrimeToFind)
    primeDict = {}
    for aPrime in primes:
        primeDict[aPrime] = True
        
    print("List and Dict populated with primes through", maxPrimeToFind)

    aNum = 9
    foundOneFlag = False
    nextNumFlag = False
    while not foundOneFlag:
        if (aNum - 1) % 1000 == 0:
            print("aNum:", aNum, flush=True)
        for aPrime in primes:
            #print("aNum:", aNum, ", aPrime:", aPrime)
            if aNum in primeDict:
                nextNumFlag = True
                break
            if aPrime > aNum:
                foundOneFlag = True
                break
            aNumPrimeHalfRem = (aNum - aPrime) / 2
            if round(aNumPrimeHalfRem % 1, 6) != 0:
                continue
            #print("aNum:", aNum, ", aPrime:", aPrime, ", aNumPrimeHalfRem:",
            #      aNumPrimeHalfRem)
            if round((aNumPrimeHalfRem ** 0.5) % 1,6) == 0:
                foundOneFlag = False
                nextNumFlag = True
                break
        if nextNumFlag:
            aNum += 2
            nextNumFlag = False
            continue


    totalTime = time() - startTime
    print("\n\nThe smallest odd composite that cannot be written as the sum",
          "of a prime and twice a square is", aNum)
    print("Time to find:", '{:,.3f}'.format(totalTime))

"""
Result:

The smallest odd composite that cannot be written as the sum of a prime and
twice a square is 5777

Time to find: 1.354

"""
