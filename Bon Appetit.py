#!/bin/python3
#HackerRankTeam - Bon Appetit
#7-8-2017 @Author - Jonathan Thornton
#https://www.hackerrank.com/challenges/bon-appetit?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

import sys

def bonAppetit(n, k, b, ar):
    # Complete this function
    total = sum(ar)
    actual_split = int((total-ar[k])/2)
    if(actual_split == b):
        return 'Bon Appetit'
    else:
        return b - actual_split


#Test Case
# n, k = (4,1)
# ar = [3,10,2,9]
# b = 12

#Test Case
# n, k = (4,1)
# ar = [3,10,2,9]
# b = 7


n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)