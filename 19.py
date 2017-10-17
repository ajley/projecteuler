'''You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

'''

# sunday = 0 so %7 ==0 is check for sunday

months = [31,28,31,30,31,30,31,31,30,31,30,31]
monthsLeap = [31,29,31,30,31,30,31,31,30,31,30,31]


def isLeapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False


def countSundays(year,start):
    endDay = start
    count = 0
    if isLeapYear(year):
        for month in monthsLeap:
            if endDay % 7 == 0:
                count += 1
            endDay += month
    else:
        for month in months:
            if endDay % 7 == 0:
                count += 1
            endDay += month

    return(count,endDay)

startDay = 1 # a Monday
startYear = 1900
endYear = 2001
totalCount = 0

for year in range(startYear,endYear):
    res = countSundays(year,startDay)
    totalCount += res[0]
    startDay = res[1]




print(totalCount - countSundays(1900,1)[0])

