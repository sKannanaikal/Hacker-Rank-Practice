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

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

def printLinkedList(head):
    nextValue = head
    while nextValue is not None:
        print(nextValue.data)
        nextValue = nextValue.next

#
# Complete the 'removeDuplicates' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def removeDuplicates(llist):
    # Write your code here
    currentNode = llist
    nextNode = currentNode.next

    while nextNode is not None:
        if currentNode.data == nextNode.data:
            currentNode.next = nextNode.next
            nextNode = currentNode.next

        elif currentNode.data != nextNode.data:
            currentNode = currentNode.next
            nextNode = currentNode.next

    return llist

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input('Enter num of tests: '))

    for t_itr in range(t):
        llist_count = int(input('Enter list size: '))

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input('Enter list item: '))
            llist.insert_node(llist_item)

        llist1 = removeDuplicates(llist.head)

        printLinkedList(llist1)

        #print_singly_linked_list(llist1, ' ', fptr)
        #fptr.write('\n')

    #fptr.close()
