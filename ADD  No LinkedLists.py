"""




"""

""" EDitorial fastest """"
 Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        # corner cases
        if A == None and B == None:
            return None
        
        p1, p2 = A, B
        
        # add B to A
        carry = 0
        while p1.next != None and p2.next != None:
            added_num = p1.val + p2.val + carry
            p1.val = added_num%10
            carry = added_num//10
            p1 = p1.next
            p2 = p2.next

        added_num = p1.val + p2.val + carry
        p1.val = added_num%10
        carry = added_num//10

        if p1.next == None and p2.next == None:
            if carry == 1:
                p1.next = ListNode(1)
        else:
            if p1.next == None:
                p1.next = p2.next
            p1 = p1.next
            while carry and p1.next != None:
                added_num = p1.val + carry
                p1.val = added_num%10
                carry = added_num//10
                p1 = p1.next
            if carry == 1:
                added_num = p1.val + carry
                p1.val = added_num%10
                carry = added_num//10
                if carry == 1:
                    p1.next = ListNode(1)
        return A




    """ SELF HACKER RANK SMART INTERVIEWS """








    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def Rev(self, head):
        h2 = None
        while(head != None):
            x = ListNode(head.val)
            x = head
            head = head.next
            x.next = h2
            h2 = x
        return h2
        
    
    def addTwoNumbers(self, h1, h2):
        h3 = None
        h1 = self.Rev(h1)
        h2 = self.Rev(h2)
        c = 0
        while(h1 != None or h2 != None or c!=0):
            su = c
            if(h1 != None):
                su += h1.val
                h1 = h1.next
            if(h2 != None):
                su += h2.val
                h2 = h2.next
            x = ListNode(su%10)
            x.next = h3
            h3 = x
            c = su//10
            h3 = self.Rev(h3)
                
        return h3
