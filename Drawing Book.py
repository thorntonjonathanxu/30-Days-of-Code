#!/bin/python3
#HackerRankTeam - Drawing Book
#7-8-2017 @Author - Jonathan Thornton
#https://www.hackerrank.com/challenges/drawing-book

import sys
import math

def solve(booksize, request_page):
    # Complete this function
    if(request_page/booksize <= .5):     #search from the front to back
        flips = math.floor(request_page / 2)
    else:                                #search from back to front
        flips = math.floor(booksize/2)-math.floor(request_page/2)
    return flips

    #Minimalist solution 
    #return min(request_page//2, booksize//2 - request_page//2)



#Test Case 1 
# booksize = 6
# request_page = 6


#Custom Input
booksize = int(input().strip())
request_page = int(input().strip())
result = solve(booksize, request_page)
print(result)