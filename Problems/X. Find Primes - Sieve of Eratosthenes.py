# -*- coding: utf-8 -*-
"""
Project Euler


"""


from time import time
import numpy as np


def findPrimes(maxValueOfPrime):  # Sieve of Eratosthenes
    # primes = np.array([])
    maxValueOfPrime = int(maxValueOfPrime)
    # counter = 0
    # primeValues = [True] * (maxValueOfPrime + 1)
    primeValues = np.full((maxValueOfPrime + 1), True)
    primeValues[0] = False
    # primeValues[1] = False
    for aPrime in range(2, int(maxValueOfPrime**(1 / 2)) + 1):
        if primeValues[aPrime]:     # don't check if already rulled-out
            # print("Found a prime:", aPrime)
            # if counter == 1000:
            #     counter = 0
            #     print("aPrime:", aPrime)
            for numToElim in range(aPrime*2, maxValueOfPrime + 1, aPrime):
                primeValues[numToElim] = False
        # counter += 1
    """
    for aPrimeNo in range(2, len(primeValues)):
        if primeValues[aPrimeNo]:
            primes = np.append(primes, aPrimeNo)
    """
    primes = primeValues.nonzero()[0]
    return primes


if __name__ == '__main__':
    startTime = time()
    print("\n\n")

    # maxPrimeValue = 1_115_464_351
    maxPrimeValue = 6_500_000_000

    primes = findPrimes(maxPrimeValue)

    totalTime = time() - startTime
    print("Number of Primes Found with max value", str(maxPrimeValue) + ':',
          len(primes))
    print("Time to find:", '{:,.3f}'.format(totalTime))
    print('primes[:100]:', primes[:100])
    print('primes[-100:]:', primes[-100:])

    f_name = 'Primes_up_to_' + str(maxPrimeValue) + '.csv'

    np.savetxt(f_name, primes, fmt='%.0f', delimiter=',')

"""
Result:

Number of Primes Found with max value 6500000000: 301711469
Time to find: 8,365.090 (2 h 19.4 m)
primes[:100]: [  1   2   3   5   7  11  13  17  19  23  29  31  37  41  43  47
  53  59
  61  67  71  73  79  83  89  97 101 103 107 109 113 127 131 137 139 149
 151 157 163 167 173 179 181 191 193 197 199 211 223 227 229 233 239 241
 251 257 263 269 271 277 281 283 293 307 311 313 317 331 337 347 349 353
 359 367 373 379 383 389 397 401 409 419 421 431 433 439 443 449 457 461
 463 467 479 487 491 499 503 509 521 523]
primes[-100:]: [6499997887 6499997893 6499997927 6499997929 6499997939
 6499997947
 6499997951 6499998013 6499998061 6499998077 6499998079 6499998133
 6499998163 6499998179 6499998187 6499998209 6499998221 6499998251
 6499998257 6499998299 6499998301 6499998391 6499998409 6499998413
 6499998469 6499998523 6499998529 6499998581 6499998601 6499998611
 6499998613 6499998641 6499998647 6499998689 6499998719 6499998721
 6499998727 6499998763 6499998779 6499998787 6499998793 6499998803
 6499998863 6499998877 6499998887 6499998931 6499998979 6499999027
 6499999049 6499999063 6499999081 6499999097 6499999109 6499999117
 6499999133 6499999139 6499999141 6499999151 6499999213 6499999229
 6499999243 6499999271 6499999277 6499999301 6499999343 6499999349
 6499999357 6499999397 6499999399 6499999403 6499999409 6499999421
 6499999459 6499999481 6499999483 6499999543 6499999601 6499999621
 6499999637 6499999697 6499999703 6499999717 6499999729 6499999747
 6499999771 6499999787 6499999811 6499999813 6499999819 6499999837
 6499999853 6499999867 6499999873 6499999879 6499999897 6499999931
 6499999951 6499999967 6499999991 6499999993]

"""
