# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 23:53:55 2019

@author: PaulJ
"""

factors_cache = {}


def find_all_factors(number):
    orig_number = number
    if number in factors_cache:
        return factors_cache[number]
    listOfFactors = []
    listOfLargeFactors = []
    testFactor = 2
    maxSingleFactorLimit = number**(0.5) + 1
    while testFactor < maxSingleFactorLimit and number != 1:
        if number % testFactor == 0:
            listOfFactors.append(testFactor)
            listOfLargeFactors.append(int(round(number / testFactor, 0)))
            number = 1
        testFactor += 1
    for aLargeFactor in listOfLargeFactors:
        large_list_factors = find_all_factors(aLargeFactor)
        listOfFactors = listOfFactors + large_list_factors
    if not listOfFactors:
        listOfFactors = [number]
    if 1 in listOfFactors:
        listOfFactors.remove(1)
    factors_cache[orig_number] = listOfFactors
    return listOfFactors
