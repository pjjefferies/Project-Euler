# -*- coding: utf-8 -*-
"""
Project Euler

Problem 65: Convergents (fraction) of e



Analysis

"""


from time import time


if __name__ == '__main__':
    startTime = time()
    print("\n\n")

    a = {0: 2}
    
    i = 1
    for k in range(1, 34):
        a[i] = 1
        a[i+1] = 2*k
        a[i+2] = 1
        i += 3
    
    
    convNum = {0: a[0], 1: a[1]*a[0]+1}
    convDen = {0: 1, 1: a[1]}
    for aConv in range(2, 100):
        convNum[aConv] = convNum[aConv-1]*a[aConv]+convNum[aConv-2]
        convDen[aConv] = convDen[aConv-1]*a[aConv]+convDen[aConv-2]

    print(a, "\n", len(a), "\n", convNum[99], "\n", convDen[99], "\n",
          convNum[99]/convDen[99])
    
    convNum100Text = str(convNum[99])
    convNum100SumOfDig = 0
    for aChar in convNum100Text:
        convNum100SumOfDig += int(aChar)
    

    totalTime = time() - startTime
    print("\nThe sum of digits in the numerator of the 100th convergent of",
          "the continued fraction for e is", convNum100SumOfDig)
    print("Time to find:", '{:,.3f}'.format(totalTime))

"""
Result:

The sum of digits in the numerator of the 100th convergent of the continued
fraction for e is 272
Time to find: 0.000

"""
