# -*- coding: utf-8 -*-
"""
Project Euler

Problem 28: Number spiral diagonals

Starting with the number 1 and moving to the right in a clockwise direction
a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
in the same way?

"""

from time import time



if __name__ == '__main__':
    startTime = time()
    matrixSize = 1001
    matrixSize = 1001     #for debug

    matrix = []
    for row in range(matrixSize):
        matrix.append([0]*matrixSize)

    locCol = matrixSize // 2
    locRow = matrixSize // 2
    numCount = 1
    
    matrix[locRow][locCol] = numCount
    numCount += 1   #increment number to start first box
    locCol += 1     #Move out of currnet box to start new box
    
    while locCol < matrixSize:
        colCount = 1
        print("Starting new box. locRow:", locRow, ", locCol:", locCol,
        ", numCount:", numCount)
        #print("Before first while. locRow:", locRow, ", locCol:", locCol,
        #      "matrix[locRow][locCol-1]:", matrix[locRow][locCol-1])
        while matrix[locRow][locCol-1] > 0:     #create left side of box
            #print("Drawing RH. locRow:", locRow, ", locCol:", locCol,
            #", numCount:", numCount)
            matrix[locRow][locCol] = numCount    #fill in number
            locRow += 1                         #go to next row
            numCount += 1                       #increment number
        while matrix[locRow-1][locCol] > 0:     #create bottom side of box
            #print("Drawing BT. locRow:", locRow, ", locCol:", locCol,
            #", numCount:", numCount, ", colCount:", colCount)
            matrix[locRow][locCol] = numCount    #fill in number
            locCol -= 1                         #go to next row
            numCount += 1                       #increment number
            colCount += 1                       #count col. to use on top
        while matrix[locRow][locCol+1] > 0:     #create left side of box
            #print("Drawing LH. locRow:", locRow, ", locCol:", locCol,
            #", numCount:", numCount)
            matrix[locRow][locCol] = numCount    #fill in number
            locRow -= 1                         #go to next row
            numCount += 1                       #increment number
        for aCol in range(colCount):            #create top side of box
            #print("Drawing TT. locRow:", locRow, ", locCol:", locCol,
            #", numCount:", numCount, ", aCol:", aCol)
            matrix[locRow][locCol] = numCount    #fill in number
            locCol += 1                         #go to next row
            numCount += 1                       #increment number
        
    diagonalSum = 1
    for aRow in range(matrixSize // 2):
        #print("1:", aRow, diagonalSum)
        diagonalSum += (matrix[aRow][aRow])
        #print("2:", aRow, diagonalSum)
        diagonalSum += (matrix[matrixSize - aRow - 1][aRow])
        #print("3:", aRow, diagonalSum)
        diagonalSum += (matrix[aRow][matrixSize - aRow - 1])
        #print("4:", aRow, diagonalSum)
        diagonalSum += (matrix[matrixSize - aRow - 1][matrixSize - aRow - 1])
        #print("5:", aRow, diagonalSum)
        
        

    totalTime = time() - startTime
    print("The sum the numbers on the diagonals in a", matrixSize, "x",
          matrixSize, "spiral is", diagonalSum)
    print("Time to find:", totalTime)


"""
Result:

The sum the numbers on the diagonals in a 1001 x 1001 spiral is 669171001
Time to find: 1.1846308708190918

"""