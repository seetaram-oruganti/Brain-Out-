"""
Implement pow(x, n) % d.

In other words, given x, n and d,

find (xn % d)

Note that remainders on division cannot be negative.
In other words, make sure the answer you return is non negative.

Input : x = 2, n = 3, d = 3
Output : 2

2^3 % 3 = 8 % 3 = 2.


"""

class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
        
    def pow(self, x, n, d):
        if(x==0):
            return 0
        if(n==0):
            return 1
        ans = pow(x, n//2, d)
        if(n&1==0):
            return (ans * ans)%d
        else:
            return (ans * ans * x)%d
            
        
