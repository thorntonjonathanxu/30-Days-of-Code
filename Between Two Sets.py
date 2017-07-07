#!/bin/python3
#HackerRankTeam - Between Two Sets
#7-6-2017 @Author - Jonathan Thornton
#https://www.hackerrank.com/challenges/between-two-sets

#Input
#First line contains the number of digits for both m and n
#Second and Third line contains the list of digits for m and n respectively. 
#Values ranging between 1~100

import sys


def getTotal(a, b):
    # Complete this function

    #Finds the range from the largest value in A and smallest in B
    maxA = max(setA)
    minB = min(setB)
    count = 0
    for num in range(maxA,minB+1):
        left = all([num % numA == 0 for numA in setA])      #finds all values in the set where each value is a common denominator
        right = all([numB % num == 0 for numB in setB])     #Compares each value to see each instance where the values were mod = 0
        count += left*right                                 #Only counts the instances where the common denominator exists in both sets
    return count

#Test Case
# lenA, lenB = (2,3)
# setA = [2,4]   
# setB = [16,32,96]

#Inputs
lenA, lenB = map(int,input().split())     #loads in the length of each respective set
setA = list(map(int,input().split()))     #Inputs the list of items in A
setB = list(map(int,input().split()))     #Inputs the list of items in B

#Solution
total = getTotal(lenA,lenB)
print(total)
