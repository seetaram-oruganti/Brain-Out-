"""
Find Duplicate in Array
Asked in:  
Amazon
VMWare
Riverbed
Given a read only array of n + 1 integers between 1 and n, find one number that repeats in linear time using less than O(n) space and traversing the stream sequentially O(1) times.

Sample Input:

[3 4 1 4 1]
Sample Output:

1
If there are multiple possible answers ( like in the sample case above ), output any one.

If there is no duplicate, output -1


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        A = list(A)
        n = len(A)
        for i in range(n):
            index = A[i]%n
            A[index] = A[index] + n
            
        for j in range(n):
            if A[j]//n > 1:
                return j
        
        return -1
    
"""
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        lenA = len(A)
        temp = [0]*lenA
        for i in A:
            if temp[i - 1]:
                return i
            else:
                temp[i - 1] = 1
        return -1
            

