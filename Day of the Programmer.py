#!/bin/python3
#HackerRankTeam - Day of the Programmer
#7-8-2017 @Author - Jonathan Thornton
#https://www.hackerrank.com/challenges/day-of-the-programmer

#This calculates the 256th day of the year based on the Julian and the Gregorian
#calendars. 

import sys

def solve(year):
    # Complete this function

    if (year == 1918):
        return '26.09.1918'
    elif ((year <= 1917) & (year%4 == 0)) or ((year > 1918) & (year%400 == 0 or ((year%4 == 0) & (year%100 != 0)))):
        return '12.09.%s' %year
    else:
        return '13.09.%s' %year
    
#Test Case 1:
#year = 1917
#Expected Output: 13.09.2017

#Custom User Input
year = int(input().strip())
result = solve(year)
print(result)
