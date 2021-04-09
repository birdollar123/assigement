#!/bin/python3

import os
import sys
import heapq

def cookies(k, A):
    #先將A list以Min Heap的方式排列()
    heap = []
    for i in A:
        heapq.heappush(heap, i)

    iterations = 0
    while True:
        try:
            least_sweetness = heapq.heappop(heap)

            #如果還有小於threshold value的餅乾
            if least_sweetness < k:
                #secondleast寫在判斷式內，因為有可能new_sweerness是剩下的最後一個餅乾，但是它 < k的值 所以跳到except return -1
                #heap[0] = new_sweetness
                secondleast_sweetness = heapq.heappop(heap)
                new_sweetness = (1*least_sweetness + 2*secondleast_sweetness)
                heapq.heappush(heap, new_sweetness) #放回heap中排序
                iterations += 1
            
            #沒有餅乾小於threshold
            elif least_sweetness >= k:
                return iterations

        except:
            return -1
        
        print(heap)
        
##Main
nk = input().split()
#n is size of A[], k is the threshold value
n = int(nk[0])
k = int(nk[1])
A = list(map(int, input().rstrip().split()))
print(A) #[1, 2, 3, 9, 10, 12]

result = cookies(k, A)
result
