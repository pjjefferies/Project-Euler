# -*- coding: utf-8 -*-
"""
Project Euler

Problem 22: Names scores

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

"""

from time import time


if __name__ == '__main__':
    startTime = time()

    with open("p022_names.txt", "r") as nameFile:
        textListOfNames = nameFile.read()

    textListOfNames = textListOfNames.replace('"', '')
    listOfNames = textListOfNames.split(",")
    
    listOfNames.sort()
    
    nameScoreTotal = 0
    
    for nameCount in range(len(listOfNames)):
        nameScore = 0
        for aChar in listOfNames[nameCount]:
            nameScore += ord(aChar) - 64
        nameScoreTotal += (nameCount + 1) * nameScore
    
    totalTime = time() - startTime
    print("The total of all of the name scores is", nameScoreTotal)
    print("Time to find:", totalTime)

"""

Result

The total of all of the name scores is 871198282
Time to find: 0.024000883102416992

"""
