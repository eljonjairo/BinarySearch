
#!/usr/bin/env python3

# Binary search
# 
# John Diaz january 2023 Base on 12 beginner Python projects - Coding Course FreeCodeCamp.org
#TO DO List:
#  
#

import random
import numpy as np


def BinarySearch(l,target, low=None, high=None):
    if low == None:
        low = 0
    if high == None:
        high = len(l) - 1
        
    # if high < low target is not in l    
    if high < low:
        return -1
        
    midpoint = (low+high) // 2      # Calculate the midpoint
    
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return BinarySearch(l, target, low, midpoint-1)
    else:
        return BinarySearch(l, target, midpoint+1, midpoint-1)
        
    
if __name__ == '__main__' :
    len_ = 50
    # Generate a numpy array with zeros
    list_ = np.zeros(len_,)
    # Full fill the array
    for il in range(len_) :
        list_[il] = random.randint(-3*len_,3*len_)
    # Sorted and eliminate repeated elements
    list_ = np.unique(list_)
    # Generate the target number
    target = random.randint(-3*len_,3*len_)
    index = BinarySearch(list_,target)
    if index == -1:
        print(f" the number {target} is not in the list")
    else:    
        print(f" the number {target} is  in position {index}")
