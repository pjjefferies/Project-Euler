# -*- coding: utf-8 -*-
"""
Project Euler

Problem 64: Odd Period Square Roots

All square roots are periodic when written as continued fractions and can be
written in the form:

It can be seen that the sequence is repeating. For conciseness, we use the
notation √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats
indefinitely.

The first ten continued fraction representations of (irrational) square roots
are:

√2=[1;(2)], period=1
√3=[1;(1,2)], period=2
√5=[2;(4)], period=1
√6=[2;(2,4)], period=2
√7=[2;(1,1,1,4)], period=4
√8=[2;(1,4)], period=2
√10=[3;(6)], period=1
√11=[3;(3,6)], period=2
√12= [3;(2,6)], period=2
√13=[3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N ≤ 13, have an odd period.

How many continued fractions for N ≤ 10000 have an odd period?
"""

from time import time
import math
# from functools import reduce
from contextlib import suppress
# from p243_Resilience_cython import fracCanBeReducedPrimeProdDen
# from p243_Resilience_cython import calcResilience
# import csv
import numpy as np
# import pandas as pd

verbose = True


def generate_list_of_irrational_square_roots(max_value):
    irr_sq_roots = []
    for a_num in range(2, max_value+1):
        a = a_num**0.5
        b = int(a)
        if a != b:
            irr_sq_roots.append(a_num)
    return irr_sq_roots


def find_repeating_fraction_sequence(an_irr_sq_root):
    # print('Starting: an_irr_sq_root:', an_irr_sq_root)
    soln = []
    a0 = math.floor(an_irr_sq_root**0.5)
    num_rat = 1
    # num_irr_sq = 0
    den_rat = -a0
    den_irr_sq = an_irr_sq_root
    an_irr_no = an_irr_sq_root ** 0.5
    while True:  # While period has not been found
        # print('while: num_rat:', num_rat, 'den_rat:', den_rat)
        a = [a0]
        unred_num_mult = num_rat
        
        rationalized_num_rat = -den_rat
        rationalized_den_rat = (den_irr_sq - den_rat**2) / unred_num_mult
        
        a_next = math.floor((an_irr_no + rationalized_num_rat) /
                            rationalized_den_rat)
        
        """
        simp_num_rat = (((rationalized_num_rat /
                          rationalized_den_rat) - simp_whole) *
                          rationalized_den_rat)
        """
        simp_num_rat = (rationalized_num_rat -
                        (a_next * rationalized_den_rat))
        simp_den_rat = rationalized_den_rat
        
        new_soln = [a_next,
                    simp_num_rat,
                    simp_den_rat]
        a.append(a_next)
        if new_soln in soln:
            period = len(soln)
            break
        soln.append(new_soln)
        den_rat = simp_num_rat
        num_rat = simp_den_rat

    return period, soln


if __name__ == '__main__':
    verbose = False
    startTime = time()
    print('\n')

    maxSquareToAnalyze = 10000  # for testing. Eventually to 10,000
    odd_periods = 0
    periods = []

    irr_sq_roots = (
        generate_list_of_irrational_square_roots(maxSquareToAnalyze))

    for an_irr_sq_root in irr_sq_roots:
        period, soln = find_repeating_fraction_sequence(an_irr_sq_root)
        periods.append([an_irr_sq_root, period, soln])
        if len(soln) % 2 == 1:
            odd_periods += 1
        if verbose:
            print('an_irr_sq_root:', an_irr_sq_root,
                  # '\nsoln:\n', soln)
                  ': Period:', period)

    totalTime = time() - startTime
    print('Number of continued fractions, for N <=', str(maxSquareToAnalyze) +
          ', that have odd periods:', odd_periods)
    print('Time to find:', '{:,.3f}'.format(totalTime))

"""
Result:

Number of continued fractions, for N <= 10000, that have odd periods: 1322
Time to find: 1.323

"""
