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
# Complete the 'reverse' function below.
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

def recursiveReverse(llist):
    # Write your code here
    currentValue = llist
    nextValue = currentValue.next

    if nextValue is None or currentValue is None:
        return currentValue
    
    reversedList = recursiveReverse(nextValue)
    nextValue.next = currentValue
    currentValue.next = None

    return reversedList

def reverse(llist):
    if llist is None or llist.next is None:
        return llist
    
    reversed = reverse(llist.next)
    llist.next.next = llist
    llist.next = None

    return reversed



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input("Enter test count: "))

    for tests_itr in range(tests):
        llist_count = int(input("Enter size: "))

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input("Enter item: "))
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        printLinkedList(llist1)

        #print_singly_linked_list(llist1, ' ', fptr)
        #fptr.write('\n')

    #fptr.close()
