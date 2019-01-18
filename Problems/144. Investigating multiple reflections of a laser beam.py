# -*- coding: utf-8 -*-
"""
Project Euler

Investigating multiple reflections of a laser beam
Problem 144 

In laser physics, a "white cell" is a mirror system that acts as a delay line
for the laser beam. The beam enters the cell, bounces around on the mirrors,
and eventually works its way back out.

The specific white cell we will be considering is an ellipse with the equation
4x2 + y2 = 100

The section corresponding to −0.01 ≤ x ≤ +0.01 at the top is missing, allowing
the light to enter and exit through the hole.


The light beam in this problem starts at the point (0.0,10.1) just outside the
white cell, and the beam first impacts the mirror at (1.4,-9.6).

Each time the laser beam hits the surface of the ellipse, it follows the usual
law of reflection "angle of incidence equals angle of reflection." That is,
both the incident and reflected beams make the same angle with the normal line
at the point of incidence.

In the figure on the left, the red line shows the first two points of contact
between the laser beam and the wall of the white cell; the blue line shows the
line tangent to the ellipse at the point of incidence of the first bounce.

The slope m of the tangent line at any point (x,y) of the given ellipse is:
    m = −4x/y

The normal line is perpendicular to this tangent line at the point of
incidence.

The animation on the right shows the first 10 reflections of the beam.

How many times does the beam hit the internal surface of the white cell before exiting?

Created on Wed Jan 16 22:47:34 2019

@author: PaulJ
"""

from time import time
import math
from line_ellipse_intercepts import line_ellipse_intercepts


if __name__ == '__main__':
    startTime = time()
    print('\n')
    X = 0
    Y = 1
    LAST = -1
    contact_points = [[0, 10.1]]
    first_target_point = [1.4, -9.6]
    ellipse_scale_a = 5
    ellipse_scale_b =  10

    x_start = contact_points[LAST][X]
    y_start = contact_points[LAST][Y]
    m_out = ((first_target_point[Y] - contact_points[LAST][Y]) /
             (first_target_point[X] - contact_points[LAST][X]))

    x_1_test, y_1_test = line_ellipse_intercepts(
            line_slope = m_out,
            line_point_x = contact_points[LAST][X],
            line_point_y = contact_points[LAST][Y],
            ellipse_scale_a = ellipse_scale_a,
            ellipse_scale_b = ellipse_scale_b)

    while (not (abs(contact_points[LAST][X]) <= 0.01 and
                contact_points[LAST][Y] > 9) or
           len(contact_points) == 1):
        m_in = m_out

        x_end, y_end = line_ellipse_intercepts(
            line_slope = m_in,
            line_point_x = contact_points[LAST][X],
            line_point_y = contact_points[LAST][Y],
            ellipse_scale_a = ellipse_scale_a,
            ellipse_scale_b = ellipse_scale_b)
        contact_points.append([x_end, y_end])
        # print('last contact points:', contact_points[-1])
        m_tan = -4 * contact_points[LAST][X] / contact_points[LAST][Y]
        theta_tan = math.atan(m_tan)
        theta_2_in = math.atan(abs((m_tan - m_in)/(1 + m_tan * m_in)))
        theta_2_out = math.pi - theta_2_in
        alpha_2_out = theta_tan + theta_2_out
        m_out = math.tan(alpha_2_out)

    bounces = len(contact_points) - 2

    totalTime = time() - startTime
    print('\nThere were', bounces, 'bounces before exit')
    print('Time to find:', '{:,.3f} s'.format(totalTime))

"""
Result:

There were 354 bounces before exit
Time to find: 0.004 s
    
"""



