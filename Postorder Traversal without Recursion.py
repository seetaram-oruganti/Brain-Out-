"""


Postorder Traversal

    Asked in:  
    Amazon
    Microsoft

Given a binary tree, return the postorder traversal of its nodes’ values.

Example :

Given binary tree

   1
    \
     2
    /
   3

return [3,2,1].

""""
# Using recursion is not allowed.

   """" NOTE: You only need to implement the given function.
    Do not read input, instead use the arguments to the function.
    Do not print the output, instead return values as specified.
    Still have a doubt? Checkout Sample Codes for more details. 
"""



# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, A):
        stack = [A]
        visited = []
        while stack:
            node = stack.pop()
            visited.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return list(reversed(visited))
