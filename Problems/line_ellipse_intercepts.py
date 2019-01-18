# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 13:02:09 2019

@author: PaulJ
"""

import math
from quadratic_equation_solution import quadratic_equation_solution


def line_ellipse_intercepts(line_slope, line_point_x, line_point_y,
                            ellipse_scale_a, ellipse_scale_b):
    m = line_slope
    x1 = line_point_x
    y1 = line_point_y
    a0 = ellipse_scale_a
    a02 = a0 ** 2
    b0 = ellipse_scale_b
    b02 = b0 ** 2
    mdb02 = m / b02
    if m == math.inf:
        y1_minus_m_x = -math.inf
    elif m == -math.inf:
        y1_minus_m_x = math.inf
    else:
        y1_minus_m_x = y1 - m * x1

    a1 = 1 / a02 + mdb02 * m
    b1 = 2 * mdb02 * y1_minus_m_x
    c1 = (y1_minus_m_x ** 2) / b02 - 1

    try:  # for x's
        x2_1, x2_2 = quadratic_equation_solution(a=a1, b=b1, c=c1)
    except ValueError:
        raise ValueError('Line does not intercept ellipse')

    """
    if x2_1 == x2_2:  # Line tangent to ellipse, only one point to consider
        x2 = x2_1
        y2 = m * (x2 - x1) + y1
    else:
    """
    y2_1 = m * (x2_1 - x1) + y1
    d1 = ((x2_1 - x1) ** 2 + (y2_1 - y1) ** 2) ** 0.5
    y2_2 = m * (x2_2 - x1) + y1
    d2 = ((x2_2 - x1) ** 2 + (y2_2 - y1) ** 2) ** 0.5

    # Choose x2, y2 that is furthest from x1, y1
    if d1 > d2:
        x2 = x2_1
        y2 = y2_1
    else:
        x2 = x2_2
        y2 = y2_2

    return x2, y2


if __name__ == '__main__':
    line_slope=0
    line_point_x=0
    line_point_y=10
    ellipse_scale_a=5
    ellipse_scale_b=10
    x2, y2 = line_ellipse_intercepts(line_slope, line_point_x, line_point_y,
                                     ellipse_scale_a, ellipse_scale_b)
    print('x2:', x2, '\ny2:', y2)

