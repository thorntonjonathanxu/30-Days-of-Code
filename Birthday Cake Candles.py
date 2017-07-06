#!/bin/python3
#HackerRankTeam - Birthday Cake Candles
#7-6-2017 @Author - Jonathan Thornton

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    highest = 0
    i = 0
    count = 0
    
    while i < n:
        if ar[i] == highest:
            count += 1
        if ar[i] > highest:
            highest = ar[i]
            count = 1
        i += 1
        #Formatting checks to double check increments
        #print('Count: ' + str(count))
        #print('Highest: ' + str(highest))
    return count

# n = 4
# ar = [3,2,1,3]
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
