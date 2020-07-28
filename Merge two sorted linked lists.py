"""

Merge two sorted linked lists
1272.43 more points to get your next star!
Rank: 111904|Points: 927.57/2200
Problem Solving

    Problem
    Submissions
    Leaderboard
    Discussions
    Editorial

This challenge is part of a tutorial track by MyCodeSchool

You’re given the pointer to the head nodes of two sorted linked lists. The data in both lists will be sorted in ascending order. Change the next pointers to obtain a single, merged linked list which also has data in ascending order. Either head pointer given may be null meaning that the corresponding list is empty.

Input Format

You have to complete the SinglyLinkedListNode MergeLists(SinglyLinkedListNode headA, SinglyLinkedListNode headB) method which takes two arguments - the heads of the two sorted linked lists to merge. You should NOT read any input from stdin/console.

The input is handled by the code in the editor and the format is as follows:

The first line contains an integer

, denoting the number of test cases.
The format for each test case is as follows:

The first line contains an integer
, denoting the length of the first linked list.
The next lines contain an integer each, denoting the elements of the linked list.
The next line contains an integer , denoting the length of the second linked list.
The next

lines contain an integer each, denoting the elements of the second linked list.

Constraints

, where is the

    element of the list.

Output Format

Change the next pointer of individual nodes so that nodes from both lists are merged into a single list. Then return the head of this merged list. Do NOT print anything to stdout/console.

The output is handled by the editor and the format is as follows:

For each test case, print in a new line, the linked list after merging them separated by spaces.

Sample Input

1
3
1
2
3
2
3
4

Sample Output

1 2 3 3 4 

Explanation

The first linked list is: 1 -> 2 -> 3 -> NULL

The second linked list is: 3 -> 4 -> NULL

Hence, the merged linked list is: 1 -> 2 -> 3 -> 3 -> 4 -> NULL



"""

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
def mergeLists(h1, h2):
    h3 = SinglyLinkedListNode(-1)
    t = h3
    while(h1 != None and h2 != None):
        if(h1.data <  h2.data):
            x = SinglyLinkedListNode(h1.data)
            x = h1
            h1= h1.next
            x.next = None
            h3.next = x
            h3 = x
        else:
            x = SinglyLinkedListNode(h2.data)
            x = h2
            h2= h2.next
            x.next = None
            h3.next = x
            h3 = x
    if(h1 != None):
        h3.next = h1
    else:
        h3.next = h2
    return t.next




if __name__ == '__main__':
