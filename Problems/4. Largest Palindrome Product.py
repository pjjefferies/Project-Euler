# -*- coding: utf-8 -*-
"""
Project Euler

Problem 4

Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


from time import time

def isAPalindrome(aNumber):
    aNumberString = str(aNumber)
    return aNumberString == aNumberString[::-1]


def searchForPalindrome():
    palindrome = 0
    for no1 in range(999,99,-1):
        for no2 in range(no1,99,-1):
            if no1 * no2 < palindrome:
                continue
            if isAPalindrome(no1 * no2):
                palindrome, factor1, factor2 = no1 * no2, no1, no2
                print("Found one:", palindrome)
    return factor1, factor2


if __name__ == '__main__':
    startTime = time()
    no1, no2 = searchForPalindrome()
    totalTime = time() - startTime
    print("Factor1:", no1, ", Factor2:", no2, ", Product:", no1*no2)
    print("Time to find:", totalTime)