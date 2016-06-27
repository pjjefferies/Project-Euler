# -*- coding: utf-8 -*-
"""
Project Euler

Problem 41: Pandigital prime

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?


Analysis



"""

from time import time


def isPanDigital(aNumber):
    aNumStr = str(aNumber)
    aNumStrCopy = aNumStr[:]
    for aCharNo in range(1,len(aNumStr)+1):
        aNumStrCopy = aNumStrCopy.replace(str(aCharNo), "")
        #print("aNumStrCopy:", aNumStrCopy, len(aNumStrCopy), len(aNumStr), aCharNo)
        if len(aNumStrCopy) != len(aNumStr) - aCharNo:
            #print("return False")
            return False
    if aNumStrCopy != "":
        #print("return False 2")
        return False
    #print("Return True")
    return True


def findPandigitalPrimes(maxValueOfPrime, primes=None):   #Sieve of Eratosthenes
    if primes == None:
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
            if isPanDigital(aPrimeNo):
                primes.append(aPrimeNo)
    return primes


if __name__ == '__main__':
    startTime = time()
    print("\n\n\n")

    maxPrimeToFind = 1e9
    primes = findPandigitalPrimes(maxPrimeToFind)
    print("Primes found up to", maxPrimeToFind)
    
    totalTime = time() - startTime
    print("\n\nThe largest n-digit pandigital prime is", str(max(primes))+".")
    print("Time to find:", '{:,.3f}'.format(totalTime))

"""
Result:

The largest n-digit pandigital prime is 7652413.
Time to find: 8.127

"""
