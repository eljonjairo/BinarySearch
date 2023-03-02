
#!/usr/bin/env python3

# Binary search
# Generate a sorted list of numbers, then find a target in the list
# John Diaz january 2023 Base on 12 beginner Python projects - Coding Course FreeCodeCamp.org
# TO DO List:
#
#

import random
import numpy as np


def insert_target(list_, target):
    # Insert the target number in a random position of the list
    len_ = len(list_) - 1
    index = random.randint(0, len_)
    list_[index] = target

    return list_


def binary_search(list_, target, low=None, high=None):
    # Search the target number into the list
    if low == None:
        low = 0
    if high == None:
        high = len(list_) - 1

    # if high < low target is not in the list
    if high < low:
        return -1

    midpoint = (low+high) // 2      # Calculate the midpoint
    if list_[midpoint] == target:
        return midpoint
    elif target < list_[midpoint]:
        return binary_search(list_, target, low, midpoint-1)
    else:
        return binary_search(list_, target, midpoint+1, high)


def print_(list_):
    len_ = len(list_)
    nrows = len_ // 10
    ici = 0
    icf = 10
    for irow in range(nrows):
        print(f" Lista del {ici+1} al {icf}:  " + str(list_[ici:icf]))
        ici += 10
        icf += 10

    if len_ % 10 != 0:
        print(f" Lista del {ici+1} al {len_}:  " + str(list_[ici:icf]))

    print()


if __name__ == '__main__':
    len_ = 58

    # Generate a numpy array with zeros
    list_ = np.zeros(len_,)
    for il in range(len_):
        list_[il] = random.randint(-3*len_, 3*len_)

    # Generate the target number
    target = random.randint(-3*len_, 3*len_)
    print()
    print(f" the target number is {target} \n ")

    list_ = insert_target(list_, target)

    # Sort the array and eliminate repeated elements
    list_ = np.unique(list_)
    # The length of the sorted list could be less than len_, because of the
    # elimination of repeated numbers.
    print_(list_)

    # Find the target number
    index = binary_search(list_, target)

    if index == -1:
        print(f" the number {target} is not in the list \n")
    else:
        print(f" the number {target} is  in position {index} \n")
