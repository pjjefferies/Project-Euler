# -*- coding: utf-8 -*-
"""
Project Euler

Problem 79: Passcode derivation

A common security method used for online banking is to ask the user for three
random characters from a passcode. For example, if the passcode was 531278,
they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be:
317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file
so as to determine the shortest possible secret passcode of unknown length.

Analysis



"""


from time import time







if __name__ == '__main__':
    startTime = time()
    print("\n\n")

    passcode = ""
    
    listOfTrys = []
    with open("p079_keylog.txt", "r") as nameFile:
        for line in nameFile:
            listOfTrys.append(int(line))

    
    orderMatrix = []
    for i in range(10):
        orderMatrix += [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for aTry in listOfTrys:
        aTryStr = str(aTry)
        aTriFC = int(aTryStr[0])
        aTriSC = int(aTryStr[1])
        aTriTC = int(aTryStr[2])
        orderMatrix[aTriFC][aTriSC] = -1
        orderMatrix[aTriSC][aTriFC] = +1
        orderMatrix[aTriFC][aTriTC] = -1
        orderMatrix[aTriTC][aTriFC] = +1
        orderMatrix[aTriSC][aTriTC] = -1
        orderMatrix[aTriTC][aTriSC] = +1
        
    for aLineNo, aLine in enumerate(orderMatrix):
        print(str(aLineNo)+":", aLine)


    totalTime = time() - startTime
    print("\nThe shortest possible secret passcode is", passcode)
    print("Time to find:", '{:,.3f}'.format(totalTime))

"""
Result:



"""
