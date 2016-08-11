
# coding: utf-8

# You are given the following information, but you may prefer to do some research for yourself.
# 
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# In[55]:

# assume we complete the month and start at the first of the month

def getNumDays(month, year):
    if month in [9,4,6,11]:
        return 30
    elif month == 2:
        return 29 if year%4 == 0 and (year%400 == 0 or year%100 != 0) else 28
    else:
        return 31


# In[76]:

def Euler19():
    months = range(1,13)
    years = range(1900,2001)
    countSundays = 0
    currStart = 1
    for year in years:
#         print "leapyear" if year%4 == 0 and (year%400 == 0 or year%100 != 0) else ""
        for month in months:
        
#             print "month :" + str(month) + " Year: " + str(year) + " num Days: " + str(getNumDays(month, year))
            currStart = (currStart + getNumDays(month,year))%7
#             print currStart
            if (currStart == 0):
                countSundays += 1
#             print "first of Month : " + str(currlastDayOfMonth + 1)
        
        
    return countSundays-2


# In[77]:

Euler19()

