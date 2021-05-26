#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def printLinkedList(head):
    nextValue = head
    while nextValue is not None:
        print(nextValue.data)
        nextValue = nextValue.next

# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtHead(llist, data):
    # Write your code here
    newHead = SinglyLinkedListNode(data)
    newHead.next = llist
    return newHead

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input("Enter Count: "))

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input("Enter Value: "))
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head

    printLinkedList(llist_head)
    #fptr.write('\n')

    #fptr.close()