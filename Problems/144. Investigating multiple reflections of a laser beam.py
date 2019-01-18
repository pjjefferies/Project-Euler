# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 22:47:34 2019

@author: PaulJ
"""

import math


def line_y_intercept(x, y, slope):
    return (y - slope * x)


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
    y1_minus_m_x = y1 - m * x1

    a1 = 1 / a02 + mdb02
    b1 = 2 * mdb02 * y1_minus_m_x
    c1 = (y1_minus_m_x ** 2) / b02 - 1

    try:
        x2_1, x2_2 = quadratic_equation_solution(a=a1, b=b1, c=c1)
    except ValueError:
        raise ValueError('Line does not intercept ellipse')

    if x2_1 == x2_2:  # Line tangent to ellipse, only one point to consider
        x2 = x2_1
        y2 = m * (x2 - x1) + y1
    else:
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
    contact_points = [[0, 10.1], [1.4, -9.6]]
    ellipse_scale_a = 5
    ellipse_scale_b =  10
    safety_counter = 0

    x_start = contact_points[-1][0]
    y_start = contact_points[-1][1]
    # b = contact_points[0][1]
    m_out = ((contact_points[-1][1] - contact_points[-2][1]) /
             (contact_points[-1][0] - contact_points[-2][0]))

    x_in = 0
    y_in = 10.1

    x_1_test, y_1_test = line_ellipse_intercepts(
            line_slope = m_out,
            line_point_x = x_in,
            line_point_y = y_in,
            ellipse_scale_a = ellipse_scale_a,
            ellipse_scale_b = ellipse_scale_b)

    if x_1_test != x_start or y_1_test != y_start:
        print('x_1_test:', x_1_test, '- y_1_test:', y_1_test)
        print('x_start:', x_start, ' - y_start:', y_start)
        raise ValueError('Line Ellipse intercept not working')

    while not (abs(contact_points[-1][0]) <= 0.01 and
               contact_points[-1][1] > 9):
        safety_counter += 1
        if safety_counter % 1000 == 0:
            print('bounce_count:', safety_counter)
        if safety_counter >= 1e6:
            break
        m_in = m_out
        x_start, y_start = contact_points[-1]

        x_end, y_end = line_ellipse_intercepts(
            line_slope = m_in,
            line_point_x = contact_points[1][0],
            line_point_y = contact_points[1][1],
            ellipse_scale_a = ellipse_scale_a,
            ellipse_scale_b = ellipse_scale_b)
        contact_points.append([x_end, y_end])
        m_tan = -4 * contact_points[-1][0] / contact_points[-1][1]
        theta_2_in = math.atan(abs((m_tan - m_in)/(1 + m_tan * m_in)))
        theta_2_out = math.pi - theta_2_in
        m_out = math.tan(theta_2_out)

    bounces = len(contact_points) - 2