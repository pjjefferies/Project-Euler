# -*- coding: utf-8 -*-
"""
Project Euler

Problem 7 - 10,001st Prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

from math import sqrt

from time import time

def isANewPrime(number, lowerPrimes):
    sqrtNumber = sqrt(number)
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
    nthPrimeToFind = 10001
    incrementToPrint = 1000
    startTime = time()
    primes = [1, 2, 3]
    k = 1       #all primes above 3 can be written as 6k +/- 1
    while True:
        #print("Primes found:", primes, ". Trying:", newTry)
        if isANewPrime(6*k-1, primes):
            primes.append(6*k-1)
            if ((len(primes) - 1) % incrementToPrint == 0):
                print(len(primes)-1, "primes found.")
        if isANewPrime(6*k+1, primes):
            primes.append(6*k+1)
            if ((len(primes) - 1) % incrementToPrint == 0):
                print(len(primes)-1, "primes found.")
        if len(primes) >= nthPrimeToFind + 1:
            break
        k += 1
        #if newTry > 100:
        #    break
    totalTime = time() - startTime
    print(str(nthPrimeToFind) + "th Prime is:", primes[nthPrimeToFind])
    print("Time to find:", totalTime)
