# -*- coding: utf-8 -*-
"""
Project Euler

Problem 89: Roman numerals

For a number written in Roman numerals to be considered valid there are basic rules which must be followed. Even though the rules allow some numbers to be expressed in more than one way there is always a "best" way of writing a particular number.

For example, it would appear that there are at least six ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules for this problem.

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.


Analysis

   1. Translate each number to decimal
       a. Start from left
       b. Search to see if left-most is greater than next or until the
          greatest is found - convert up to that point then move to next set
          until running out of characters
   
   2. Translate decimal to reduced roman numerals
       a. one decimal character at a time - convert to roman numerals

"""


from time import time


def convRomToDec(aRomNum):
    romLetVal = {"I": 1,
                 "V": 5,
                 "X": 10,
                 "L": 50,
                 "C": 100,
                 "D": 500,
                 "M": 1000}
    aDecNum = 0
    lenRomNum = len(aRomNum)
    for aCharNum, aChar in enumerate(aRomNum):
        if aCharNum == lenRomNum - 1:
            aDecNum += romLetVal[aChar]
            continue
        if romLetVal[aChar] < romLetVal[aRomNum[aCharNum+1]]:
            aDecNum -= romLetVal[aChar]
        else:
            aDecNum += romLetVal[aChar]
    return aDecNum


def convDecToRom(aDecNum):
    aRomNum = ""
    for anM in range(aDecNum // 1000):
        aRomNum += "M"
    mRem = aDecNum % 1000
    if mRem // 900 == 1:
        aRomNum += "CM"
    elif mRem // 800 == 1:
        aRomNum += "DCCC"
    elif mRem // 700 == 1:
        aRomNum += "DCC"
    elif mRem // 600 == 1:
        aRomNum += "DC"
    elif mRem // 500 == 1:
        aRomNum += "D"
    elif mRem // 400 == 1:
        aRomNum += "CD"
    elif mRem // 300 == 1:
        aRomNum += "CCC"
    elif mRem // 200 == 1:
        aRomNum += "CC"
    elif mRem // 100 == 1:
        aRomNum += "C"
    cRem = mRem % 100
    if cRem // 90 == 1:
        aRomNum += "XC"
    elif cRem // 80 == 1:
        aRomNum += "LXXX"
    elif cRem // 70 == 1:
        aRomNum += "LXX"
    elif cRem // 60 == 1:
        aRomNum += "LX"
    elif cRem // 50 == 1:
        aRomNum += "L"
    elif cRem // 40 == 1:
        aRomNum += "XL"
    elif cRem // 30 == 1:
        aRomNum += "XXX"
    elif cRem // 20 == 1:
        aRomNum += "XX"
    elif cRem // 10 == 1:
        aRomNum += "X"
    xRem = cRem % 10
    if xRem == 9:
        aRomNum += "IX"
    elif xRem == 8:
        aRomNum += "VIII"
    elif xRem == 7:
        aRomNum += "VII"
    elif xRem == 6:
        aRomNum += "VI"
    elif xRem == 5:
        aRomNum += "V"
    elif xRem == 4:
        aRomNum += "IV"
    elif xRem == 3:
        aRomNum += "III"
    elif xRem == 2:
        aRomNum += "II"
    elif xRem == 1:
        aRomNum += "I"
    return aRomNum


if __name__ == '__main__':
    startTime = time()
    print("\n\n")

    listOfRomanNumeralsIn = []
    numCharsBefore = 0
    with open("p089_roman.txt", "r") as nameFile:
        for line in nameFile:
            listOfRomanNumeralsIn.append(line.strip().upper())
            numCharsBefore += len(listOfRomanNumeralsIn[-1])
    
    listOfDecimals = []
    
    begCount = []
    endCount = []
    diffCount = []
    
    for aRomNum in listOfRomanNumeralsIn:
        tempDec = convRomToDec(aRomNum)
        tempRom = convDecToRom(tempDec)
        listOfDecimals.append([aRomNum,
                               tempDec,
                               convDecToRom(tempDec)])
        begCount.append(len(aRomNum))
        endCount.append(len(tempRom))
        diffCount.append(begCount[-1]-endCount[-1])

    noCharsSaved = sum(diffCount)

    totalTime = time() - startTime
    print("\nThe number of characters saved by writing each of the numbers"
          "in their minimal form is", str(noCharsSaved)+".")
    print("Chars before:", sum(begCount), ", Chars after:", sum(endCount))
    print("Time to find:", '{:,.3f}'.format(totalTime))

"""
Result:

The number of characters saved by writing each of the numbersin their minimal
form is 743.
Chars before: 8850 , Chars after: 8107
Time to find: 0.027

"""
