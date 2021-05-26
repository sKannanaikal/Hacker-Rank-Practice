#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum():
    # Write your code here
    arr = [
        [-9, -9, -9, 1, 1, 1],
        [0, -9, 0, 4, 3, 2],
        [-9, -9, -9, 1, 2, 3],
        [0, 0, 8, 6, 6, 0],
        [0, 0, 0, -2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ]
    startIndex = 0
    rowIndex = 0
    hourglassSumLargest = -sys.maxsize - 1 

    while (rowIndex <= len(arr) - 3):
        
        while(startIndex <= len(arr[rowIndex]) - 3):
            firstRow = arr[rowIndex][startIndex:startIndex+3]
            secondRow = arr[rowIndex + 1][startIndex+1]
            thirdRow = arr[rowIndex + 2][startIndex:startIndex+3]

            hourglassSum = sum(firstRow) + secondRow + sum(thirdRow)

            if hourglassSum > hourglassSumLargest:
                hourglassSumLargest = hourglassSum

            startIndex += 1
        
        rowIndex += 1
        startIndex = 0
    
    return hourglassSumLargest

if __name__ == '__main__':
    hourglassSum()
