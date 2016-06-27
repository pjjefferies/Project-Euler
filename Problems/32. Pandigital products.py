# -*- coding: utf-8 -*-
"""
Project Euler

Problem 32: Pandigital products

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.


"""

"""

Anaysis

X x X = XXXXXXX - doesn't work
X x XX = XXXXXX - doesn't work
X x XXX = XXXXX - doesn't work
X x XXXX = XXXX - possible space
    X in [1, 8]

XX x XX = XXXXX - doesn't work
XX x XXX = XXXX - possible space
    XX in [12, 81]
    XXX in [12, 832]

XX x XXXX = XXX - doesn't work
XXX x XXXX = XX - doesn't work

"""

from time import time


                    
            

if __name__ == '__main__':
    startTime = time()
    print("\n\n\n")

    DIGITS = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    solutionsSet = set()

    for m1 in range(1, 8+1):
        digitsRemaining1 = list(DIGITS[:])
        digitsRemaining1.remove(m1)
        #print("m1:", m1, ", digitsRemaining1:", digitsRemaining1)
        for m2d1 in digitsRemaining1:
            digitsRemaining2 = digitsRemaining1[:]
            digitsRemaining2.remove(m2d1)
            #print("m2d1:", m2d1, ", digitsRemaining2:", digitsRemaining2)
            for m2d2 in digitsRemaining2:
                digitsRemaining3 = digitsRemaining2[:]
                digitsRemaining3.remove(m2d2)
                #print("m2d2:", m2d2, ", digitsRemaining3:", digitsRemaining3)
                for m2d3 in digitsRemaining3:
                    digitsRemaining4 = digitsRemaining3[:]
                    digitsRemaining4.remove(m2d3)
                    #print("m2d3:", m2d3, ", digitsRemaining4:", digitsRemaining4)
                    for m2d4 in digitsRemaining4:
                        digitsRemaining5 = digitsRemaining4[:]
                        digitsRemaining5.remove(m2d4)
                        product = int(m1)*int(str(m2d1)+str(m2d2)+str(m2d3)+str(m2d4))
                        pda = str(product)
                        #print("pda:", pda, type(pda), ", product:", product, type(product))
                        if len(pda) != 4:
                            continue
                            print("len(pda):", len(pda), "is not 4, skip")
                        #print("len(pda):", len(pda), "is 4, check for duplicate digits")
                        #print("m1:", m1, ", m2d1:", m2d1, "m2d2:", m2d2,
                        #      ", m2d3:", m2d3, ", m2d4:", m2d4, ", digitsRemaining5:",
                        #      digitsRemaining5, ", product:", product)
                        #print(type(m1), type(m2d1), type(m2d2), type(m2d3), type(m2d4))
                        duplicateDigit = True   #check if product digits are in remaining digits
                        #print("1:digitsRemaining5:", digitsRemaining5, type(digitsRemaining5), ", pda:", pda, type(pda))
                        for remainingDigit in digitsRemaining5:
                            remainingDigitStr = str(remainingDigit)
                            if remainingDigitStr not in pda:
                                duplicateDigit = False
                                break
                        if not duplicateDigit:
                            continue
                        print("found one: m1:", m1, "* m2d1m2d2m2d3m2d4",
                              m2d1*1000+m2d2*100+m2d3*10+m2d4, "=", product)
                        solutionsSet.add(product)


    for m1d1 in range(1, 8+1):
        digitsRemaining1 = list(DIGITS[:])
        digitsRemaining1.remove(m1d1)
        for m1d2 in digitsRemaining1:
            digitsRemaining2 = digitsRemaining1[:]
            digitsRemaining2.remove(m1d2)
            for m2d1 in digitsRemaining2:
                digitsRemaining3 = digitsRemaining2[:]
                digitsRemaining3.remove(m2d1)
                for m2d2 in digitsRemaining3:
                    digitsRemaining4 = digitsRemaining3[:]
                    digitsRemaining4.remove(m2d2)
                    for m2d3 in digitsRemaining4:
                        digitsRemaining5 = digitsRemaining4[:]
                        digitsRemaining5.remove(m2d3)
                        product = (int(str(m1d1)+str(m1d2)) *
                                   int(str(m2d1)+str(m2d2)+str(m2d3)))
                        pda = str(product)
                        #print("m1d1:", m1d1, ", m1d2:", m1d2, "m2d1:", m2d1,
                        #      ", m2d2:", m2d2, ", m2d3:", m2d3, ", digitsRemaining5:",
                        #      digitsRemaining5, ", product:", product)
                        #print("pda:", pda, type(pda), ", product:", product, type(product))
                        #if m1d1 == 3 and m1d2 == 9:
                        #    print("m1d1:", m1d1, ", m1d2:", m1d2, "m2d1:", m2d1,
                        #          ", m2d2:", m2d2, ", m2d3:", m2d3, ", digitsRemaining5:",
                        #          digitsRemaining5, ", product:", product)
                        #    print("2:", type(m1), type(m2d1), type(m2d2), type(m2d3), type(m2d4))
                        if len(pda) != 4:
                            continue
                        duplicateDigit = True   #check if product digits are in remaining digits
                        #print("2:digitsRemaining5:", digitsRemaining5, type(digitsRemaining5), ", pda:", pda, type(pda))
                        for remainingDigit in digitsRemaining5:
                            remainingDigitStr = str(remainingDigit)
                            if remainingDigitStr not in pda:
                                duplicateDigit = False
                                break
                        if not duplicateDigit:
                            continue
                        #found one
                        print("found one: m1d1m1d2:", m1d1, m1d2, "* m2d1m2d2m2d3",
                              m2d1*100+m2d2*10+m2d3, "=", product)
                        solutionsSet.add(product)


    solutionSetProduct = 0
    for solution in solutionsSet:
        solutionSetProduct += solution

    totalTime = time() - startTime
    print("\n\nThe sum of all products of all pandigital products is",
          solutionSetProduct, ". The solutions are:", solutionsSet, ".")
          #"follows:", listOfCombinations)
    print("Time to find:", totalTime)


"""
Result:

found one: m1: 4 * m2d1m2d2m2d3m2d4 1738 = 6952
found one: m1: 4 * m2d1m2d2m2d3m2d4 1963 = 7852
found one: m1d1m1d2: 1 2 * m2d1m2d2m2d3 483 = 5796
found one: m1d1m1d2: 1 8 * m2d1m2d2m2d3 297 = 5346
found one: m1d1m1d2: 2 7 * m2d1m2d2m2d3 198 = 5346
found one: m1d1m1d2: 2 8 * m2d1m2d2m2d3 157 = 4396
found one: m1d1m1d2: 3 9 * m2d1m2d2m2d3 186 = 7254
found one: m1d1m1d2: 4 2 * m2d1m2d2m2d3 138 = 5796
found one: m1d1m1d2: 4 8 * m2d1m2d2m2d3 159 = 7632


The sum of all products of all pandigital products is 45228 . The solutions are: {5346, 5796, 6952, 7852, 4396, 7632, 7254} .
Time to find: 0.20199799537658691

"""