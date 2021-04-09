#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

#計算stack的總共高度
def calculateheight(h):
    height = 0
    for i in h:
        height += i
    return height

def equalStacks(h1, h2, h3):
    height1 = calculateheight(h1)
    height2 = calculateheight(h2)
    height3 = calculateheight(h3)
    label1, label2, label3 = 0,0,0
    result = 0
    while True:
        if height1 == height2 and height2 == height3: #這個條件要先放前面
            result = height1
            break
        elif height1 >= height2 and height1 >= height3: #height1最高
            height1 -= h1[label1]
            label1 += 1
        elif height2 >= height1 and height2 >= height3: #height2最高
            height2 -= h2[label2]
            label2 += 1
        elif height3 >= height1 and height3 >= height2:
            height3 -= h3[label3]
            label3 += 1
    return result
    
##Main
first_multiple_input = input().rstrip().split() #the numbers of cylinders in stacks 1, 2, 3

n1 = int(first_multiple_input[0])
n2 = int(first_multiple_input[1])
n3 = int(first_multiple_input[2])

h1 = list(map(int, input().rstrip().split())) # h1 = [3, 2, 1, 1, 1]
h2 = list(map(int, input().rstrip().split())) # h2 = [4, 3, 2]
h3 = list(map(int, input().rstrip().split())) # h3 = [1, 1, 4, 1]

result = equalStacks(h1, h2, h3)
print(result)