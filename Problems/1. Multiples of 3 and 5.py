# -*- coding: utf-8 -*-
"""
Project Euler

Problem 1

Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def isAMultiple(dividend, divisor):
    return ((dividend % divisor) == 0)


def isAMultipleOf3Or5(value):
    return (isAMultiple(value, 3) or isAMultiple(value, 5))


def sumDivisibleBy(dividend, divisor):
    return int((divisor * (dividend // divisor) * (dividend // divisor + 1) / 2))


if __name__ == '__main__':
    #Iterative Method
    totalOfMultiples = 0
    for i in range(1000):
        if isAMultipleOf3Or5(i):
            totalOfMultiples += i
    print("The sum of all the multiples of 3 or 5 below 1000 is", totalOfMultiples)
    
    #Mathematical Method
    totalOfMultiples = sumDivisibleBy(999, 3) + sumDivisibleBy(999, 5) - sumDivisibleBy(999, 15)
    print("The sum of all the multiples of 3 or 5 below 1000 is", totalOfMultiples)


"""

sum = sumDivisible(3) + sumDivisible(5) - sumDivisible(15)

e.g. sumDivisible(3) (from 1 to n) = 3+6+9+12+..+largest value up to n

    sum(1, 2, 3, ..., n) = n * (n + 1) / 2

     divisible by 3 = 3 * (1+2+3+4+...+largest value up to n divisible by 3 / 3)
                    = 3 * (1+3+3+4+...+n \ 3)
                    = 3 * (1/2*[(n/3)*(n/3 + 1)]

"""