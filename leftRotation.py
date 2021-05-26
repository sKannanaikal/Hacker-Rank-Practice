#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotateLeft(d, arr):
    # Write your code here
    copyOfArray = arr.copy()
    solution = []
    for i in range(len(arr)):
        newIndex = ((i % len(arr)) - d) % len(arr)
        solution.insert(newIndex, arr[i])
    
    return solution

def main():
    arr = [1,2,3,4,5]
    d = input("How much rotation: ")
    modifiedList = rotateLeft(int(d), arr)

    print(modifiedList)

if __name__ == '__main__':
   main()
