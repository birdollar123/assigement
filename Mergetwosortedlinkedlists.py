#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data #.data存資料
        self.next = None #.next指向下一個node

#建立list的一開始，預設裡面是沒有節點的，所以初始head,tail為None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data): #node_data 是 llist1_item 的 int值
        node = SinglyLinkedListNode(node_data) #先開一個空的linked list
        if not self.head: #not None = True
            self.head = node #self.head == None,代表這個Linked list為空，因此head跟tail同時指向 new_node
        else:
            self.tail.next = node #self.head != None,代表這個Linked list沒有為空，所以將tail.next指向new_node

        self.tail = node #將現在的tail變成new_node

def print_singly_linked_list(node, sep):
    while node:
        #print(node.data)
        node = node.next
        print(node.data)

def h1gotonextnode(current):
    target = current.next
    return target
def h2gotonextnode(current):
    target = current.next
    return target

def mergeLists(head1, head2):
    llist3 = SinglyLinkedList() #開一個新的linked list
    while True:
        #condition 1(head1和head2都還沒到最後一個)
        if head1.next != None and head2.next != None: 
            if head1.data <= head2.data:
                llist3.insert_node(head1.data)
                head1 = h1gotonextnode(head1)
            else:
                llist3.insert_node(head2.data)
                head2 = h2gotonextnode(head2)
        #condition 2
        elif head1.next != None and head2.next == None: #到h2的最後一個了
            if head1.data <= head2.data:
                llist3.insert_node(head1.data)
                head1 = h1gotonextnode(head1)
            else:
                llist3.insert_node(head2.data) #h2結束
                while True:
                    llist3.insert_node(head1.data)
                    head1 = h1gotonextnode(head1)
                    if head1.next == None: #到h1的最後一個了
                        llist3.insert_node(head1.data) #h1結束
                        break
                break #要在這邊加break 不然會到下面的 head1.next == None and head2.next == None而再跑一次
        #condition 3
        elif head1.next == None and head2.next != None: #head1要結束了
            if head1.data >= head2.data:
                llist3.insert_node(head2.data)
                head2 = h2gotonextnode(head2)
            else:
                llist3.insert_node(head1.data) #h1結束
                while True:
                    llist3.insert_node(head2.data)
                    head2 = h2gotonextnode(head2)
                    if head2.next == None:
                        llist3.insert_node(head2.data) #h2結束
                        break
                break
        
        #condition 4
        elif head1.next == None and head2.next == None:
            if head1.data <= head2.data:
                llist3.insert_node(head1.data)
                llist3.insert_node(head2.data)
                break
            else:
                llist3.insert_node(head2.data)
                llist3.insert_node(head1.data)
                break
    return llist3.head

###Main
#ex: 3 所以要輸入3個數
llist1_count = int(input())
#.head(), .tail()
llist1 = SinglyLinkedList() 
for _ in range(llist1_count): 
    llist1_item = int(input()) #1 -> 2 -> 3
    llist1.insert_node(llist1_item) #insert node to llist1
    #print(dir(llist1.insert_node))

llist2_count = int(input())
llist2 = SinglyLinkedList()
for _ in range(llist2_count):
    llist2_item = int(input())
    llist2.insert_node(llist2_item)

dir(llist1.insert_node)
#print(llist1.head, llist2.head)
llist3 = mergeLists(llist1.head, llist2.head)  #merge List
llist3
print_singly_linked_list(llist3, ' ')

 