# -*- coding: utf-8 -*-
"""
Project Euler

Problem 92: Square digit chains

A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?

Analysis

"""


from time import time


if __name__ == '__main__':
    startTime = time()
    print("\n\n")

    maxNumber = int(1e7 - 1)
    #maxNumber = int(1e3 -1)

    chainEnd = {1: 1, 89: 89}
    
    for aNum in range(1, maxNumber + 1):
        #if aNum % 50000 == 0:
        #    print("aNum:", aNum, ", length of chainEnd:", len(chainEnd))
        #print("At begining of for loop with aNum:", aNum)
        numList = [aNum]
        nextNum = aNum
        while chainEnd.get(nextNum, 0) == 0:
            nextNumStr = str(nextNum)
            nextNum = 0
            for aChar in nextNumStr:
                nextNum += int(aChar)**2
            numList.append(nextNum)
        #print("Found end of chain for", aNum, "is", numList)
        endPoint = chainEnd[numList[-1]]
        assert (endPoint == 1 or endPoint == 89)
        for aNumUsed in numList:
            chainEnd[aNumUsed] = endPoint
        
    endingAt89 = sum(1 for x in chainEnd.values() if x == 89)


    totalTime = time() - startTime
    print("\nThe number of square digig numbers that have chains ending at",
          "89 are", endingAt89, "(", str(int(endingAt89/maxNumber*100))+"%).")
    print("Time to find:", '{:,.3f}'.format(totalTime))

"""
Result:

The number of square digig numbers that have chains ending at 89 are 8581146
( 85%).
Time to find: 154.501

"""
