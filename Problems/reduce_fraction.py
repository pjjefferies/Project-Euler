# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 23:52:12 2019

@author: PaulJ
"""

from find_all_factors import find_all_factors


def reduce_fraction(numerator, denominator, return_type):
    if isinstance(numerator, list):
        pass
    elif isinstance(numerator, int):
        numerator = find_all_factors(numerator)
    else:
        raise ValueError('Numerator must be list or integer')
    if isinstance(denominator, list):
        pass
    elif isinstance(denominator, int):
        denominator = find_all_factors(denominator)
    else:
        raise ValueError('Denominator must be list or integer')

    if return_type not in (list, float):
        raise ValueError('return_type must be list or float')

    for a_num_fact in numerator[:]:
        if a_num_fact in denominator:
            numerator.remove(a_num_fact)
            denominator.remove(a_num_fact)

    numerator = numerator if numerator else [1]
    denominator = denominator if denominator else [1]

    if return_type is list:
        return numerator, denominator
    else:
        return numerator/denominator


