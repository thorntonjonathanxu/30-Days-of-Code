#!/bin/python3
#HackerRankTeam - Kangaroo
#7-6-2017 @Author - Jonathan Thornton
#https://www.hackerrank.com/challenges/kangaroo

#!/bin/python3

import sys

#x is location, v is velocity for each respective kangaroo
def kangaroo(x1, v1, x2, v2):
    # Complete this function
    #Lead Kangaroo will always be ahead
    if(v1 > v2 and (x2 - x1) % (v1 - v2) == 0):
        return 'YES'
    else:
        return 'NO'

#Test Input:
# x1, v1, x2, v2 = [0,3,4,2]
x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)