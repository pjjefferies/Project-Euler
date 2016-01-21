# -*- coding: utf-8 -*-
"""
Project Euler

Problem 18: Maximum path sum I

By starting at the top of the triangle below and moving to adjacent numbers
on the row below, the maximum total from top to bottom is 23.

  3
 7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

           75
          95 64
         17 47 82
        18 35 87 10
        20 04 82 47 65
       19 01 23 75 03 34
      88 02 77 73 07 63 67
     99 65 04 28 06 16 70 92
     41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
   53 71 44 65 25 43 91 52 97 51 14
  70 11 33 28 77 73 17 78 39 68 17 57
  91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem
by trying every route. However, Problem 67, is the same challenge with a
triangle containing one-hundred rows; it cannot be solved by brute force, and
requires a clever method! ;o)

"""

from time import time


if __name__ == '__main__':
    startTime = time()
    print("\n\n")
    nodeList = [75,
                95,64,
                17,47,82,
                18,35,87,10,
                20, 4,82,47,65,
                19, 1,23,75, 3,34,
                88, 2,77,73, 7,63,67,
                99,65, 4,28, 6,16,70,92,
                41,41,26,56,83,40,80,70,33,
                41,48,72,33,47,32,37,16,94,29,
                53,71,44,65,25,43,91,52,97,51,14,
                70,11,33,28,77,73,17,78,39,68,17,57,
                91,71,52,38,17,14,91,43,58,50,27,29,48,
                63,66, 4,68,89,53,67,30,73,16,69,87,40,31,
                 4,62,98,27,23, 9,70,98,73,93,38,53,60, 4,23]
                
    triHeight = 15

    node = [[None for x in range(triHeight+1)] for x in range(triHeight+1)]
 
    for row in range(1, triHeight+1):   #Create binary tree
        rowStart = 0
        for rowTemp in range(1, row):
            rowStart += rowTemp
        for col in range(1,row+1):
            seqNo = rowStart + col - 1
            if row < triHeight:
                node[row][col] = [nodeList[seqNo], None, None] #No, max down, path
                #node[row][col] = [nodeList[seqNo], [row+1,col], [row+1,col+1]]
            else:
                node[row][col] = [nodeList[seqNo], nodeList[seqNo], [col]]
                #node[row][col] = [nodeList[seqNo], None, None]


    for row in range(triHeight-1, 0, -1):
        for col in range(1, row+1):
            if node[row+1][col][1] > node[row+1][col+1][1]:
                #print("In if, row:", row, ", col:", col, ", 1st arg, 2nd arg:", node[row+1][col][0], node[row+1][col+1][0])
                node[row][col][1] = node[row][col][0] + node[row+1][col][1]
                node[row][col][2] = [col] + node[row+1][col][2]
            else:
                node[row][col][1] = node[row][col][0] + node[row+1][col+1][1]
                node[row][col][2] = [col] + node[row+1][col+1][2]
        #print(node[row])

   
    totalTime = time() - startTime
    print("The maximum total from top to bottom is", node[1][1][1])
    print("The column path of the maximum total from top to bottom is", node[1][1][2])    
    print("Time to find:", totalTime)


"""

Result

The maximum total from top to bottom is 1074
The column path of the maximum total from top to bottom is [1, 2, 3, 3, 3, 4, 4, 4, 5, 6, 7, 8, 9, 9, 10]
Time to find: 0.001001119613647461

"""