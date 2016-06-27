# -*- coding: utf-8 -*-
"""
Project Euler

Problem 25: 1000-digit Fibonacci number

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain
1000 digits?



"""

from time import time


if __name__ == '__main__':
    startTime = time()

    noDigitsToFind = 1000
    numberToExceed = 10 ** (noDigitsToFind - 1)
    fN = 1
    n  = 2
    fNMinusOne = 1

    while True:
        fNext = fN + fNMinusOne
        fNMinusOne = fN
        fN = fNext
        n += 1
        if fN >= numberToExceed:
            break
    
    totalTime = time() - startTime
    print("The", str(n)+"th Fibonacci number is the first to contain",
          noDigitsToFind, "digits.")
    print("Time to find:", totalTime)

"""

Result

The 4782th Fibonacci number is the first to contain 1000 digits.
Time to find: 0.015635013580322266

"""
