# -*- coding: utf-8 -*-
"""
Project Euler

Problem 26: Reciprocal cycles

A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.



"""

from time import time


def isATerminatingDecimal(someNum): #works for inverses of number < 1000
    return (((someNum * 1000) % 1) == 0)

def lenOfRep(aNum):
    remainderSeq = []
    digitSeq = []
    divisor = aNum
    remainder = 1.0
    while True:
        remainder *= 10
        digitSeq.append(remainder // divisor)
        remainderSeq.append(remainder % divisor)
        remainder = remainderSeq[-1]
        for remainderNo in range(len(remainderSeq)-1):
            try:
                #print("In try, string to search:", remainderSeq, remainderSeq[remainderNo+1:], remainderSeq[-1])
                startOfRepeat = remainderSeq[remainderNo:-1].index(remainderSeq[-1])
            except ValueError:
                continue
            endOfRepeat = len(remainderSeq) - 2
            #print("Found a matching remainder in loc.:", startOfRepeat, "and", endOfRepeat+1)
            lengthOfRepeat = endOfRepeat - startOfRepeat + 1
            sequenceRepeated = digitSeq[startOfRepeat:endOfRepeat+1]
            return(lengthOfRepeat, startOfRepeat, sequenceRepeated, digitSeq, remainderSeq)
        #print("No repeats yet, find another digit, remainder. So far, digits:", digitSeq,
        #      "remainders:", remainderSeq)


if __name__ == '__main__':
    startTime = time()

    minNumToCheck = 950
    maxNumToCheck = 1000 - 1
    #maxNumToCheck = 8        #for debug
    updateInterval = 10
    noWithMaxRepeatingDigits = 0
    maxRepeatingDigits = 0
    #getcontext().prec = 100 
    for aNum in range(maxNumToCheck, minNumToCheck + 1, -1):
        if aNum % updateInterval == 0:
            print("Looking for repeating seq. in 1/"+str(aNum))
        #print("Looking for repeating seq. in 1/"+str(aNum))
        aNumInv = 1.0/float(aNum)
        if isATerminatingDecimal(aNumInv):
            #print(aNum, "is a terminating decimal. Next...")
            continue
        noDigitsRepeat, startOfRepeat, repeatSeq, digitSeq, remainderSea = lenOfRep(aNum)
        #print("Returned from lenOfRep:", noDigitsRepeat, startOfRepeat, repeatSeq, digitSeq, remainderSea)
        #lengthOfRepeat, startOfRepeat, sequenceRepeated, digitSeq, remainderSeq
        #noDigitsRepeat = len(digitsRepeat)
        if noDigitsRepeat > maxRepeatingDigits:
            maxRepeatingDigits = noDigitsRepeat
            noWithMaxRepeatingDigits = aNum
            print("Found new max repeating digit inverse of",
                  noWithMaxRepeatingDigits, "with", maxRepeatingDigits,
                  "repeating digits.", 1/aNum)
        #else:
            #print("Found non max repeating digit inverse of",
            #      aNum, "with", noDigitsRepeat,
            #      "repeating digits.", 1/aNum)

    totalTime = time() - startTime
    print("The number with the maximum repeating digits in its inverse is",
          noWithMaxRepeatingDigits, "with", maxRepeatingDigits, "repeating",
          "digits as:", 1.0/noWithMaxRepeatingDigits)
    print("Time to find:", totalTime)

"""

Result

The number with the maximum repeating digits in its inverse is 983 with 982 repeating digits as: 0.001017293997965412
Time to find: 53.32526087760925

"""
