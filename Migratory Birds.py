#!/bin/python3
#HackerRankTeam - Migratory Birds
#7-6-2017 @Author - Jonathan Thornton
#https://www.hackerrank.com/challenges/migratory-birds

import sys

def migratoryBirds(n, ar):
    # Complete this function
    inorder = sorted(ar)
    current, tot_count, curr_count,max_group = (0,0,0,0)
    for nums in range(0,len(inorder)):
        if(inorder[nums] != current):       #Checks to see if the next item is different then previous
            current = inorder[nums]         #sets the new current value
            curr_count = 1                  #Resets count to be 1
            if(nums == 0):
                max_group = inorder[nums]
        else:
            curr_count += 1                 #Increments the current count
            if(curr_count > tot_count):     #Checks to see if current is the highest
                max_group = inorder[nums]   #sets the max group to be the current val
                tot_count = curr_count      #sets the total count to be the higher value
    return max_group

#Test Case
# n = 6
# ar = [1,4,4,4,5,3]

#Custom Input
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
