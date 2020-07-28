"""


Paint House!

    Asked in:  
    LinkedIn

Problem Description

There are a row of N houses, each house can be painted with one of the three
colors: red, blue or green.

The cost of painting each house with a certain color is different. You have
to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a N x 3
cost matrix A.

For example, A[0][0] is the cost of painting house 0 with color red; A[1][2]
is the cost of painting house 1 with color green, and so on.

Find the minimum total cost to paint all houses.


Problem Constraints

1 <= N <= 105

1 <= A[i][j] <= 103


Input Format

First and only argument is an 2D integer matrix A of size N x 3 denoting the
cost to paint the houses.


Output Format

Return an integer denoting the minimum total cost to paint all houses.


Example Input

Input 1:

 A = [  [1, 2, 3]
        [10, 11, 12]
     ]



Example Output

Output 1:

 12



Example Explanation

Explanation 1:

 Paint house 1 with red and house 2 with green i.e A[0][0] + A[1][1] = 1 + 11 = 12



    NOTE: You only need to implement the given function. Do not read input,
    instead use the arguments to the function. Do not print the output,
    instead return values as specified.
    Still have a doubt? Checkout Sample Codes for more details. 


"""


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        pr = 0
        pb = 0
        pg = 0
        n = len(A)
        for i in range(1, n+1):
            cr = A[i-1][0] + min(pb, pg)
            cb = A[i-1][1] + min(pr, pg)
            cg = A[i-1][2] + min(pb, pr)
            pr , pb , pg = cr, cb, cg
        return min(cr,cb,cg )
            
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        pr = 0
        pb = 0
        pg = 0
        n = len(A)
        for i in range(1, n+1):
            cr = A[i-1][0] + min(pb, pg)
            cb = A[i-1][1] + min(pr, pg)
            cg = A[i-1][2] + min(pb, pr)
            pr , pb , pg = cr, cb, cg
        return min(cr,cb,cg )
            
