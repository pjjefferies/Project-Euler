# -*- coding: utf-8 -*-
"""
Project Euler

Problem 35: Circular primes

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?

"""

"""

Analysis



"""

from time import time


def isANewPrime(number, lowerPrimes):
    sqrtNumber = number**(0.5)
    #print("number:", number, ", sqrtNumber:", sqrtNumber)
    for oldPrime in lowerPrimes[1:]:
        if ((number % oldPrime) == 0):
           #print(number, "is not a prime. oldPrime rejected on:", oldPrime)
            return False
        if (oldPrime > sqrtNumber): #only one primefactor > sqrt
            return True
            #print(number, "is a prime")
    return True


def isAPrime(number, primes):
    if number > max(primes):
        print("isAPrime Inconclusive")
        return False
    if number in primes:
        return True
    return False

#Fast method using the sieve of Eratosthenes

def findPrimes(maxValueOfPrime, primes=None):
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
            primes.append(aPrimeNo)
    return primes


""" Slow way but useful if finding number of primes and don't know max
def findPrimes(maxNum, primes=None):
    if primes == None:
        primes = [2, 3]
    k = 1       #all primes above 3 can be written as 6k +/- 1
    while True:
        potentialPrime = 6*k-1
        if potentialPrime > maxNum:
            return primes
        if isANewPrime(potentialPrime, primes):
            primes.append(potentialPrime)
        potentialPrime = 6*k+1
        if potentialPrime > maxNum:
            return primes
        if isANewPrime(potentialPrime, primes):
            print("In findPrimes, Found a prime", potentialPrime)
            primes.append(potentialPrime)
        k += 1
"""

def generateCircularValues(aNum):
    circularNumbers = [aNum]
    aNumStr = str(aNum)
    aNumLen = len(str(aNum))    
    for aCharNo in range(aNumLen):
        aNumStr = aNumStr[1:] + aNumStr[0]
        circularNumbers.append(int(aNumStr))
    return circularNumbers

def isAListOfPrimes(listOfNums, primes):
    for aNum in listOfNums:
        if aNum not in primes:
            return False
    return True


if __name__ == '__main__':
    startTime = time()
    print("\n\n\n")
    incrementToPrint = 1000
    counter = 0
    circularPrimes = []

    listOfPrimes = findPrimes(int(1e6-1))
    print(len(listOfPrimes), "primes up to 1e6-1 found.")
    for aPrime in listOfPrimes:
        counter += 1
        if counter % incrementToPrint == 0:
            print("Evaluating prime no", counter, "of", str(len(listOfPrimes))+":", aPrime)
        #print("Trying Prime:", aPrime)
        circularNumbers = generateCircularValues(aPrime)
        foundACircularPrime = isAListOfPrimes(circularNumbers, listOfPrimes)
        if foundACircularPrime:
            print("Found one:", aPrime)
            circularPrimes.append(aPrime)

    totalTime = time() - startTime
    print("\n\nThere are", len(circularPrimes), ". List:", circularPrimes)
    print("Time to find:", '{:,.3f}'.format(totalTime))


"""
Result:

There are 55 . List: [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131,
197, 199, 311, 337, 373, 719, 733, 919, 971, 991, 1193, 1931, 3119, 3779, 7793,
7937, 9311, 9377, 11939, 19391, 19937, 37199, 39119, 71993, 91193, 93719,
93911, 99371, 193939, 199933, 319993, 331999, 391939, 393919, 919393, 933199,
939193, 939391, 993319, 999331]
Time to find: 429.370

"""