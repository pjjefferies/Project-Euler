# -*- coding: utf-8 -*-
"""
Project Euler

Problem 19: Counting Sundays

You are given the following information, but you may prefer to do some research
for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century
unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?

"""

from time import time

def nextDay(currentDate):    #currentDay as a dict {day: #, month: #, year: ####]
    if currentDate["day"] < 28:
        currentDate["day"] = currentDate["day"] + 1
        return currentDate
    if currentDate["month"] == 1 and currentDate["day"] == 31:
        currentDate["month"] = 2
        currentDate["day"] = 1
        return currentDate
    if currentDate["month"] == 3 and currentDate["day"] == 31:
        currentDate["month"] = 4
        currentDate["day"] = 1
        return currentDate
    if currentDate["month"] == 4 and currentDate["day"] == 30:
        currentDate["month"] = 5
        currentDate["day"] = 1
        return currentDate
    if currentDate["month"] == 5 and currentDate["day"] == 31:
        currentDate["month"] = 6
        currentDate["day"] = 1
        return currentDate
    if currentDate["month"] == 6 and currentDate["day"] == 30:
        currentDate["month"] = 7
        currentDate["day"] = 1
        return currentDate
    if currentDate["month"] == 7 and currentDate["day"] == 31:
        currentDate["month"] = 8
        currentDate["day"] = 1
        return currentDate
    if currentDate["month"] == 8 and currentDate["day"] == 31:
        currentDate["month"] = 9
        currentDate["day"] = 1
        return currentDate
    if currentDate["month"] == 9 and currentDate["day"] == 30:
        currentDate["month"] = 10
        currentDate["day"] = 1
        return currentDate
    if currentDate["month"] == 10 and currentDate["day"] == 31:
        currentDate["month"] = 11
        currentDate["day"] = 1
        return currentDate
    if currentDate["month"] == 11 and currentDate["day"] == 30:
        currentDate["month"] = 12
        currentDate["day"] = 1
        return currentDate
    if currentDate["month"] == 12 and currentDate["day"] == 31:
        currentDate["year"] = currentDate["year"] + 1
        currentDate["month"] = 1
        currentDate["day"] = 1
        return currentDate
    if (currentDate["month"] == 2 and currentDate["day"] == 29 and
        (currentDate["year"] % 4 == 0 and (currentDate["year"] % 100 != 0 or
                                           currentDate["year"] % 400 == 0))):
        currentDate["month"] = 3
        currentDate["day"] = 1
        return currentDate
    if (currentDate["month"] == 2 and currentDate["day"] == 28 and
        (currentDate["year"] % 4 != 0 or (currentDate["year"] % 100 == 0 and
                                          currentDate["year"] % 400 != 0))):
        currentDate["month"] = 3
        currentDate["day"] = 1
        return currentDate
    currentDate["day"] = currentDate["day"] + 1
    return currentDate



if __name__ == '__main__':
    startTime = time()
    print("\n\n")

    currentDate = {"day": 1, "month": 1, "year": 1900}
    dayOfWeek = 0   # 0 = Monday
    
    startTarget = {"day": 1, "month": 1, "year": 1901}
    
    while currentDate != startTarget:
        currentDate = nextDay(currentDate)
        dayOfWeek = (dayOfWeek + 1) % 7
        #print(currentDate, dayOfWeek)
        
    print("Start day of:", currentDate, "is", dayOfWeek)
    
    endTargetPlusOne = {"day": 1, "month": 1, "year": 2001}
    sundayOnFirsts = 0

    while currentDate != endTargetPlusOne:
        currentDate = nextDay(currentDate)
        dayOfWeek = (dayOfWeek + 1) % 7
        if currentDate["day"] == 1 and dayOfWeek == 6:
            sundayOnFirsts += 1
        #print(currentDate, dayOfWeek, sundayOnFirsts)

    totalTime = time() - startTime
    print("There are", sundayOnFirsts, "Sundays that fall-on the first of the",
          "months in the twentieth century")
    print("Time to find:", totalTime)


"""

Result

Start day of: {'month': 1, 'day': 1, 'year': 1901} is 1
There are 171 Sundays that fall-on the first of the months in the twentieth century
Time to find: 0.06100296974182129

"""