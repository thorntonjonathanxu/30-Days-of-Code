#!/bin/python3
#HackerRankTeam - Breaking the Records
#7-6-2017 @Author - Jonathan Thornton
#https://www.hackerrank.com/challenges/breaking-best-and-worst-records


import sys

def getRecord(s):
    # Complete this function
    highest = score[0]
    lowest = score[0]
    h_count = 0
    l_count = 0
    for num in range(len(score)):
        if(score[num] > highest):
            highest = score[num]
            h_count += 1
        if(score[num] < lowest):
            lowest = score[num]
            l_count += 1
    print(str(h_count) + ' ' + str(l_count))

#Test Cases
# elements = 10
# score = [3,4,21,36,10,28,35,5,24,42]

#Inputs
elements = int(input().strip())
score = list(map(int, input().strip().split(' ')))
getRecord(score)
