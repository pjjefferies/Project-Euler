# -*- coding: utf-8 -*-
"""
Project Euler

Problem 39: Integer right triangles

If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

"""

"""

Analysis

a + b + c = p, p <= 1000
a^2 + b^2 = c^2
a, b <= c - 1, a, b <= p - 3

"""

from time import time


if __name__ == '__main__':
    startTime = time()

    solutions = {}
    pMax = 1000
    
    for anA in range(pMax - 2):
        for aB in range(anA, pMax-2):
            c = (anA * anA + aB * aB) ** (0.5)
            if round(c,3) != float(int(c)):
                continue
            p = anA + aB + round(c)
            if p > pMax:
                continue
            solutions[p] = solutions.get(p,0) + 1   #?

    sol = max(solutions.keys(), key=(lambda k:solutions[k]))

    totalTime = time() - startTime
    print("\n\nThe value of p <= 1000 with a maximum number of solutions is",
          sol)
    print("Time to find:", '{:,.3f}'.format(totalTime))


"""
Result:

The value of p <= 1000 with a maximum number of solutions is 840
Time to find: 2.788

"""