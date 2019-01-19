# -*- coding: utf-8 -*-
"""
Project Euler

Exploring the number of different ways a number can be expressed as a sum of
powers of 2
Problem 169s

Define f(0)=1 and f(n) to be the number of different ways n can be expressed
as a sum of integer powers of 2 using each power no more than twice.

For example, f(10)=5 since there are five different ways to express 10:

1 + 1 + 8
1 + 1 + 4 + 4
1 + 1 + 2 + 2 + 4
2 + 4 + 4
2 + 8

What is f(10**25)?

Created on Fri Jan 18 13:00:00 2019

@author: PaulJ
"""

from time import time
# import math


def build_max_below(pow_2, max_value):
    max_below = {1: 2}
    # old_2_pow = 1
    # while old_2_pow * 2 <= max_value:
    for new_2_pow in pow_2[1:]:
        old_2_pow = new_2_pow / 2
        # new_2_pow = old_2_pow * 2
        max_below[new_2_pow] = max_below[old_2_pow] + 2 * new_2_pow
        old_2_pow = new_2_pow
    return max_below


def build_2_pow_list(max_sum):
    pow_2 = [1]
    while pow_2[-1] < max_sum:
        pow_2.append(pow_2[-1] * 2)
    pow_2 = pow_2[:-1]
    return pow_2


def build_sum_below_dict(n):
    pass


if __name__ == '__main__':
    startTime = time()
    print('\n')

    max_sum = 1000  # 1e25
    fs_of_max_sums = {}

    for max_sum in [1e1, 1e2, 1e3, 1e4, 1e5]:
        pow_2s = build_2_pow_list(max_sum)

        # max_below = build_max_below(pow_2s, max_sum)

        sums_below = {1: {0: [[0]],
                          1: [[1]],
                          2: [[2]]}}

        for this_2_pow in range(1, len(pow_2s)):  # 1, 2, 3, 4, 5, ...
            prev_2_pow = this_2_pow - 1        # 0, 1, 2, 3, 4, ...
            # print('this_2_pow:', this_2_pow)
            this_pow_2 = 2 ** this_2_pow  # e.g 2, 4, 8, 16, 32, ...
            prev_pow_2 = int(this_pow_2 / 2)  # 1, 2, 4, 8, 16, 32, ...
            these_sums = {}
            # print('sums_below[prev_pow_2]:', sums_below[prev_pow_2])
            for a_prev_sum_below in sums_below[prev_pow_2]:
                # print('a_prev_sum_below:', a_prev_sum_below)
                for a_prev_sum_combo in sums_below[prev_pow_2][a_prev_sum_below]:
                    for no_new_2_pow in range(2+1):
                        new_sum = a_prev_sum_below + this_pow_2 * no_new_2_pow
                        if new_sum > max_sum:
                            continue
                        if new_sum in these_sums:
                            curr_new_sum_combo = these_sums[new_sum]
                            curr_new_sum_combo.append(
                                a_prev_sum_combo + [no_new_2_pow])
                        else:
                            curr_new_sum_combo = [a_prev_sum_combo +
                                                  [no_new_2_pow]]
                        # print('curr_new_sum_combo:', curr_new_sum_combo,
                        #       ', new_sum:', new_sum)
                        these_sums[new_sum] = curr_new_sum_combo
            # print('this_pow_2:', this_pow_2, ', these_sums:\n', these_sums)
            # sums_below[this_pow_2] = these_sums
            sums_below = {this_pow_2: these_sums.copy()}
            # print('sums_below:\n', sums_below)

        fs_of_max_sums[max_sum] = len(sums_below[this_pow_2][max_sum])
        print('fs_of_max_sums:', fs_of_max_sums)

    totalTime = time() - startTime
    print('\nf(' + str(max_sum) + ') = ', len(sums_below[this_pow_2][max_sum]))
    print('Time to find:', '{:,.3f} s'.format(totalTime))

"""
Result:


    
"""



