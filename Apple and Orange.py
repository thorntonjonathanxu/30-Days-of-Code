#!/bin/python3
#HackerRankTeam - Apple and Orange
#7-6-2017 @Author - Jonathan Thornton
#https://www.hackerrank.com/challenges/apple-and-orange

#Output
#On the first line, print the number of apples that fall on Sam's house.
#On the second line, print the number of oranges that fall on Sam's house.

import sys

#Input
# The first line contains two space-separated integers denoting the respective values of s and t . (House Length)
# The second line contains two space-separated integers denoting the respective values of a and b. (Apple Tree and Orange Tree)
# The third line contains two space-separated integers denoting the respective values of m and n. (# of Apples and # of Oranges)
# The fourth line contains  space-separated integers denoting the respective distances that each apple falls from point a. 
# The fifth line contains  space-separated integers denoting the respective distances that each orange falls from point b.

# Test Case:
# s,t = (7,11)
# a,b = (5,15)
# m,n = (3,2)
# apple = [-2,2,1]
# orange = [5,-6]

#Given Input
s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

#Initalize Tree and output count
app_adj = []
def countFruits(input_list, start_loc,h_start,h_end):
    i = 0
    count = 0
    temp_list = []
    while(i < len(input_list)):
        temp_list.append(int(input_list[i])+ start_loc)
        if (temp_list[i] <= h_end and temp_list[i] >= h_start):
            count += 1
        i += 1
    print(count) 

#-----------------------------------------------------------------------------
#Simple Solution:
#It adds one value to the list whenever it fullfills the ranged parameters
def simpleSoultion():
    print(sum([1 for x in apple if (x + a) >= s and (x + a) <= t]))
    print(sum([1 for x in orange if (x + b) >= s and (x + b) <= t]))

countFruits(apple,a,s,t)
countFruits(orange,b,s,t)

