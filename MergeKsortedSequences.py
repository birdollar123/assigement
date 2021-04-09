#!/bin/python3
#測資
# 3
# 3
# 3 2 1
# 6 5 4
# 9 8 7
# -> 9 8 7 6 5 4 3 2 1
import math
import os
import random
import re
import sys
import heapq
#
# Complete the 'MergeKSortedSequences' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts 2D_LONG_INTEGER_ARRAY sequences as parameter.
#

def MergeKSortedSequences(sequences):
    heap = []
    sequences_split = []
    start = 0
    for j in range(len(sequences)):
        sequences_split = sequences[start] #先取[[3, 2, 1], [6, 5, 4], [9, 8, 7]] 的 [3, 2, 1]
        #先乘-1排序
        for i in map(lambda x:x*-1, sequences_split):
            heapq.heappush(heap, i)
        start += 1
        
    print(heap)
    #[-9, -8, -6, -7, -3, -1, -4, -2, -5]

    #decreasing的sequence
    output = [] 
    for k in range(len(heap)):
        number = heapq.heappop(heap)
        output.append(-1*number) #把-1*heap 再*-1一次

    return output

##Main
k = int(input().strip())
n = int(input().strip())
sequences = []

for _ in range(k):
    sequences.append(list(map(int, input().rstrip().split())))
print(sequences)
# [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
merged_sequences = MergeKSortedSequences(sequences)
merged_sequences
