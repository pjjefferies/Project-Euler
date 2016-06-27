# -*- coding: utf-8 -*-
"""
Project Euler

Problem 37: Truncatable primes

The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

"""

"""

Analysis



"""

from time import time

def findPrimes(maxValueOfPrime, primes=None):   #Sieve of Eratosthenes
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

"""
def isAPrime(number, primes):
    if number > max(primes):
        print("isAPrime Inconclusive for value:", number)
        raise ValueError
    if number in primes:
        return True
    return False
"""

"""
def isATruncPrimeRightTrunc(aPrime, primes):
    for aCharNo in range(1,len(str(aPrime))):
        #print("In isATruncPrimeRightTrunc, eval.", int(str(aPrime)[aCharNo:]),
        #      "in", aPrime)
        if not int(str(aPrime)[:-aCharNo]) in primes:
            return False
    return True

"""
def isATruncPrimeLeftTrunc(aPrime, primes):
    for aCharNo in range(1,len(str(aPrime))):
        #print("In isATruncPrimeLeftTrunc, eval.", int(str(aPrime)[aCharNo:]),
        #      "in", aPrime)
        if not int(str(aPrime)[aCharNo:]) in primes:
            return False
    return True


if __name__ == '__main__':
    startTime = time()
    print("\n\n\n")

    listOfPrimes = findPrimes(int(1E6-1))
    maxPrimeFound = max(listOfPrimes)
    print("Seed list of primes", len(listOfPrimes), "found with max value of", str(max(listOfPrimes))+".")
    truncatablePrimesOneWay = []

    nextListToEval = ['2', '3', '5', '7']
    flagToStop = False

    while nextListToEval != [] and (not flagToStop):
        nextNextListToEval = []
        for numToEval in nextListToEval:
            #print("At first 'for', nextListToEval", nextListToEval,
            #      ", numToEval:", numToEval)
            tempListToEval = []
            for newDigit in range(0,9+1):
                tempNumToEval = int(str(numToEval)+str(newDigit))
                #print("Adding", numToEval, "to", newDigit, "=", tempNumToEval,
                #      "to check if prime")
                if tempNumToEval <= maxPrimeFound:
                    if tempNumToEval in listOfPrimes:
                        #print("yes, it is prime")
                        tempListToEval += [tempNumToEval]
                else:
                    print("Not enough primes to compare to for", tempNumToEval,
                          "use alternate method")
                    flagToStop = True
                    break
            if tempListToEval == []:
                #print("No next level primes found to", numToEval)
                pass
            else:
                truncatablePrimesOneWay += tempListToEval
                truncatablePrimes = []
                for aPrime in truncatablePrimesOneWay:
                    if isATruncPrimeLeftTrunc(aPrime, listOfPrimes):
                        #print("yes,", aPrime, "is left trunctable too!")
                        truncatablePrimes += [aPrime]
                    else:
                        #print("no,", aPrime, "is not left trunctable too")
                        pass
                if len(truncatablePrimes) >= 11:
                    break
                #print("Current truncatablePrimes list:", truncatablePrimesOneWay)
                nextNextListToEval += tempListToEval
        nextListToEval = nextNextListToEval[:]

    truncatablePrimeSum = sum(truncatablePrimes)

    totalTime = time() - startTime
    print("\n\nThe sum of all truncatable primes is", truncatablePrimeSum,
          ". The truncatable primes are:", truncatablePrimes)
    print("Time to find:", '{:,.3f}'.format(totalTime))


"""
Result:

Work Computer
The sum of all truncatable primes is 748317 . The truncatable primes are: [23,
37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
Time to find: 1.919

Home Computer
The sum of all truncatable primes is 748317 . The truncatable primes are: [23,
37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]
Time to find: 6.035

"""
