"""

Palindrome List

    Asked in:  
    Amazon
    Microsoft

Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.

Notes:

    Expected solution is linear in time and constant in space.

For example,

List 1-->2-->1 is a palindrome.
List 1-->2-->3 is not a palindrome.

    NOTE: You only need to implement the given function. Do not read input, instead use the arguments to the function. Do not print the output, instead return values as specified.
    Still have a doubt? Checkout Sample Codes for more details. 

"""



# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        st = []
        temp = A
        while(A != None):
            st.append(A.val)
            A = A.next
        A = temp
        while(A != None):
            if(st.pop() != A.val):
                return 0
            A = A.next
        return 1
                
            
