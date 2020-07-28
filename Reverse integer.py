"""
Reverse integer
Asked in:  
HCL
Bloomberg
Reverse digits of an integer.

Example1:

x = 123,

return 321
Example2:

x = -123,

return -321

Return 0 if the result overflows and does not fit in a 32 bit signed integer

"""


class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        sgn = -1 if A < 0 else 1
        A = abs(A)
        string = str(A)
        reverse = string[::-1]
        result = int(reverse)
        if result > 2**31 - 1:
            return 0
        return sgn * result
