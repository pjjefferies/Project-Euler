# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 12:56:51 2019

@author: PaulJ
"""


def quadratic_equation_solution(a, b, c):
    if 4*a*c > b**2:
        raise ValueError('Real roots only supported at this time')
    if 4*a*c == b**2:  # Line is tangent to ellipse
        x = -b / (2*a)
        return x, x

    num2 = (b**2 - 4*a*c)**(0.5)
    x1 = (-b + num2)/(2*a)
    x2 = (-b - num2)/(2*a)

    return x1, x2
