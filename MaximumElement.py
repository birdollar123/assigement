#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    step_by_step = [] #用來判斷指令1, 2, 3
    number_stack = [] #main stack
    index = 0
    maximum = 0
    max_stack = [] #找最大值的stack
    getmax = []
    for op in operations:
        step_by_step = list(map(int, op.split()))
        if step_by_step[0] == 1:
            number_stack.append(step_by_step[1]) # 當operation是1時，stack往上長

            #第一次遇到operation 1，所以此時的最大值 = step_by_step[1]
            if index == 0: 
                max_stack.append(step_by_step[1]) 
                index += 1
            #遇到比現在max中還要大的數
            elif step_by_step[1] > max_stack[index-1]:
                max_stack.append(step_by_step[1]) 
                index += 1            
            else:
                max_stack.append(max_stack[index-1])
                index += 1

        elif step_by_step[0] == 2:
            number_stack.pop() #刪除number_stack最後一個stack的value #如果是pop(0)則是刪除第一個stack，後面的會自動往前補
            max_stack.pop() #同時刪除max_stack最後一個數值
            index -= 1

        elif step_by_step[0] == 3:
            getmax.append(max_stack[index-1])

    return getmax

##Main
n = int(input().strip())
ops = []
for _ in range(n):
    ops_item = input()
    ops.append(ops_item) #operations = ['1 97', '2', '1 20', ....]
res = getMax(ops)
res