# -*- coding: utf-8 -*-
"""
Project Euler

Problem 10

Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

from time import time

#Fast method using the sieve of Eratosthenes

if __name__ == '__main__':
    maxValueOfPrime = 2*10**6 - 1
    incrementToPrint = 1000
    startTime = time()
    sumOfPrimes = 0
    counter = 0
    primeValues = [True] * (maxValueOfPrime + 1)
    for aPrime in range(2,int(maxValueOfPrime**(1/2))+1):
        if primeValues[aPrime]:     #don't check if already rulled-out
            print("Found a prime:", aPrime)
            if counter == 1000:
                couner = 0
                print("aPrime:", aPrime)
            for numToElim in range(aPrime*2,maxValueOfPrime+1,aPrime):
                primeValues[numToElim] = False
        counter += 1
    for aPrime in range(2, maxValueOfPrime+1):
        if primeValues[aPrime]:
            sumOfPrimes += aPrime
    totalTime = time() - startTime
    print("The sum of all primes less than", maxValueOfPrime, "is:", sumOfPrimes)
    print("Time to find:", totalTime)
    
"""
Result - quick method:

The sum of all primes less than 1999999 is: 142913828922
Time to find: 2.053637981414795
"""


"""

The slow way
def isANewPrime(number, lowerPrimes):
    sqrtNumber = number**(1/2)
    #print("number:", number, ", sqrtNumber:", sqrtNumber)
    for oldPrime in lowerPrimes[1:]:
        if ((number % oldPrime) == 0):
            #print(number, "is not a prime. oldPrime rejected on:", oldPrime)
            return False
        if (oldPrime > sqrtNumber): #only one primefactor > sqrt
            return True
    #print(number, "is a prime")
    return True


if __name__ == '__main__':
    maxValueOfPrime = 2*10**6 - 1
    incrementToPrint = 1000
    startTime = time()
    primes = [0, 2, 3]
    k = 1       #all primes above 3 can be written as 6k +/- 1
    while True:
        #print("Primes found:", primes, ". Trying:", newTry)
        if (6*k-1 > maxValueOfPrime):
            break
        if isANewPrime(6*k-1, primes):
            primes.append(6*k-1)
            if ((len(primes) - 1) % incrementToPrint == 0):
                print(len(primes)-1, "primes found. Last prime:", 6*k-1)
        if (6*k+1 > maxValueOfPrime):
            break
        if isANewPrime(6*k+1, primes):
            primes.append(6*k+1)
            if ((len(primes) - 1) % incrementToPrint == 0):
                print(len(primes)-1, "primes found. Last prime:", 6*k-1)
        k += 1
        #if newTry > 100:
        #    break
    sumOfPrimesToLimit = 0
    for aPrime in primes:
        sumOfPrimesToLimit += aPrime
    totalTime = time() - startTime
    print("The sum of all primes less than", maxValueOfPrime, "is:", sumOfPrimesToLimit)
    print("Time to find:", totalTime)


"""
"""
Result:

The sum of all primes less than 1999999 is: 142913828922
Time to find: 2509.1645250320435

148,934 primes found
148,934th prime found is 1,999,993
"""