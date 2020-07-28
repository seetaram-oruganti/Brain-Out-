"""

Remove Nth Node from List End

    Asked in:  
    HCL
    Amazon

Given a linked list, remove the nth node from the end of list and return its head.

For example,
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

    Note:

        If n is greater than the size of the list, remove the first node of the list.

Try doing it using constant additional space.



"""



# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        x=A
        count=0
        while(x!=None):
            count+=1
            x=x.next
        if(count==1):
            x=None
            return x
        if(count<=B):
            A=A.next
            return A
        s=count-B+1
        x=A
        for i in range(0,s-2):
            x=x.next
        x.next=x.next.next
        return A
        

