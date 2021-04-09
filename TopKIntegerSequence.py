#!/bin/python3
#測資
# 3
# 4
# 12 9 7 5
# 11 4 2 1
# 3 10 8 6

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'TopKIntegerSequence' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts 2D_LONG_INTEGER_ARRAY matrix as parameter.
#

def TopKIntegerSequence(matrix, n):
    top_k = []
    heap = []
    matrix_split = []
    start = 0
    print(len(matrix))
    for i in range(len(matrix)): #跑幾次迴圈 
        matrix_split = matrix[start] #先拆分
        for i in matrix_split:
            heapq.heappush(heap,i)
        top_k.append(heapq.heappop(heap)) #Extract-mean #記得用append
        start += 1
    return top_k



k = int(input().strip()) #rows
n = int(input().strip()) #columns
matrix = []

for _ in range(k):
    matrix.append(list(map(int, input().rstrip().split())))

print(matrix)
#[[12, 9, 7, 5], [11, 4, 2, 1], [3, 10, 8, 6]]
top_k_integer_sequence = TopKIntegerSequence(matrix, n)
top_k_integer_sequence
