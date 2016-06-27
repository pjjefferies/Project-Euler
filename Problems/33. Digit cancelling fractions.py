# -*- coding: utf-8 -*-
"""
Project Euler

Problem 33: Digit cancelling fractinos

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.

"""

"""

Anaysis



"""

from time import time


if __name__ == '__main__':
    startTime = time()
    print("\n\n\n")

    solutions = []

    for denominator in range(11,99+1):
        dd1 = str(denominator // 10)
        dd2 = str(denominator % 10)
        for numerator in range(11, denominator):
            quotient = numerator / denominator
            nd1 = str(numerator // 10)
            nd2 = str(numerator % 10)
            if dd1 == nd1:
                if dd2 != '0':
                    secondQuotient = float(nd2) / float(dd2)
                    if secondQuotient == quotient:
                        print("Found One1:", numerator, "/", denominator, "=", quotient)
                        solutions.append((numerator, denominator, int(nd2), int(dd2), quotient))
                        continue
                    else:
                        #print("Didn't find One:", numerator, "/", denominator, "=", quotient, secondQuotient)
                        continue
            if dd1 == nd2:
                if dd2 != '0':
                    secondQuotient = float(nd1) / float(dd2)
                    if secondQuotient == quotient:
                        print("Found One2:", numerator, "/", denominator, "=", quotient)
                        solutions.append((numerator, denominator, int(nd1), int(dd2), quotient))
                        continue
                    else:
                        #print("Didn't find One:", numerator, "/", denominator, "=", quotient, secondQuotient)
                        continue
            if dd2 == nd1:
                secondQuotient = float(nd2) / float(dd1)
                if secondQuotient == quotient:
                    print("Found One3:", numerator, "/", denominator, "=", quotient)
                    solutions.append((numerator, denominator, int(nd2), int(dd1), quotient))
                    continue
                else:
                    #print("Didn't find One:", numerator, "/", denominator, "=", quotient, secondQuotient)
                    continue
            if dd2 == nd2 and nd2 != '0':
                secondQuotient = float(nd1) / float(dd1)
                if secondQuotient == quotient:
                    print("Found One4:", numerator, "/", denominator, "=", quotient)
                    solutions.append((numerator, denominator, int(nd1), int(dd1), quotient))
                    continue
                else:
                    #print("Didn't find One:", numerator, "/", denominator, "=", quotient, secondQuotient)
                    continue

    solutionsProduct = 1
    for solution in solutions:
        solutionsProduct *= (solution[2] / solution[3])

    totalTime = time() - startTime
    print("\n\nThe product of the four fractions given in lowest common terms",
          "is", solutionsProduct, "with the following fractions:", solutions)
    print("Time to find:", totalTime)


"""
Result:

The product of the four fractions given in lowest common terms is [(16, 64, 0.25), (26, 65, 0.4), (19, 95, 0.2), (49, 98, 0.5)]
Time to find: 0.06401586532592773

16/64 = 1/4
26/65 = 2/5
19/95 = 1/5
49/98 = 4/8 = 1/2
Product: 2/200 = 1/100 - denominator = 100


"""