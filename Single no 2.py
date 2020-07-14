"""
Single Number II
Asked in:  
Google
Amazon
Given an array of integers, every element appears thrice except for one which occurs once.

Find that element which does not appear thrice.

Note: Your algorithm should have a linear runtime complexity.

Could you implement it without using extra memory?

Input Format:

    First and only argument of input contains an integer array A
Output Format:

    return a single integer.
Constraints:

2 <= N <= 5 000 000  
0 <= A[i] <= INT_MAX
For Examples :

Example Input 1:
    A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
Example Output 1:
    4
Explanation:
    4 occur exactly once
Example Input 2:
    A = [0, 0, 0, 1]
Example Output 2:
    1

"""




class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        k = 31
        c1 = 0
        c0 = 0
        s = ""
        while(k>-1):
            c1 = 0
            c0 = 0
            for i in A:
                if(i&(1<<k)):
                    c1 += 1
                else:
                    c0 += 1
            if(c1%3):
                s = s + "1"
            else:
                s = s + "0"
            k -= 1
            
        return (int(s,2))    
                
