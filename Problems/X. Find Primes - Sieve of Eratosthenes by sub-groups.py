# -*- coding: utf-8 -*-
"""
Created on Thu May 17 20:53:15 2018

@author: PaulJ
"""

import math


MAX_PRIMES_PER_LOOP = 500_000_000


def find_short_prime_list(primesList, initial_search_no, search_loop_size):
    primeValues = [True] * search_loop_size
    for an_old_prime in primesList:
        min_prime_mult = math.ceil(initial_search_no / an_old_prime)
        max_prime_mult = math.ceil((initial_search_no + search_loop_size) /
                                   an_old_prime)
        for prime_mult in range(min_prime_mult, max_prime_mult):
            primeValues[an_old_prime * prime_mult] = False
    for loopInc in range(search_loop_size):
        prime_try = loopInc + initial_search_no
        