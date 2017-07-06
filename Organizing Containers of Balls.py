#!/bin/python3
#HackerRankTeam - Organizing Containers of Balls
#7-6-2017 @Author - Jonathan Thornton

import sys


q = int(input().strip())
for a0 in range(q):
    n = int(input().strip())
    M = []
    for M_i in range(n):
       M_t = [int(M_temp) for M_temp in input().strip().split(' ')]
       M.append(M_t)
    
    #q represents number of queries
    #n -> number of containers 
    #M[0] represents the slots which are empty
    #M[1] represents the slots which are full
