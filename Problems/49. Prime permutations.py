# -*- coding: utf-8 -*-
"""
Project Euler

Problem 49: Prime permutatinos

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?

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


def arePermutations(aListOfNumStr):
    aListOfStrings = []
    for aMember in aListOfNumStr:
        aListOfStrings.append(str(aMember))
    for aStringNo1, aString1 in enumerate(aListOfStrings[:-1]):
        for aStringNo2, aString2 in enumerate(aListOfStrings[aStringNo1+1:]):
            aString2Copy = aString2[:]
            for aChar in aString1:
                if aChar not in aString2Copy:
                    return False
                aString2Copy = aString2Copy.replace(aChar, "", 1)
    return True


if __name__ == '__main__':
    startTime = time()
    print("\n\n\n")

    solFound = False
    maxPrimeValue = 20000
    primes = findPrimes(maxPrimeValue)
    aNum1List = []
    aNum2List = []
    aNum3List = []

    primeDict = {}
    for aPrime in primes:
        primeDict[aPrime] = True

    for aNum1 in range(1000,9999):
        aNum1List.append(aNum1)
        if aNum1 not in primeDict or aNum1 == 1487:
            continue
        for adder in range(1, 4500):
            aNum2 = aNum1 + adder
            if aNum1 == 2969:
                aNum2List.append(aNum2)
            if aNum2 not in primeDict or aNum2 > 9999:
                continue
            aNum3 = aNum2 + adder
            if aNum1 == 2969 and aNum2 == 6299:
                aNum3List.append(aNum3)
            if aNum3 not in primeDict or aNum3 > 9999:
                continue
            if arePermutations([aNum1, aNum2, aNum3]):
                solFound = True
                break
        if solFound:
            break

    if solFound:
        aNumList = [aNum1, aNum2, aNum3]
        aNumList.sort()
        aConcatNo = int(str(aNumList[0])+str(aNumList[1])+str(aNumList[2]))

        totalTime = time() - startTime
        print("\n\nThe 12-digit number formed by concatenating the three terms in"
              "the other 4-digit prime, permutation, equal spaced numbers is",
              aConcatNo)
        print("Time to find:", '{:,.3f}'.format(totalTime))
    else:
        print("Solution not found")

"""
Result:

The 12-digit number formed by concatenating the three terms inthe other
4-digit prime, permutation, equal spaced numbers is 296962999629
Time to find: 1.032

"""
