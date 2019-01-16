# -*- coding: utf-8 -*-
"""
Project Euler

Arranged probability
Problem 100 
If a box contains twenty-one coloured discs, composed of fifteen blue discs and
 six red discs, and two discs were taken at random, it can be seen that the
probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two
blue discs at random, is a box containing eighty-five blue discs and thirty
five red discs.

By finding the first arrangement to contain over 1012 = 1,000,000,000,000 discs
in total, determine the number of blue discs that the box would contain.
"""

from time import time
import math
from reduce_fraction import reduce_fraction
from find_all_factors import find_all_factors
# from functools import reduce
# from contextlib import suppress
# from p243_Resilience_cython import fracCanBeReducedPrimeProdDen
# from p243_Resilience_cython import calcResilience
# import csv
# import numpy as np
# import pandas as pd

verbose = True
MID_GUESS_RATIO = 1 / (2 ** 0.5)
factors_cache = {}


def find_no_blue_with_prob_closest_to_50_of_picking_two_blue_discs(a_number):
    denominator = find_all_factors(a_number) + find_all_factors(a_number - 1)
    first_guess_value = math.ceil(a_number * MID_GUESS_RATIO)

    second_guess_value = first_guess_value - 1

    numerator = (find_all_factors(first_guess_value) +
                 find_all_factors(second_guess_value))

    numerator, denominator = reduce_fraction(numerator, denominator, list)

    return first_guess_value, numerator, denominator


if __name__ == '__main__':
    verbose = False
    solutions = [4]
    target_min_number = 1e12 + 1
    startTime = time()
    print('\n')

    starting_number = solutions[0] + 1
    current_number = starting_number

    while solutions[-1] < target_min_number:
        safety_catch_max_itteration = 100000
        # print('\ncurrent number:', current_number)
        no_blue_discs, numerator, denominator = (
            find_no_blue_with_prob_closest_to_50_of_picking_two_blue_discs(
                current_number))
        if numerator == [1] and denominator == [2]:
            solutions.append(current_number)
            current_number = (
                5 * current_number if len(solutions) == 1
                else math.floor(current_number ** 2 / solutions[-2]))
            # print('solution:', current_number)
        else:
            current_number += 1

    totalTime = time() - startTime
    print('\nFirst number >=', target_min_number, 'with probability of 50% of',
          'choosing 2 blue chips is', current_number, 'with',
          no_blue_discs, 'blue chips.')
    print('Time to find:', '{:,.3f} s'.format(totalTime))

"""
Result:

First number >= 1000000000001.0 with probability of 50% of choosing 2 blue
chips is 6238626641368 with 756872327473 blue chips.
Time to find: 1.420 s

The ratio between adjacent solutions approaches (1+sqrt(2))**2  (by inspection)

"""
