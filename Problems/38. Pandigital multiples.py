# -*- coding: utf-8 -*-
"""
Project Euler

Problem 38: Pandigital multiples

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?

"""

"""

Analysis

x1x2x3x4 x i = xxxx or xxxxx, x=1, 2

x1x2x3 x i = xxx or xxxx, i=1, 2, 3     O(1000)

x1x2 x i = xx or xxx, i=1, 2, 3         O(100)

x1 x i = x or xx, i=1, 2, 3, 4, 5, 6, 7, 8, 9, 10

"""

from time import time


if __name__ == '__main__':
    startTime = time()
    #print("\n\n\n")

    pandigitalSolutions = []

    #Case x1x2x3x4 x i = xxxx or xxxxx, x=1, 2
    for anInt in range(1000, 9999+1):
        aPotPanD = ""
        for aSeqNo in range(1, 2+1):
            aPotPanD += str(anInt * aSeqNo)
        #print("aPotPanD:", aPotPanD)
        if len(aPotPanD) == 9:
            flag = True
            for aDigit in "123456789":
                if aDigit not in aPotPanD:
                    flag = False
                    break
            if flag:
                pandigitalSolutions += [[anInt, (1,2), int(aPotPanD)]]

    #Case x1x2x3 x i = xxxx or xxxxx, x=1, 2, 3
    for anInt in range(100, 999+1):
        aPotPanD = ""
        for aSeqNo in range(1, 3+1):
            aPotPanD += str(anInt * aSeqNo)
        #print("aPotPanD:", aPotPanD)
        if len(aPotPanD) == 9:
            flag = True
            for aDigit in "123456789":
                if aDigit not in aPotPanD:
                    flag = False
                    break
            if flag:
                pandigitalSolutions += [[anInt, (1,2), int(aPotPanD)]]

    #Case x1x2 x i = xxxx or xxxxx, x=1, 2, 3
    for anInt in range(10, 99+1):
        aPotPanD = ""
        for aSeqNo in range(1, 3+1):
            aPotPanD += str(anInt * aSeqNo)
        #print("aPotPanD:", aPotPanD)
        if len(aPotPanD) == 9:
            flag = True
            for aDigit in "123456789":
                if aDigit not in aPotPanD:
                    flag = False
                    break
            if flag:
                pandigitalSolutions += [[anInt, (1,2), int(aPotPanD)]]

    #Case x1 x i = xxxx or xxxxx, x=1, 2, 3, 4, 5, 6, 7, 8 ,9
    for anInt in range(1, 9+1):
        aPotPanD = ""
        for aSeqNo in range(1, 9+1):
            aPotPanD += str(anInt * aSeqNo)
        #print("aPotPanD:", aPotPanD)
        if len(aPotPanD) == 9:
            #print("Length is 9")
            flag = True
            for aDigit in "123456789":
                if aDigit not in aPotPanD:
                    flag = False
                    break
            if flag:
                pandigitalSolutions += [[anInt, (1,2), int(aPotPanD)]]

    
    maxPanD = (0,0,0)
    for aPanD in pandigitalSolutions:
        if aPanD[2] > maxPanD[2]:
            maxPanD = aPanD[:]


    totalTime = time() - startTime
    print("\n\nThe largest 1 to 9 pandigital 9-digit number as the",
          "concatinated product of an integer with (1,2, ..., n), n > 1 is",
          maxPanD, ". The complete list is:", pandigitalSolutions)
    print("Time to find:", '{:,.3f}'.format(totalTime))


"""
Result:

The largest 1 to 9 pandigital 9-digit number as the concatinated product of an
integer with (1,2, ..., n), n > 1 is [9327, (1, 2), 932718654] . The complete
list is: [[6729, (1, 2), 672913458], [6792, (1, 2), 679213584], [6927, (1, 2),
692713854], [7269, (1, 2), 726914538], [7293, (1, 2), 729314586], [7329,
(1, 2), 732914658], [7692, (1, 2), 769215384], [7923, (1, 2), 792315846],
[7932, (1, 2), 793215864], [9267, (1, 2), 926718534], [9273, (1, 2),
927318546], [9327, (1, 2), 932718654], [192, (1, 2), 192384576], [219, (1, 2),
219438657], [273, (1, 2), 273546819], [327, (1, 2), 327654981], [1, (1, 2),
123456789]]
Time to find: 0.049

"""