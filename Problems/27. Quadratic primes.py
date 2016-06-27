# -*- coding: utf-8 -*-
"""
Project Euler

Problem 27: Quadratic primes

Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values
n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80
primes for the consecutive values n = 0 to 79. The product of the coefficients,
−79 and 1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = 0.


"""
"""
Analysis
     b must be a prime number to satisfy when n = 0
     a must positive or negative integer to result in an integer with b and n as integers
     n**2 + an + b > 1
          an > 1 -b - n**2
          a > 1/n - b/n - n but this must apply at the extremes of b, 2 and 997,
                         the lowest and highest prime from -999 to +999, and for n starting at 0 or 1
          for b = 2, n = 0;   a > 1 -   2/1 + 1; a > -2
          for b = 997, n = 0; a > 1 - 997/1 + 1; a > -997
          therefore, for lower values of b, we can restrict the range of 'a' more

"""

from time import time
from math import sqrt

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


def isAPrime(aNum, primes):
    if primes[-1] < aNum:
        primes = findPrimes(aNum, primes)
    if aNum in primes:
        return True, primes
    else:
        return False, primes


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
            primes.append(potentialPrime)
        k += 1


if __name__ == '__main__':
    startTime = time()

    minA = -1000 + 1
    maxA = 1000 - 1
    minB = -1000 + 1     #has no effect
    maxB = 1000 - 1
    longestPrimeSeqLen = 0
    longestPrimeSeqA   = 0
    longestPrimeSeqB   = 0

    print("Finding primes as high as", maxB)
    primes = findPrimes(maxB)
    bOptions = primes[:]

    for aB in bOptions:
        print("Evaluating aB:", aB)
        aMin = -aB
        for anA in range(-aB, maxA + 1):
            #print("Evaluating anA", anA)
            #currentPrimeSeqLength = 0
            n = 0
            while True:
                possiblePrime = n**2 + anA * n + aB
                #print("possiblePrime:", possiblePrime, ", n:", n, ", anA:",
                #      anA, ", aB:", aB)
                aPrimeQ, primes = isAPrime(possiblePrime, primes)
                if aPrimeQ:
                    #currentPrimeSeqLength += 1
                    n += 1
                    continue
                #print("Is a prime")
                if n > longestPrimeSeqLen:
                    longestPrimeSeqLen = n
                    longestPrimeSeqA = anA
                    longestPrimeSeqB = aB
                    print("Found a new longest seqence of length",
                          longestPrimeSeqLen, ", with anA:", anA , "and aB:",
                          aB)
                break

    totalTime = time() - startTime
    print("The quadratic expression that produces the longest prime sequence starting at n=0 is:",
          "n**2 + n*"+str(longestPrimeSeqA), "+", str(longestPrimeSeqB)+" with a sequence length of",
          str(longestPrimeSeqLen)+". a * b =", longestPrimeSeqA*longestPrimeSeqB)
    print("Time to find:", totalTime)

"""

Result

The quadratic expression that produces the longest prime sequence starting at
n=0 is: n**2 + n*-61 + 971 with a sequence length of 71. a * b = -59231
Time to find: 384.43325304985046

"""
