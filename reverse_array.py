#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray(a):
    # Write your code here
    b = []
    
    count = len(a) - 1
    
    while count >= 0:
        b.append(a[count])
        count -= 1
    
    return b

def main():
    values = [1, 2, 3, 4]
    reversedValues = reverseArray(values)
    print(reversedValues)

if __name__ == '__main__':
    main()
