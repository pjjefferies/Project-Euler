# -*- coding: utf-8 -*-
"""
Project Euler

Problem 17: Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out
in words, how many letters would be used?

"""

from time import time
from re import sub

numWord = {1: "one",
           2: "two",
           3: "three",
           4: "four",
           5: "five",
           6: "six",
           7: "seven",
           8: "eight",
           9: "nine",
           10: "ten",
           11: "eleven",
           12: "twelve",
           13: "thirteen",
           14: "fourteen",
           15: "fifteen",
           16: "sixteen",
           17: "seventeen",
           18: "eighteen",
           19: "nineteen",
           20: "twenty",
           30: "thirty",
           40: "forty",
           50: "fifty",
           60: "sixty",
           70: "seventy",
           80: "eighty",
           90: "ninety",
           100: "hundred",
           1000: "thousand"}


def intToWord(aNum):
    aNumOnes = aNum % 10
    aNumTens = (aNum % 100 // 10) * 10
    aNumHundreds = aNum // 100
    if aNum > 1000:
        raise ValueError
    elif aNum == 1000:
        numString = "One Thousand"
    elif aNum >= 100:
        numString = numWord[aNumHundreds] + " hundred"
        #aNumHunRem = aNum % 100
        #aNumHunRemString = str(aNumHunRem)
        if aNumTens >= 20:
            numString = numString + " and " + numWord[aNumTens]
            if aNumOnes > 0:
                numString = numString + "-" + numWord[aNumOnes]
        elif aNumTens >= 10:
            numString = numString + " and " + numWord[aNumOnes + 10]
        elif aNumOnes > 0:
            numString = numString + " and " + numWord[aNumOnes]
    elif aNum >= 20:
        numString = numWord[aNumTens]
        if aNumOnes > 0:
            numString = numString + "-" + numWord[aNumOnes]
    elif aNum >= 10:
        numString = numWord[aNumOnes + 10]
    elif aNum > 0:
        numString = numWord[aNumOnes]
    return numString
    


if __name__ == '__main__':
    startTime = time()
    print("\n\n")
    
    letterCount = 0
    for n in range(1, 1000+1):
        wordText = intToWord(n)
        wordTextClean = sub(r'\W+', "", wordText)
        letterCount += len(wordTextClean)
        #print(str(n)+", ", str(wordText)+", ", str(wordTextClean)+", ", str(len(wordTextClean))+", ", letterCount)
        
    totalTime = time() - startTime
    print("The count of the characters of text of numbers from 1 to 1000 is", letterCount)
    print("Time to find:", totalTime)


"""

Result

The count of the characters of text of numbers from 1 to 1000 is 21124
Time to find: 0.014003992080688477

"""