#!/bin/python3
#HackerRankTeam - Birthday Chocolate
#7-6-2017 @Author - Jonathan Thornton
#https://www.hackerrank.com/challenges/the-birthday-bar

import sys

def solve(size, squares, day, month):
    #Builds a list with all possible subsets with values of True and False cases
    check = [sum(squares[nums:nums+month]) == day for nums in range(0,len(squares))]    #check is a list of booleans
    count = check.count(True)                                                           #Counts all instances where set was validated

    # count = sum(sum(squares[nums:nums+month]) == day for nums in range(0,len(squares)))      #One line solution

    return count
#Test Cases 1
# size = 6
# squares = [1,1,1,1,1,1]
# day, month = (3,2)
#Output 0

#Test Cases 2
# size = 1
# squares = [4]
# day, month = (4,1)
#Output 1

#Test Cases 3
# size = 5
# squares = [1,2,1,3,2] 
# day, month = [3,2]
# Output 2

#Custom User Input:
size = int(input().strip())
squares = list(map(int, input().strip().split(' ')))
day, month = input().strip().split(' ')
day, month = [int(day), int(month)]
result = solve(size, squares, day, month)
print(result)