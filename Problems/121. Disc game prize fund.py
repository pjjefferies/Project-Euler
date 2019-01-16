# -*- coding: utf-8 -*-
"""
Project Euler

Disc game prize fund

Problem 121 

A bag contains one red disc and one blue disc. In a game of chance a player
takes a disc at random and its colour is noted. After each turn the disc is
returned to the bag, an extra red disc is added, and another disc is taken at
random.

The player pays £1 to play and wins if they have taken more blue discs than red
discs at the end of the game.

If the game is played for four turns, the probability of a player winning is
exactly 11/120, and so the maximum prize fund the banker should allocate for
winning in this game would be £10 before they would expect to incur a loss.
Note that any payout will be a whole number of pounds and also includes the
original £1 paid to play the game, so in the example given the player actually
wins £9.

Find the maximum prize fund that should be allocated to a single game in which
fifteen turns are played.
"""

from time import time
import math

verbose = True

if __name__ == '__main__':
    verbose = False
    # solutions = []
    startTime = time()
    print('\n')
    max_number_turns = 15
    no_blue_to_win = math.ceil((max_number_turns + 0.5) / 2)
    results_encoding_max = 2**max_number_turns-1
    total_prob = 0

    for a_result_int in range(results_encoding_max + 1):
        a_result_bin_str = bin(a_result_int)[2:]
        a_result_bin_str = ('0' * (max_number_turns - len(a_result_bin_str)) +
                            a_result_bin_str)
        if a_result_bin_str.count('1') >= no_blue_to_win:
            this_prob = 1
            for a_bit_no, a_bit in enumerate(a_result_bin_str):
                if int(a_bit):
                    this_prob *= 1/(2+a_bit_no)
                else:
                    this_prob *= (1+a_bit_no)/(2+a_bit_no)
            total_prob += this_prob

    max_payout = math.floor(1/total_prob)

    totalTime = time() - startTime
    print('The probability of winning with 15 turns is', total_prob,
          '\nThe maximum profitible even unit payout with a one unit',
          'entry is', max_payout)
    print('Time to find:', '{:,.3f} s'.format(totalTime))

"""
Result:

The probability of winning with 15 turns is 0.0004406394650212371 
The maximum profitible even unit payout with a one unit entry is 2269
Time to find: 0.219 s

"""
