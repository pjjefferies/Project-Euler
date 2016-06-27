# -*- coding: utf-8 -*-
"""
Project Euler

Problem 21: Amicable numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.


"""

from time import time

"""
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

def findNPrimes(n):
    nthPrimeToFind = n
    primes = [2, 3]
    k = 1       #all primes above 3 can be written as 6k +/- 1
    while True:
        #print("Primes found:", primes, ". Trying:", newTry)
        if isANewPrime(6*k-1, primes):
            primes.append(6*k-1)
        if isANewPrime(6*k+1, primes):
            primes.append(6*k+1)
        if len(primes) >= nthPrimeToFind + 1:
            break
        k += 1
    return primes

def getPrimeExp(aTriNum, thisPrime):
    anExp = 0
    while True:
        if aTriNum % thisPrime == 0:
            aTriNum = int(aTriNum / thisPrime)
            anExp += 1
        else:
            return anExp

def findPrimes(aNum, primes):
    aNumOG = aNum
    if aNum == 1:
        return []
    thePrimes = []
    for aPrime in primes:
        if aNum % aPrime == 0:
            aPrimeExp = getPrimeExp(aNum, aPrime)
            #print("aNum:", aNum, ", aPrime:", aPrime, ", aPrimeExp:", aPrimeExp)
            thePrimes.append(aPrime)
            aNum = int(aNum / (aPrime**aPrimeExp))
            if aNum == 1:
                return thePrimes
    print("If you got here, that's a problem. aNum:", aNum, ", thePrimes:",
          thePrimes, ", aNumOG:", aNumOG)
"""

def findFactorsBruteForce(aNum):
    factors = set()
    maxToTry = int(aNum ** (1.0/2.0))
    for numToTry in range(1, maxToTry + 1):
        if aNum % numToTry == 0:
            factors.add(numToTry)
            factors.add(int(aNum / numToTry))
    factors.discard(aNum)
    return factors

if __name__ == '__main__':
    startTime = time()
    print("\n\n")


    maxAmicableNumber = 10000 - 1
    #maxAmicableNumber = 250 - 1     # for debus

    amicableNumbers = set()
    numsTried = []
    for numToTry in range(2, maxAmicableNumber+1):
        if numToTry in numsTried:
            #print(numToTry, "already evaluated, move on")
            continue
        numsTried.append(numToTry)
        numToTryFactors = findFactorsBruteForce(numToTry)
        #print("1:", numToTry, "factors are", numToTryFactors)
        potAmicableNum = 0
        for aFactor in numToTryFactors:
            potAmicableNum += aFactor
        if potAmicableNum in numsTried or potAmicableNum == numToTry:
            #print(numToTry, "already evaluated, move on")
            continue
        numsTried.append(potAmicableNum)
        potAmicableNumFactors = findFactorsBruteForce(potAmicableNum)
        #print("2:", potAmicableNum, "factors are", potAmicableNumFactors)
        potAmicableNumFactorsSum = 0
        for aFactor in potAmicableNumFactors:
            potAmicableNumFactorsSum += aFactor
        if potAmicableNumFactorsSum == numToTry:
            amicableNumbers.add(numToTry)
            amicableNumbers.add(potAmicableNum)
            print("Found a pair of amicalble numbers:", str(numToTry)+",",
                  potAmicableNum)
        else:
            #print("numtoTry and potAmicableNum are not amicable numbers")
            pass

    sumOfAmicableNums = 0
    for aNum in amicableNumbers:
        sumOfAmicableNums += aNum

    totalTime = time() - startTime
    print("The sum of all the amicable numbers under 1000 are", sumOfAmicableNums)
    print("Time to find:", totalTime)


"""

Result

Found a pair of amicalble numbers: 220, 284
Found a pair of amicalble numbers: 1184, 1210
Found a pair of amicalble numbers: 2620, 2924
Found a pair of amicalble numbers: 5020, 5564
Found a pair of amicalble numbers: 6232, 6368
The sum of all the amicable numbers under 1000 are 31626
Time to find: 3.9847609996795654

"""





""" - stopped for difficulty of finding factors knowing primes and prime exponents, probably require recursion
    primes = findNPrimes(1000)
    amicableNumbers = set()
    numsTried = []
    for numToTry in range(2, maxAmicableNumber+1):
        if numToTry in numsTried:
            print(numtoTry, "already evaluated, move on")
            continue
        thisNumPrimes = findPrimes(numToTry, primes)
        numToTryFactors = set()
        numToTryFactorsSum = 0
        thisNumPrimeExps = []
        for aPrime in thisNumPrimes:            
            #aPrimeExp = getPrimeExp(numToTry, aPrime)
            thisNumPrimeExps.append(getPrimeExp(numToTry, aPrime))
        for aPrimeSeqNo1 in range(len(thisNumPrimes)):
            for aPrimeSeqNo2 in range(aPrimeSeqNo1,len(thisNumPrimes)):
                
                numToTryFactors.add(aPrime ** anExp)
        numToTryFactors.discard(numToTry)
        print("1:", numToTry, "factors are", numToTryFactors)
        for aFactor in numToTryFactors:
            numToTryFactorsSum += aFactor
        potAmicableNum = numToTryFactorsSum
        if potAmicableNum in numsTried:
            print(potAmicableNum, "already evaluated, move on")
            continue
        numsTried.append(numToTry)
        numsTried.append(potAmicableNum)
        print("For", numToTry, ", the potential amicable pair is", potAmicableNum)
        if potAmicableNum == numToTry:
            print("Potential Amicable Number and Number to try,", str(numToTry)+", are identical. Move on.")
            continue
        potAmicableNumPrimes = findPrimes(potAmicableNum, primes)
        potAmicableNumFactors = set()
        potAmicableNumFactorsSum = 0
        for aPrime in potAmicableNumPrimes:
            aPrimeExp = getPrimeExp(numToTryFactorsSum, aPrime)
            for anExp in range(aPrimeExp+1):
                potAmicableNumFactors.add(aPrime ** anExp)
        potAmicableNumFactors.discard(potAmicableNum)
        print("2:", potAmicableNum, "factors are", potAmicableNumFactors)
        origPotAmicableNum = 0
        for aFactor in potAmicableNumFactors:
            origPotAmicableNum += aFactor
        if origPotAmicableNum == numToTry:
            amicableNumbers.add(numToTry)
            amicableNumbers.add(potAmicableNum)
            print("Found a pair of amicalble numbers:", str(numToTry)+",",
                  potAmicableNum)
        else:
            print("numtoTry and potAmicableNum are not amicable numbers")
"""
