# -*- coding: utf-8 -*-
"""
Project Euler

Problem 3

Larget Prime Number

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

from time import time

def findAllFactors(number):
    #print("In findAllFactors with number:", number)
    if number % 2 == 0:
        listOfFactors = [2]
    else:
        listOfFactors = []
    testFactor = 3
    maxSingleFactorLimit = number**(0.5)
    maxAllFactorLimit = number / 3
    #print("Initial test factor:", testFactor)
    counter = 0
    while testFactor < maxAllFactorLimit:
        counter += 1
        if counter >= 1000000:
            #print("testFactor:", testFactor, "with limit:", maxAllFactorLimit)
            counter = 0
        if number % testFactor == 0:
            #print("found a factor:", testFactor)
            listOfFactors.append(testFactor)
            number = int(number / testFactor)
            if testFactor > maxSingleFactorLimit:
                break
            #print("In findAllFactors, new number to find factors of", number)
            maxAllFactorLimit = int(maxAllFactorLimit / testFactor) + 2
            #print("maxAllFactorLimit:", maxAllFactorLimit)
        testFactor += 2
    listOfFactors.append(number)
    #print("Returning a list of factors", listOfFactors)
    return listOfFactors


if __name__ == '__main__':
    startTime = time()
    testNumber = 600851475143
    #print("\n\nStarting to find all primes")
    #if testNumber % 2 == 0:
    #    listOfFactorsNew1 = [2] + findAllFactors(testNumber / 2)
    #else:
    listOfFactorsNew1 = findAllFactors(testNumber)
    #print("listOfFactorsNew1 before while loop:", listOfFactorsNew1)
    #print("Prime factors of", testNumber, "are", listOfFactorsNew1, ".")
    #productOfFactors = 1
    #for factor in listOfFactorsNew1:
    #    productOfFactors *= factor
    #print("Product of prime factors is:", productOfFactors)
    largestFactor = max(listOfFactorsNew1)
    totalTime = time() - startTime
    print("\nLargest prime factor of", testNumber, "is", largestFactor, ".")
    print("Time to calculate:", round(totalTime,4), ".")
        
        
        
        
        
        