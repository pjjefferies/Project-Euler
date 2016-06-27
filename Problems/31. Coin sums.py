# -*- coding: utf-8 -*-
"""
Project Euler

Problem 31: Coin Sums

In England the currency is made up of pound, £, and pence, p, and there are
eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

"""

from time import time

#Solution from problem overview - recursive with memorization

def addNextCoinWrapperTheirs(coinsSoFar, COINVALUES, TARGETVALUE):
    memorizedSolCache = [0] * (TARGETVALUE+1)
    memorizedSolCache[0] = 1
    for coinValue in COINVALUES:
        for j in range(coinValue, TARGETVALUE+1):
            memorizedSolCache[j] += memorizedSolCache[j-coinValue]
    #print(memorizedSolCache, len(memorizedSolCache))
    return memorizedSolCache[-1]


#My Solution

def addNextCoinWrapperMine(coinsSoFar, COINVALUES, TARGETVALUE):
    NOCOINTYPES = len(COINVALUES)

    def addNextCoin(coinsSoFar):
        nextCoinNo = len(coinsSoFar)
        #print("In addNextCoin, coinsSoFar:", coinsSoFar, ", nextCoinNo:",
        #      nextCoinNo)
        if nextCoinNo == NOCOINTYPES:   #return ValueError if no more coins to make solution
            raise ValueError
        total = 0
        for coinNo in range(len(coinsSoFar)):       #Do we need this?
            total += coinsSoFar[coinNo]*COINVALUES[coinNo]
        coinQuantPoss = (TARGETVALUE - total) // COINVALUES[nextCoinNo]
        #print("TARGETVALUE:", TARGETVALUE, ", total:", total,
        #      ", COINVALUES[nextCoinNo]:", COINVALUES[nextCoinNo],
        #      ", coinQuantPoss:", coinQuantPoss)
        returnCoinsLists = []
        for coinQuant in range(coinQuantPoss+1):  #iterate over possible range of
            nextCoinList = coinsSoFar + [coinQuant]
            #print("nextCoinList 1:", nextCoinList, ", coinsSoFar:", coinsSoFar, ", coinQuant:", coinQuant)
            newTotal = 0
            for coinNo in range(len(nextCoinList)):
                newTotal += nextCoinList[coinNo]*COINVALUES[coinNo]
            if newTotal == TARGETVALUE:
                returnCoinsLists = returnCoinsLists + [nextCoinList]
                #print("Found a solution:", nextCoinList, ", returnCoinsLists:", returnCoinsLists)
                continue
            #print("nextCoinList 2:", nextCoinList, ", coinQuant:", coinQuant)
            try:                                #current coin nos. that don't exceed target
                #print("###Sent to addNextCoin, nextCoinList:", nextCoinList)
                nextCoinList = addNextCoin(nextCoinList[:]) #should only receive solutions here
                #print("Returned from addNextCoin, nextCoinList:", nextCoinList)
                #print("In coinQuant Loop, coinQuant:", coinQuant)
                if nextCoinList == []:  #no solutions return, next...
                    continue
            except ValueError:
                #print("Returned from addNextCoin with no solution, at end of coins. Going in nextCoinList:", nextCoinList)
                continue
            returnCoinsLists = returnCoinsLists + nextCoinList
            #print("Found solution(s) 2:", nextCoinList, ", returnCoinsLists:", returnCoinsLists)
        #print("###After for loop, returning these solutions:", returnCoinsLists)
        return returnCoinsLists
        
    return addNextCoin(coinsSoFar)



if __name__ == '__main__':
    startTime = time()
    print("\n\n\n")
    COINVALUES = [1, 2, 5, 10, 20, 50, 100, 200]
    #COINVALUES = [1, 2, 5, 10]    #for debug
    TARGETVALUE = 200
    #TARGETVALUE = 100                    #for debug

    listOfCombinations = addNextCoinWrapperMine([], COINVALUES, TARGETVALUE)
    startTime2 = time()
    noOfCombinations = addNextCoinWrapperTheirs([], COINVALUES, TARGETVALUE)

    for aSol in range(len(listOfCombinations)):
        for zeroToPad in range(len(COINVALUES)-len(listOfCombinations[aSol])):
            listOfCombinations[aSol] += [0]
    
    totalTimeMine = time() - startTime2
    totalTimeTheirs = startTime2 - startTime
    print("\n\nMy solution: The coinst 1p, 2p, 5p, 10p, 20p, 50p, 1 Pound, 2 Pound can be",
          "combined in", len(listOfCombinations), "ways to make 2 Pounds.")
          #"follows:", listOfCombinations)
    print("Time to find:", totalTimeMine)
    print("\nTheir solution: The coinst 1p, 2p, 5p, 10p, 20p, 50p, 1 Pound, 2 Pound can be",
          "combined in", noOfCombinations, ".")
    print("Time to find:", totalTimeTheirs, "\n\n")



"""
Result:

The coinst 1p, 2p, 5p, 10p, 20p, 50p, 1 Pound, 2 Pound can be combined in 73682
ways to make 2 Pounds asfollows: [[0, 0, 0, 0, 0, 0, 0, 1], ...
Time to find: 133.05169820785522

"""