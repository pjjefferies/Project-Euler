# -*- coding: utf-8 -*-
"""
Project Euler

Problem 48: Self Powers

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10,405,071,317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

Analysis

"""


from time import time





if __name__ == '__main__':
    startTime = time()
    print("\n\n\n")

    maxOfSeries = 1000
    sumOfSeries = 0
    for aNum in range(1,maxOfSeries+1):
        tempNumStr = int(str(aNum ** aNum)[-10:])
        sumOfSeries += tempNumStr
    
    sumOfSeriesTen = str(sumOfSeries)[-10:]


    totalTime = time() - startTime
    print("\n\nThe last ten digits of the series 1^1+2^2+..+1000^1000 are",
          sumOfSeriesTen)
    print("Time to find:", '{:,.3f}'.format(totalTime))

"""
Result:

The last ten digits of the series 1^1+2^2+..+1000^1000 are 9110846700
Time to find: 0.219

"""
