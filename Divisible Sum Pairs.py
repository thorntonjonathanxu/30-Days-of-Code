#!/bin/python3
#HackerRankTeam - Divisible Sum Pairs
#7-6-2017 @Author - Jonathan Thornton
#https://www.hackerrank.com/challenges/divisible-sum-pairs?h_r=next-challenge&h_v=zen


import sys

def divisibleSumPairs(n, k, ar):

    #O(n^2)
    count = 0
    for i in range(0,len(ar)):
        for j in range(1,len(ar)):
            if((i < j) and ((ar[i]+ar[j]) % k == 0)):
                count += 1
                #print(str(i) + ':' + str(j) + 'Total: '+ str(count))
    return count

#Test Input:
# n, k = (6,3)
# ar = [1,3,2,6,1,2]

#Custom User Input
n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
