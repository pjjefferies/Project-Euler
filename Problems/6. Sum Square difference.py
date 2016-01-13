# -*- coding: utf-8 -*-
"""
Project Euler

Problem 6

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

from time import time

if __name__ == '__main__':
    maxNumber = 100
    startTime = time()
    difference = (maxNumber*(maxNumber+1)/2)**2
    """    Inefficient method
    for i in range(1, maxNumber+1):
        difference -= i**2
    """
    
    #Efficient method
    difference -= (maxNumber/6)*(2*maxNumber+1)*(maxNumber+1)
    totalTime = time() - startTime
    print("Difference between sum of squares of first", maxNumber,
          "natural numbers and the square of the sums is:", difference)
    print("Time to find:", totalTime)






"""

Project Euler

Problem 6

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


(1 + 2 + 3 + ... + 10)^2 - (1^2 + 2^2 + ... + 10^2) =
	1*1 + 1*2 + 1*3 + ... + 1*10 + 2*1 + 2*2 + 2*3 + ... + 2*10 + ...
      + 10*1 + 10*2 + 10*3 + ... + 10*10 - 1*1 - 2*2 - 3*3 - ... - 10*10
    = 1*2 + 1*3 + ... + 1*10 + 2*1 + 2*3 + ... + 2*10 + ... + 10*1 + 10*2 + 10*9
    = 1*(2 + 3 + ... + 10) + 2*(1 + 3 + 4 + 10) + ... + 10*(1 + 2 + 3 + ... + 9)
    = 1*(1 + 2 + 3 + 10 - 1) + 2*(1 + 2 + 3 + ... + 10 - 2) + 10*(1 + 2 + 3 + ... + 10 - 10)
    = (1+2+3+...+10)*(1+2+3+...+10) + 1*(-1) + 2*(-2) + ... + 10*(-10)
    = (1+2+3+...+10)^2 - (1^2 + 2^2 + 3^2 + ... + 10^2)
    = [10*(10+1)/2]^2 - (1^2 + 2^2 + 3^2 + ... + 10^2)

For n = 100

	N = [100*(100+1)/2]^2 - (1^2 + 2^2 + 3^3 + ... + 100^2)
 
 """