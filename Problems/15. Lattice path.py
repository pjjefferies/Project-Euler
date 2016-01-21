# -*- coding: utf-8 -*-
"""
Project Euler

Problem 15: Lattice path

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?


"""

from time import time

if __name__ == '__main__':
    startTime = time()
    print("\n\n")
    latticeWidth = 21
    latticeHeight = latticeWidth
    latticePathToPoints = [[1 for x in range(latticeWidth)] for x in range(latticeHeight)]
    for y in range(1, latticeHeight):
        for x in range(1, latticeWidth):
            latticePathToPoints[y][x] = latticePathToPoints[y][x-1] + latticePathToPoints[y-1][x]
    totalTime = time() - startTime
    print("The number of paths from upper left to lower right is", latticePathToPoints[latticeHeight-1][latticeWidth-1])
    print("Time to find:", totalTime)

"""

Result

The number of paths from upper left to lower right is 35345263800
Time to find: 0.0

"""

"""

second try, didn't work

if __name__ == '__main__':
    startTime = time()
    print("\n\n")
    latticeWidth = 20
    latticeHeight = 20
    paths = 2**(latticeWidth - 1)     #paths to middle diagonal
    paths = (paths - 2)*2 + 2         #paths to middle + 1
    print("Paths at mid-diagonal + 1 (20):", paths)
    #paths = (paths - 2)*2 + 2    #D+1
    #paths = (paths - 2*1*20)*2 + 20*2
    #paths = (paths - 2*2*20)*2 + 2*2*20
    #paths = (paths - 2*3*20)*2 + 2*3*20
    
    
    for i in range(1, latticeWidth -2):
        paths = (paths - 2*latticeWidth*i)*2 + 2*latticeWidth*i
        print("Paths at mid-diagonal +", str(i+1), "("+str(19+i+1)+"):", paths)

    totalTime = time() - startTime
    print("The number of paths from upper left to lower right is", paths)
    print("Time to find:", totalTime)

"""


""" Slow method, never finished

if __name__ == '__main__':
    startTime = time()
    print("\n\n")
    latticeWidth = 20
    latticeHeight = 20
    pathLengths = 1
    #latticeWidth = 4    #for debug
    #latticeHeight = 4   #for debug
    latticePoints = [[0 for x in range(latticeWidth)] for x in range(latticeHeight)]
    for x in range(latticeWidth):
        for y in range(latticeHeight):
            if x == latticeWidth - 1 and y == latticeHeight - 1:
                latticePoints[y][x] = [-1, -1]
            elif x == latticeWidth - 1:
                latticePoints[y][x] = [y + 1, -1]
            elif y == latticeHeight - 1:
                latticePoints[y][x] = [-1, x + 1]
            else:
                latticePoints[y][x] = [y + 1, x + 1]

    paths = [[[0,0]]]
    pathLength = (latticeWidth - 1) + (latticeHeight - 1)
    while ((len(paths[0])-1) < pathLength):
        tempPaths = []
        for pathNo in range(len(paths)):
            #print("At start of for, paths[pathNo]:", paths[pathNo])
            xCurr = paths[pathNo][-1][1]
            yCurr = paths[pathNo][-1][0]
            #if latticePoints[yCurr][xCurr][1] == -1: #if at right edge, add downward step to current path
            if xCurr == 19:
                #print("At right edge, add downward step only")
                #paths[pathNo].append([yCurr+1,xCurr]) #don't append, save mem
                paths[pathNo][-1] = [yCurr+1,xCurr]
            #elif latticePoints[yCurr][xCurr][0] == -1: #if at bottom edge, add right step to current path
            elif yCurr == 19:
                #paths[pathNo].append([yCurr,xCurr+1]) #don't append, save mem
                paths[pathNo][-1] = [yCurr+1,xCurr]  #Just save last point
                #print("At bottom edge, add rightward step only")
            else:     #otherwise, duplicate path in temp list and add right step to one and down step to other
                pathLengths += 1
                tempPaths.append(paths[pathNo][:])
                #paths[pathNo].append([yCurr,xCurr+1]) #Don't append, save mem
                paths[pathNo][-1] = [yCurr,xCurr+1]
                #tempPaths[-1].append([yCurr+1,xCurr]) #Don't append, save mem
                tempPaths[-1][-1] = [yCurr+1,xCurr]
            #print("At end of for, paths[pathNo]:", paths[pathNo])
            #print("At end of for, tempPaths    :", tempPaths)
        paths = paths + tempPaths
        #print("At end of while, paths:", paths, ". Path lengths:", (len(paths[0])-1))
        print("At end of while, path lengths:", (paths[0][0][0]+paths[0][0][1]), "of", pathLength,". Number of paths:", len(paths))
    
    totalTime = time() - startTime
    print("The number of paths from upper left to lower right is", len(paths))
    print("Time to find:", totalTime)

"""