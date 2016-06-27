# -*- coding: utf-8 -*-
"""
Project Euler

Problem 40: Champernowne's constant

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1,000 × d10,000 × d100,000 × d1,000,000



Analysis



"""

from time import time

if __name__ == '__main__':
    startTime = time()
    print("\n\n\n")

    #                           Didn't work, has some logic flaw
    digitRange = [0]*7
    digitRange[1] = [1, 9]
    for noDigits in range(2, 6+1):
        digitRange[noDigits] = [digitRange[noDigits-1][1]+1, 
                                digitRange[noDigits-1][1]+9*noDigits*10**(noDigits-1)]

    print("digitRange:", digitRange)
    """
    d = [0]*7   #d is number starting at digit m. fraction identifies digit in d
    d[0] = 1
    for expon in range(1, 6+1):
        numDigits = expon + 1
        number = 10**expon
        d[expon] = ((number - (digitRange[numDigits-1][1]-1+(number % 2)))/numDigits
                   + digitRange[numDigits-1][1])

    
    digitAtD = [0]*7
    digitAtD[0] = 1
    for numberNo in range(1, 6+1):
        numLength = len(str(int(d[numberNo])))
        digitNo = int(round(d[numberNo] % 1 * numLength, 0))+1
        digitAtD[numberNo] = int(str(d[numberNo])[digitNo-1])
        print("numberNo:", numberNo, ", numLength:", numLength, ", digitNo:",
              digitNo, ", digitAtD[numberNo]:", digitAtD[numberNo])

    digitProduct = 1
    for numberNo in range(1, 6+1):
        digitProduct *= digitAtD[numberNo]
    
    """

    champsConstant = ''
    aNum = 1
    while len(champsConstant) < 1e6:
        champsConstant += str(aNum)
        aNum += 1

    digitProduct = 1
    for expon in range(0, 6+1):
        digitProduct *= int(champsConstant[10**expon-1])
        print("expon:", expon, ", champsConstant:", champsConstant[10**expon-1])
        print(champsConstant[10**expon-1-3:10**expon-1+4])
        print(champsConstant[10**expon-1-10:10**expon-1+11])
    
    totalTime = time() - startTime
    print("\n\nThe product of the 7 digits is", str(digitProduct)+".")
    print("Time to find:", '{:,.3f}'.format(totalTime))

"""
Result:

The product of the 7 digits is 210.
Time to find: 0.437

"""
