#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for i in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    def max(a,b):
        if a>b:
            return a
        else:
            return b
    sums = -63
    max = -63
    for i in range(4):
        for j in range(4):
            sums = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            if sums>max:
                max=sums
            sums = -63
        
    print(max)
