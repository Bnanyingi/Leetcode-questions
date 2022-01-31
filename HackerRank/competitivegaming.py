#Trial 1
def numPlayers(k, scores):
    # Write your code here
    
    count = 0
    n = 0
    
    for i in scores:
        if n > k:
           n = i

           
        if count % 2 == 0:
            return scores




#trial 2

import math
import os
import random
import re
import sys







def numPlayers(k, scores):
        # Write your code here
    
  maxval = 0
  maxarr = {}
  newarr = {}
  
  for index,value in enumerate(scores):
    maxval = max(value,maxval)
    maxarr[index] = maxval
    newarr[value] = index
    
    xwin = False
    
    while index>= 0:
        maxval = maxarr[index]
        index = newarr[maxval]-1
        xwin = not xwin
        
        return scores
    
    for i in range(int(input())):
        k = int(input())
        scores = list(map(int,input().split()))
        print(numPlayers(k, scores))
        
    
    
  
  
    
        

            