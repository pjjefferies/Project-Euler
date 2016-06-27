# -*- coding: utf-8 -*-
"""
Project Euler

Problem 137: Fibonacci golden nuggets

Consider the infinite polynomial series AF(x) = xF1 + x2F2 + x3F3 + ..., where
Fk is the kth term in the Fibonacci sequence: 1, 1, 2, 3, 5, 8, ... ; that is,
Fk = Fk−1 + Fk−2, F1 = 1 and F2 = 1.

For this problem we shall be interested in values of x for which AF(x) is a
positive integer.

Surprisingly AF(1/2)     =     (1/2).1 + (1/2)2.1 + (1/2)3.2 + (1/2)4.3
+ (1/2)5.5 + ...
      =     1/2 + 1/4 + 2/8 + 3/16 + 5/32 + ...
      =     2
The corresponding values of x for the first five natural numbers are shown
below.

x    AF(x)
√2−1    1
1/2    2
(√13−2)/3    3
(√89−5)/8    4
(√34−3)/5    5
We shall call AF(x) a golden nugget if x is rational, because they become
increasingly rarer; for example, the 10th golden nugget is 74049690.

Find the 15th golden nugget.

"""

from time import time
from math import log
psi = (1+5**0.5)/2
sqrtFive = 5 ** 0.5

def isFib(aNum):
    if round((5*aNum*aNum+4)**(0.5),14) % 1 == 0:
        return True
    if round((5*aNum*aNum-4)**(0.5),14) % 1 == 0:
        return True
    return False

def nOfFib(aPotFibNo):
    fiveSqRoot = 5**0.5
    aPotFibNoSq = aPotFibNo * aPotFibNo
    n = log(((aPotFibNo*fiveSqRoot+(5*aPotFibNoSq+4)**0.5)/2),psi)
    if round(n,4) % 1 == 0:
        return n
    else:
        print("First fib try check failed:", aPotFibNo, n)
    n = log(((aPotFibNo*fiveSqRoot+(5*aPotFibNoSq-4)**0.5)/2),psi)
    if round(n,4) % 1 == 0:
        return n
    else:
        print("Second fib try check failed:", aPotFibNo, n)
    raise ValueError


def fibN(aFibNum):
    aFib = round((psi**aFibNum - (-psi)**(-aFibNum)) / sqrtFive)
    print("Found fib #", aFibNum, "as", aFib)
    return aFib


def genFib(maxN=1000, maxFn=1e40):
    fN = [0, 1, 1]
    n = 2
    while ((n <= maxN) and (fN[-1] < maxFn)):
        assert (n == (len(fN) - 1))
        fN.append(fN[-1] + fN[-2])
        n += 1
    return fN


def infPolyFib(x, fibSeries):
    polySum = 0
    for aFibNo, aFib in enumerate(fibSeries[1:], start=1):
        #print(x, aFibNo, aFib)
        deltaUpdate = (float(x) ** aFibNo) * aFib
        polySumNew = polySum + deltaUpdate
        if polySum == polySumNew:   #ran out of precision
            break
        polySum = polySumNew
    return polySum, deltaUpdate


def infPolyFibSlope(x, fibSeries):
    polySum = 0
    for aFibNo, aFib in enumerate(fibSeries[1:], start=1):
        deltaUpdate = (x ** (aFibNo-1)) * aFib * aFibNo
        polySumNew = polySum + deltaUpdate
        if polySum == polySumNew:   #ran out of precision
            break
        polySum = polySumNew
    return polySum, deltaUpdate


def infPolyFibInv(aF):
    return (-aF-1+(5*aF*aF+2*aF+1)**0.5)/(2*aF)


def findPrimes(maxValueOfPrime):   #Sieve of Eratosthenes
    primes = []
    maxValueOfPrime = int(maxValueOfPrime)
    counter = 0
    primeValues = [True] * (maxValueOfPrime + 1)
    for aPrime in range(2,int(maxValueOfPrime**(1/2))+1):
        if primeValues[aPrime]:     #don't check if already rulled-out
            #print("Found a prime:", aPrime)
            if counter == 1000:
                counter = 0
                print("aPrime:", aPrime)
            for numToElim in range(aPrime*2,maxValueOfPrime+1,aPrime):
                primeValues[numToElim] = False
        counter += 1
    for aPrimeNo in range(2,len(primeValues)):
        if primeValues[aPrimeNo]:
            primes.append(aPrimeNo)
    return primes


def findPrimeFactors(aNumber, primesDict):     
    primeFactors = []
    for aPrime in primesDict:
        if aPrime > aNumber:
            break
        if aNumber % aPrime == 0:
            primeFactors.append(aPrime)
    return primeFactors


def findFactorExponents(aNumber, factors):
    aNumberReduced = aNumber
    factorAndExpon = []
    for aFactor in factors:
        expTry = 1
        while aNumberReduced % (aFactor ** expTry) == 0:
            expTry += 1
        factorAndExpon.append([aFactor, expTry-1])
    return factorAndExpon


def reduceFraction(aNum, primesDict):
    aNumNum = int(aNum * 1e15)
    aNumDen = int(1e15)
    aNumNumFactors = findPrimeFactors(aNumNum, primesDict)
    aNumNumFactors.sort(reverse=True)
    aNumNumFactExp = findFactorExponents(aNumNum, aNumNumFactors)
    #aNumDenFactors = findAllFactors(aNumDen)
    for afactor, aFactorExp in aNumNumFactExp:
        for anExp in range(aFactorExp):
            if aNumDen % afactor == 0:
                aNumDen /= afactor
                aNumNum /= afactor
    return int(aNumNum), int(aNumDen)


def genPerfSquareListDict(maxBase=1000, maxSquare=1000000,
                             perfSquaresList = None, perfSquaresDict = None):
    maxBase = max(maxBase, int(maxSquare ** 0.5 + 1))
    if perfSquaresList == None:
        perfSquaresList = []
        perfSquaresDict = {}
    aNum = len(perfSquaresList) + 1
    while aNum <= maxBase:
        aNumSquare = aNum * aNum
        perfSquaresList.append(aNumSquare)
        perfSquaresDict[aNumSquare] = True
        aNum += 1
    perfSquaresDict[0] = maxBase * maxBase
    return perfSquaresList, perfSquaresDict


if __name__ == '__main__':

    startTime = time()
    #perfSquaresList, perfSquaresDict = genPerfSquareListDict(10000000)
    print("\nFinished generating list & dict of perfect squares\n\n")
    aNum = 1

    goldenNuggets = []
    while len(goldenNuggets) < 5:
        aNumSquared = aNum * aNum
        testNum = 5*aNumSquared -4
        if round((testNum ** 0.5),14) % 1 == 0:
            #testNumInt = int(round((testNum ** 0.5),0))
            #n = round((testNum**0.5 - 1)/5,4)
            if (testNum**0.5 - 1) % 5 == 0:
                n = (testNum**0.5 - 1)/5
                if n == 0:
                    aNum += 1
                    continue
                #x = infPolyFibInv(n)
                x = (-n-1+(5*n*n+2*n+1)**0.5)/(2*n)
                print("Found one: anumSquared:", aNumSquared, ", testNum:", testNum,
                      ", n:", n, ", x:", x, flush=True)
                goldenNuggets.append([x, n, aNum, aNumSquared, testNum])
        aNum += 1

    totalTime = time() - startTime
    
    # O(1) method from somewhere on web
    aNugFast = []
    for i in range(1, 15+1):
        aNugFast.append(fibN(2*i)*fibN(2*i+1))
    
    
    #print("\n\nThe 15th golden nugget is", goldenNuggets[15-1][1],
    #"with an x of", goldenNuggets[15-1][0])
    print("\nAll golden nuggets found:\n[x, Nugget]")
    for aNuggetNo, aNugget in enumerate(goldenNuggets):
        print(str(aNuggetNo+1)+":", aNugget)
    print("\nFound", len(goldenNuggets))
    print("Time to find:", totalTime)
    
    print("\nAll golden nuggets found with fast method:\nNugget")
    for aNuggetNo, aNugget in enumerate(aNugFast):
        print(str(aNuggetNo+1)+":", aNugget)
    print("\nFound", len(aNugFast))

"""

Result




"""

"""
Found one: anumSquared: 25 , testNum: 121 , n: 2.0 , x: 0.5
Found one: anumSquared: 1156 , testNum: 5776 , n: 15.0 , x: 0.6
Found one: anumSquared: 54289 , testNum: 271441 , n: 104.0 , x: 0.6153846153846154
Found one: anumSquared: 2550409 , testNum: 12752041 , n: 714.0 , x: 0.6176470588235294
Found one: anumSquared: 119814916 , testNum: 599074576 , n: 4895.0 , x: 0.6179775280898876
Found one: anumSquared: 5628750625 , testNum: 28143753121 , n: 33552.0 , x: 0.6180257510729614
Found one: anumSquared: 264431464441 , testNum: 1322157322201 , n: 229970.0 , x: 0.6180327868852459
Found one: anumSquared: 12422650078084 , testNum: 62113250390416 , n: 1576239.0 , x: 0.6180338134001252
Found one: anumSquared: 583600122205489 , testNum: 2918000611027441 , n: 10803704.0 , x: 0.6180339631667066
Found one: anumSquared: 9000123176502441 , testNum: 45000615882512201 , n: 42426697.0 , x: 0.6180339822352893
Found one: anumSquared: 27416783093579881 , testNum: 137083915467899401 , n: 74049690.0 , x: 0.618033985017358
Found one: anumSquared: 55833579873437809 , testNum: 279167899367189041 , n: 105672683.0 , x: 0.6180339861343352
Found one: anumSquared: 64000875921795136 , testNum: 320004379608975676 , n: 113137859.0 , x: 0.6180339863069177
Found one: anumSquared: 94250513516076225 , testNum: 471252567580381121 , n: 137295676.0 , x: 0.6180339867367709
Found one: anumSquared: 104778521648351236 , testNum: 523892608241756176 , n: 144760852.0 , x: 0.6180339868405859
Found one: anumSquared: 155556304237687824 , testNum: 777781521188439116 , n: 176383845.0 , x: 0.6180339871828965
Found one: anumSquared: 216334223689804900 , testNum: 1081671118449024496 , n: 208006838.0 , x: 0.618033987421125


The 15th golden nugget is 144760852.0 with an x of 0.6180339868405859

All golden nuggets found:
[x, Nugget]
1: [0.5, 2.0, 5, 25, 121]
2: [0.6, 15.0, 34, 1156, 5776]
3: [0.6153846153846154, 104.0, 233, 54289, 271441]
4: [0.6176470588235294, 714.0, 1597, 2550409, 12752041]
5: [0.6179775280898876, 4895.0, 10946, 119814916, 599074576]
6: [0.6180257510729614, 33552.0, 75025, 5628750625, 28143753121]
7: [0.6180327868852459, 229970.0, 514229, 264431464441, 1322157322201]
8: [0.6180338134001252, 1576239.0, 3524578, 12422650078084, 62113250390416]
9: [0.6180339631667066, 10803704.0, 24157817, 583600122205489, 2918000611027441]
10: [0.6180339822352893, 42426697.0, 94868979, 9000123176502441, 45000615882512201]
11: [0.618033985017358, 74049690.0, 165580141, 27416783093579881, 137083915467899401]
12: [0.6180339861343352, 105672683.0, 236291303, 55833579873437809, 279167899367189041]
13: [0.6180339863069177, 113137859.0, 252983944, 64000875921795136, 320004379608975676]
14: [0.6180339867367709, 137295676.0, 307002465, 94250513516076225, 471252567580381121]
15: [0.6180339868405859, 144760852.0, 323695106, 104778521648351236, 523892608241756176]
16: [0.6180339871828965, 176383845.0, 394406268, 155556304237687824, 777781521188439116]
17: [0.618033987421125, 208006838.0, 465117430, 216334223689804900, 1081671118449024496]

Found 17
Time to find: 1003.1574664115906
"""