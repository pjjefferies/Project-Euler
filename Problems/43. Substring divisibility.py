# -*- coding: utf-8 -*-
"""
Project Euler

Problem 43: Sub-string divisibility

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.

"""

"""

Analysis

d8d9d10 % 17 = 0 => d8d9d10 : [0, 986] by 17
d7d8d9  % 13 = 0 => d7*100 + d8 *10 + d9 = 13n, for n=0, 1, 2, ...
                    d7 = (13n - d8*10 - d9)/100 for n=0, 1, 2, ... but !=d8d9d10
d4d5d6  %  5 = 0 => d5 : [0, 5]
d5d6d7  %  7 = 0 => d5 = (7n - d6*10 - d5)/100 for n=0, 1, 2, ... but !=d6d7d8d9
d2d3d4  % 2  = 0 => d4 = [0, 2, 4, 6, 8], but != d5d6d7d8d9
d3 in remaining digits
d2 in remaining digits
d1 is remaining digit

38,318,280 remaining possibilities - better than 10 billion

"""

from time import time

def subStringDivisibilityTest(aSolutionTry):
    aS = str(aSolutionTry)    
    if len(aS) == 9 and '0' not in aS:
        aS = '0' + aS
    #print(aSolutionTry, aS)
    d2d3d4 = 100*int(aS[2-1])+10*int(aS[3-1])+int(aS[4-1])
    d3d4d5 = 100*int(aS[3-1])+10*int(aS[4-1])+int(aS[5-1])
    d4d5d6 = 100*int(aS[4-1])+10*int(aS[5-1])+int(aS[6-1])
    d5d6d7 = 100*int(aS[5-1])+10*int(aS[6-1])+int(aS[7-1])
    d6d7d8 = 100*int(aS[6-1])+10*int(aS[7-1])+int(aS[8-1])
    d7d8d9 = 100*int(aS[7-1])+10*int(aS[8-1])+int(aS[9-1])
    d8d9d10 = 100*int(aS[8-1])+10*int(aS[9-1])+int(aS[10-1])
    
    if d2d3d4 % 2 != 0:
        print("failed 234 test")
        return False
    if d3d4d5 % 3 != 0:
        print("failed 345 test")
        return False
    if d4d5d6 % 5 != 0:
        print("failed 456 test")
        return False
    if d5d6d7 % 7 != 0:
        print("failed 567 test")
        return False
    if d6d7d8 % 11 != 0:
        print("failed 678 test")
        return False
    if d7d8d9 % 13 != 0:
        print("failed 789 test")
        return False
    if d8d9d10 % 17 != 0:
        print("failed 8910 test")
        return False
    return True


if __name__ == '__main__':
    startTime = time()
    print("\n\n\n")

    solutionsList = []
    for d8d9d10 in range(102, 986, 17):
        numString3 = str(d8d9d10)
        d10 = int(str(d8d9d10)[2])
        d9 = int(str(d8d9d10)[1])
        d8 = int(str(d8d9d10)[0])
        if d8 == d9 or d9 == d10 or d8 == d10:
            continue
        #print("Found through d8:", numString3)
        for n7 in range(0, 76):     #temp, should be 76
            d7 = (13*n7 - d8*10 - d9) / 100
            #print("n7:", n7, ", d7:", d7, ", d8:", d8, ", d9:", d9, d7 % 1 == 0)
            if round(d7,3) % 1 != 0 or d7 > 9.5:
                continue
            #print("d7=...")
            d7 = int(d7)
            if str(d7) in numString3:
                break
            numString4 = str(d7) + numString3
            #print("Found through d7:", numString4)
            for d6 in range(0, 5+1, 5):
                if str(d6) in numString4 or ((d6*100+d7*10+d8) % 11 != 0):
                    continue
                numString5 = str(d6) + numString4
                for n5 in range(0, 142):
                    d5 = (7*n5 - d6*10 - d7)/100
                    if d5 % 1 != 0 or d5 > 9.5:
                        continue
                    d5 = int(d5)
                    if str(d5) in numString5:
                        continue
                    numString6 = str(d5) + numString5
                    #print("Found through d5:", numString6)
                    for d4 in range(0, 8+1, 2):
                        if str(d4) in numString6:
                            continue
                        numString7 = str(d4) + numString6
                        #print("Found through d4:", numString7)
                        remainChar = "0123456789"
                        for aChar in numString7:
                            remainChar = remainChar.replace(aChar,"")
                        #print("remainChar:", remainChar)
                        for d3Char in remainChar:
                            d3 = int(d3Char)
                            if ((d3*100+d4*10+d5) % 3 != 0):
                                continue
                            #print("Found through d3:", d3Char + numString7)
                            remainChar2 = remainChar.replace(d3Char, "")
                            for d2Char in remainChar2:
                                d2 = int(d2Char)
                                #print("Found through d2:", d2Char + d3Char + numString7)
                                d1Char = remainChar2.replace(d2Char,"")
                                #print("Found through d1:", d1Char + d2Char + d3Char + numString7)
                                numString10 = (d1Char + d2Char + d3Char
                                             + numString7)
                                #print("Found one:", numString10)
                                solutionsList.append(int(numString10))
    
    realSolutionsList = []
    for aSolution in solutionsList:
        if subStringDivisibilityTest(aSolution):
            realSolutionsList.append(aSolution)
        else:
            print("Found false solution:", aSolution)
    
    solutionsSum = sum(realSolutionsList)

    totalTime = time() - startTime
    print("\n\nThe sum of all 0 to 9 digit pandigital numbes with listed",
          "property is", str(solutionsSum)+ ". The list of numbers is:",
          solutionsList)
    print("Time to find:", '{:,.3f}'.format(totalTime))


"""
Result:

The sum of all 0 to 9 digit pandigital numbes with listed property is
16695334890. The list of numbers is: [4160357289, 1460357289, 4106357289,
1406357289, 4130952867, 1430952867]
Time to find: 0.000

"""