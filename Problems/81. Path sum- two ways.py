# -*- coding: utf-8 -*-
"""
Project Euler

Problem 81: Path sum: two ways

In the 5 by 5 matrix below, the minimal path sum from the top left to the
bottom right, by only moving to the right and down, is indicated in bold red
and is equal to 2427.

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target
As..."), a 31K text file containing a 80 by 80 matrix, from the top left to
the bottom right by only moving right and down.
"""

from time import time
#import csv
import pandas as pd

numMatrixFilename = "p081_matrix.txt"
#numMatrixFilename = "p081_matrix_test.txt"   #for test
verbose = False

class sqSpace(object):
    def __init__(self, value):
        self.value = value
        self.sumIncBel = 0
        self.minValPath = ""
    def __str__(self):
        return("\nMin Sum of path: " + self.minValPath + " is : "
               + str(self.sumIncBel))

if __name__ == '__main__':
    startTime = time()
    print("\n\n")

    try:
        numMatrix = pd.read_csv(numMatrixFilename,
                                sep=",",
                                engine="c",
                                index_col=None,
                                header=None,
                                names=None)
    except(OSError, ValueError):
        print("Input File not found")
        exit()
    
    matrixSize = len(numMatrix)
    
    #initialize matrix to be filled with sqSpace objects
    theGrid = [[0]*matrixSize for i in range(matrixSize)]
    
    #fill matrix with sqSpace objects with values from file
    for row in range(matrixSize):
        for col in range(matrixSize):
            theGrid[row][col] = sqSpace(numMatrix[col][row]) #have to invert, input backwards
    
    #start from lower left and find best path to lower left from each square
    #working our way toward upper right
    for drRow in range(matrixSize-1, -1, -1):   #from diagonal column
        for urCol in range(matrixSize- drRow):  #from bottom row
            col = drRow + urCol
            row = matrixSize - urCol - 1
            if verbose: print("Bottom Half: row:", row, ", col:", col,
                              ", drRow:", drRow, ", urCol:", urCol)
            if col >= matrixSize or row >= matrixSize:
                print("Index out of range")
                exit()
            if (col == matrixSize - 1 and row == matrixSize - 1):
                theGrid[row][col].minValPath = ""
                theGrid[row][col].sumIncBel = theGrid[row][col].value
                if verbose: print("1st sec.: col==row==matrixSize",
                      theGrid[row][col].minValPath,
                      theGrid[row][col].sumIncBel)
            elif col == matrixSize -1:
                theGrid[row][col].minValPath = ("D" + theGrid[row+1][col].minValPath)
                theGrid[row][col].sumIncBel = (theGrid[row+1][col].sumIncBel
                                               + theGrid[row][col].value)
                if verbose: print("1st sec.: col==matrixSize",
                      theGrid[row][col].minValPath,
                      theGrid[row][col].sumIncBel)
            elif row == matrixSize -1:
                theGrid[row][col].minValPath = ("R" + theGrid[row][col+1].minValPath)
                theGrid[row][col].sumIncBel = (theGrid[row][col+1].sumIncBel
                                               + theGrid[row][col].value)
                if verbose: print("1st sec.: row==matrixSize",
                      theGrid[row][col].minValPath,
                      theGrid[row][col].sumIncBel)
            elif (theGrid[row+1][col].sumIncBel <= theGrid[row][col+1].sumIncBel):
                theGrid[row][col].minValPath = ("D" + theGrid[row+1][col].minValPath)
                theGrid[row][col].sumIncBel = (theGrid[row+1][col].sumIncBel
                                               + theGrid[row][col].value)
                if verbose: print("1st sec.: row <= col for path",
                      theGrid[row][col].minValPath,
                      theGrid[row][col].sumIncBel)
            elif (theGrid[row+1][col].sumIncBel > theGrid[row][col+1].sumIncBel):
                theGrid[row][col].minValPath = ("R" + theGrid[row][col+1].minValPath)
                theGrid[row][col].sumIncBel = (theGrid[row][col+1].sumIncBel
                                               + theGrid[row][col].value)
                if verbose: print("1st sec.: row > col for path",
                      theGrid[row][col].minValPath,
                      theGrid[row][col].sumIncBel)
            else:
                print("Error traversing tree, please check")
                exit()
 
    if verbose: print("")
    for drRow in range(matrixSize - 2, -1, -1):   #from diagonal column
        for urCol in range(drRow + 1):  #from bottom row
            col = urCol
            row = drRow - urCol
            if verbose: print("Top Half: row:", row, ", col:", col,
                              ", drRow:", drRow, ", urCol:", urCol)
            if (theGrid[row+1][col].sumIncBel <= theGrid[row][col+1].sumIncBel):
                theGrid[row][col].minValPath = ("D" + theGrid[row+1][col].minValPath)
                theGrid[row][col].sumIncBel = (theGrid[row+1][col].sumIncBel
                                               + theGrid[row][col].value)
                if verbose: print("2nd sec.: row <= col for path",
                      theGrid[row][col].minValPath,
                      theGrid[row][col].sumIncBel)
            elif (theGrid[row+1][col].sumIncBel > theGrid[row][col+1].sumIncBel):
                theGrid[row][col].minValPath = ("R" + theGrid[row][col+1].minValPath)
                theGrid[row][col].sumIncBel = (theGrid[row][col+1].sumIncBel
                                               + theGrid[row][col].value)
                if verbose: print("2nd sec.: row > col for path",
                      theGrid[row][col].minValPath,
                      theGrid[row][col].sumIncBel)
            else:
                print("Error traversing tree, please check")
                exit()


    
    totalTime = time() - startTime
    print(theGrid[0][0])
    print("Time to find:", '{:,.3f}'.format(totalTime))

"""
Result:

Min Sum of path: RRRRRRDRDRDRRRDRRRRRRDRRRRRRDRRRRRRDDRDRDDRRDDDDDDRDDDDDRDDRR
DRDRRRDRRDDDDDRRRDDDDDDDRRDDDDDRDDDRDRDRDRRRDDRRRDRRDDDDDDDDDRRRRRRDDDDDRRRRRD
RDRRRRDDRDRDDDDDDDR is : 427337
Time to find: 0.664

"""
