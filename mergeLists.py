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

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def printLinkedList(head):
    nextValue = head
    while nextValue is not None:
        print(nextValue.data)
        nextValue = nextValue.next

def mergeLists(head1, head2):
    node1 = head1
    node2 = head2

    merged = SinglyLinkedList()

    while node1 is not None or node2 is not None:
        if node1 is None:
            merged.insert_node(node2.data)
            node2 = node2.next
        elif node2 is None:
            merged.insert_node(node1.data)
            node1 = node1.next
        elif node1.data <= node2.data:
            merged.insert_node(node1.data)
            node1 = node1.next
        elif node2.data < node1.data:
            merged.insert_node(node2.data)
            node2 = node2.next
    
    return merged.head

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input('how many tests: '))

    for tests_itr in range(tests):
        llist1_count = int(input('list1 size: '))

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input('list 1 element: '))
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input('list 2 size: '))

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input('list 2 element: '))
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        printLinkedList(llist3)

        #print_singly_linked_list(llist3, ' ', fptr)
        #fptr.write('\n')

    #fptr.close()
