# -*- coding: utf-8 -*-
"""
Project Euler

Problem 14: Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""

from time import time


"""
if __name__ == '__main__':
    startTime = time()
    n = 2
    maxN = 1e6 - 1 + 1
    #maxN = 1000        #for debugging
    maxSeqNo = 1
    maxSeqLen = 0
    while n < maxN:
        #print("Looking for Collatz seqence length of", n, ".")
        noOfSteps = 0
        nextInSeq = n
        stepsInSeq = []     #A stack of [n, steps to 1]
        while nextInSeq != 1:
            #print("Into 2nd while. nextInSeq:", nextInSeq, ", stepsInSeq:", stepsInSeq)
            #print("After incrementing steps, stepsInSeq:", stepsInSeq)            
            noOfSteps += 1
            nextInSeq = int(nextInSeq/2) if ((nextInSeq % 2) == 0) else int((3*nextInSeq)+1)
            #print("After finding next seq. no, nextInSeq:", nextInSeq)
            #chainSeq += 1
        #should have found the length of new seq. by here
        #if stepsInSeq[0][1] > maxSeqLen:
        if noOfSteps > maxSeqLen:
            maxSeqLen = noOfSteps
            maxSeqNo  = n
            print("Found new longest length seq. maxSeqLen:", maxSeqLen, ", maxSeqNo:", maxSeqNo)
        #store all Collatz sequence lengths found on path
        #print("After storing all collatzSeqLen found, collatzSeqLen:", collatzSeqLen)
        #print("Found Collatz Seq. Length for", n, "and", len(stepsInSeq), "intermediate seq. lengths added")
        if n % 5000 == 0:
            #print("Found Collatz Seq. Length for", n, ". collatzSeqLen length:", len(collatzSeqLen), "size:", getsizeof(collatzSeqLen,0))
            print("Found Collatz Seq. Length for", n, ". collatzSeqLen length:", len(collatzSeqLen), "size:", getsizeof(collatzSeqLen,0))
        n += 1
    totalTime = time() - startTime
    print("The longest Collatz squence under", maxN, "is",
          maxSeqNo, "with a length of", maxSeqLen)
    print("Time to find:", totalTime)



Result

The longest Collatz squence under 1000000.0 is 837799 with a length of 524
Time to find: 160.87129402160645



"""


if __name__ == '__main__':
    startTime = time()
    collatzSeqLen = {}
    n = 2
    maxN = 1e6 - 1 + 1
    #maxN = 1000        #for debugging
    maxSeqNo = 1
    maxSeqLen = 0
    while n < maxN:
        #print("Looking for Collatz seqence length of", n, ".")
        #noOfSteps = 0
        nextInSeq = n
        stepsInSeq = []     #A stack of [n, steps to 1]
        while nextInSeq != 1:
            #print("Into 2nd while. nextInSeq:", nextInSeq, ", stepsInSeq:", stepsInSeq)
            #Try with only 1,000, saved 
            #if len(collatzSeqLen) > nextInSeq:   #If with range of some found lengths, check to see if known
                #print("In 1st 'if', len(collatzSeqLen):", len(collatzSeqLen), ", nextInSeq:", nextInSeq)
            if collatzSeqLen.get(nextInSeq, 0) != 0:  #If not zero, known. Use existing value.
                #print("In 2nd 'if'. Existing seq. found. Length:", collatzSeqLen[nextInSeq])
                #chainSeqLen += collatzSeqLen[nextInSeq] #add length on known remaining sequence to length to get here so far
                for stepNo in range(len(stepsInSeq)):   #for each step to get here, add remaining length
                    stepsInSeq[stepNo][1] += collatzSeqLen.get(nextInSeq, 0)
                    #print("After finding known length & adding to existing chain, stepsInSeq:", stepsInSeq)
                break
            stepsInSeq.append([nextInSeq,1])  #If we didn't find a known seq. length, add next in seq. to stack of steps
            #print("After adding new step, stepsInSeq:", stepsInSeq)
            for stepNo in range(len(stepsInSeq)-1): #Increment step count for each step along the way
                stepsInSeq[stepNo][1] += 1
            #print("After incrementing steps, stepsInSeq:", stepsInSeq)            
            #noOfSteps += 1
            nextInSeq = int(nextInSeq/2) if ((nextInSeq % 2) == 0) else int((3*nextInSeq)+1)
            #print("After finding next seq. no, nextInSeq:", nextInSeq)
        #should have found the length of new seq. by here
        if len(stepsInSeq) == 0:    #If sequence length is already knonw, move on...
            #print("We already know seq. length of:", str(n)+". It's", str(collatzSeqLen[n])+". Next!")
            #if n % 5000 == 0:
            #    print("Found Collatz Seq. Length for", n, ". collatzSeqLen length:", len(collatzSeqLen), "size:", getsizeof(collatzSeqLen,0))
            n += 1
            continue
        if stepsInSeq[0][1] > maxSeqLen:
        #if noOfSteps > maxSeqLen:
            maxSeqLen = stepsInSeq[0][1]
            maxSeqNo  = n
            #print("Found new longest length seq. maxSeqLen:", maxSeqLen, ", maxSeqNo:", maxSeqNo)
        #store all Collatz sequence lengths found on path
        for step in stepsInSeq:
            #while len(collatzSeqLen) <= step[0]:
            #    collatzSeqLen.append(0)
            collatzSeqLen[step[0]] = step[1]
        #print("After storing all collatzSeqLen found, collatzSeqLen:", collatzSeqLen)
        #print("Found Collatz Seq. Length for", n, "and", len(stepsInSeq), "intermediate seq. lengths added")
        #if n % 5000 == 0:
            #print("Found Collatz Seq. Length for", n, ". collatzSeqLen length:", len(collatzSeqLen), "size:", getsizeof(collatzSeqLen,0))
        #    print("Found Collatz Seq. Length for", n, ". collatzSeqLen length:", len(collatzSeqLen), "size:", getsizeof(collatzSeqLen,0))
        n += 1
    totalTime = time() - startTime
    print("The longest Collatz squence under", maxN, "is",
          maxSeqNo, "with a length of", maxSeqLen)
    print("Time to find:", totalTime)

"""

Result

The longest Collatz squence under 1000000.0 is 837799 with a length of 524
Time to find: 23.580929040908813

"""
