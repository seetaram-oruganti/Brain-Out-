"""


Insertion Sort List

    Asked in:  
    Microsoft
    Google

Sort a linked list using insertion sort.

We have explained Insertion Sort at Slide 7 of Arrays

Insertion Sort Wiki has some details on Insertion Sort as well.

Example :

Input : 1 -> 3 -> 2

Return 1 -> 2 -> 3



"""



# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    
    def insertionSortList(self, head_ref): 
  
    # Initialize sorted linked list 
        sorted = None
  
    # Traverse the given linked list and insert every 
    # node to sorted 
        current = head_ref 
        while (current != None): 
      
        # Store next for next iteration 
            next = current.next
  
        # insert current in sorted linked list 
            sorted = self.sortedInsert( sorted, current) 
  
        # Update current 
            current = next
      
    # Update head_ref to point to sorted linked list 
        head_ref = sorted
        return head_ref 
  
# function to insert a new_node in a list. Note that this 
# function expects a pointer to head_ref as this can modify the 
# head of the input linked list (similar to push()) 
    def sortedInsert(self, head_ref, new_node): 
  
        current = None
          
        # Special case for the head end */ 
        if (head_ref == None or (head_ref).val >= new_node.val): 
          
            new_node.next = head_ref 
            head_ref = new_node 
          
        else: 
          
            # Locate the node before the point of insertion  
            current = head_ref 
            while (current.next != None and
                current.next.val < new_node.val): 
              
                current = current.next
              
            new_node.next = current.next
            current.next = new_node 
              
        return head_ref 
