# -*- coding: utf-8 -*-
"""
Project Euler

Problem 50: Consecutive prime sum

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?

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


def longestSequentialSumSeries(sumToFind, listOfComponents):
    print("In longest...: sumToFind:", sumToFind, ", listOfComponets:",
          listOfComponents)
    longestSolution = []
    for aCompLeftNo, aCompLeft in enumerate(listOfComponents):
        print("In first for, aCompLeftNo:", aCompLeftNo, ", aCompLeft:", aCompLeft)
        tempSum = aCompLeft
        for nextCompNo, nextComp in enumerate(listOfComponents[aCompLeftNo+1:],
                                              aCompLeftNo+1):
            tempSum += nextComp
            print("   Updated tempSum:", tempSum)
            if tempSum == sumToFind:
                tempSolution = [aCompLeft] + listOfComponents[aCompLeftNo:nextCompNo]
                print("tempSolution:", tempSolution)
                if len(tempSolution) > len(longestSolution):
                    longestSolution = tempSolution[:]
                    break
    if len(longestSolution) > 0:
        return longestSolution
    else:
        raise ValueError


if __name__ == '__main__':
    startTime = time()
    print("\n\n")

    maxPrimeValue = 1000000
    #maxPrimeValue = 10000      #for debug
    primeSumSeries = []
    primes = findPrimes(maxPrimeValue)

    primeSumDict = {1: 0}
    sumPrimes = [0]*(maxPrimeValue+1)
    prevPrime = 1
    for aPrimeNo, aPrime in enumerate(primes, start=1):
        #sumPrimes[aPrime] = sumPrimes[prevPrime] + aPrime
        #print("aPrime:", aPrime, ", sumPrimes[prevPrime]", sumPrimes[prevPrime],
        #      ", prevPrime:", prevPrime)
        primeSumDict[aPrime] = primeSumDict[prevPrime] + aPrime
        prevPrime = aPrime

    invPrimeSumDict = dict([[v,k] for k,v in primeSumDict.items()])

    #del primeSumDict[1]
    counter = 1

    print("Finished creating referene lists & dictionary")
    lowerPrimes = []

    for aPrime in primes:
        if counter % 1000 == 0:
            print("Evaluating Prime", aPrime)
        counter += 1
        lowerPrimes = []
        for anotherPrime in primes:
            if anotherPrime < aPrime:
                lowerPrimes.append(anotherPrime)
            else:
                break

        for aLoPrReNo, aLoPrRem in enumerate(lowerPrimes):

            reqHighSum = (aPrime + primeSumDict[aLoPrRem] - aLoPrRem)

            highPrime = invPrimeSumDict.get(reqHighSum, 0)

            if highPrime == 0 or highPrime <= aLoPrRem:
                continue
            else:
                primeSumSeries.append([aPrime, aLoPrRem, highPrime])
                """
                tempSeries = []
                for aNum in range(aLoPrRem,
                                  invPrimeSumDict[reqHighSum]+1):
                    if aNum in primeSumDict:
                        tempSeries.append(aNum)
                #print("tempSeries:", tempSeries)
                #primeSumSeries.append([aPrime, tempSeries])
                #print("Found one:", primeSumSeries[-1])
                """
                lowerPrimes.append(aPrime)
                break
        lowerPrimes.append(aPrime)

    for aPrSumSerNo, aPrSumSer in enumerate(primeSumSeries):
        tempPrimeList = []
        for aPrime in primes:
            if aPrime < aPrSumSer[1]:
                continue
            if aPrime > aPrSumSer[2]:
                primeSumSeries[aPrSumSerNo].append(tempPrimeList)
                break
            tempPrimeList.append(aPrime)


    bestSolution = [0, 0, 0, []]
    for aSolution in primeSumSeries:
        if len(aSolution[3]) > len(bestSolution[3]):
            bestSolution = aSolution[:]

    totalTime = time() - startTime
    print("\nThe prime that can be written as the longest sum of primes below"
          "one-million is", bestSolution[0], "with series", bestSolution[3],
          "with", len(bestSolution[3]), "items.")
    print("Time to find:", '{:,.3f}'.format(totalTime))

"""
Result:

The prime that can be written as the longest sum of primes belowone-million is
997651 with series [7, 11, ..., 3929, 3931] with 543 items.
Time to find: 3,814.935  (63.6 min.)
On work computer with latest algorythm: 1,840.288 s (30.7 min.)

"""
