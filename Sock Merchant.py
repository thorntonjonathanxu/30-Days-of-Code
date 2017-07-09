#!/bin/python3
#HackerRankTeam - Sock Merchant
#7-8-2017 @Author - Jonathan Thornton
#https://www.hackerrank.com/challenges/sock-merchant?h_r=next-challenge&h_v=zen

import sys
from collections import Counter

def sockMerchant(n, ar):
    #Complete this function
    sorted = ar.sort()
    pairs = 0
    i = 0
    while (i < len(ar)-1):
        if(ar[i] == ar[i+1]):
            pairs += 1      #Counts the item as a pair
            i += 2          #Skips the current node and following node (since it removes matches)
        else:
            i += 1
    return pairs


#Test Case 1
# n = 9
# ar = [10,20,20,10,10,30,50,10,20]
#Output :3

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
