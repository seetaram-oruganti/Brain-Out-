"""

Excel Column Number
Asked in:  
Amazon
Problem Description

Given a column title A as appears in an Excel sheet, return its corresponding column number.



Problem Constraints
1 <= |A| <= 100



Input Format
First and only argument is string A.



Output Format
Return an integer



Example Input
Input 1:

 1
Input 2:

 28


Example Output
Output 1:

 "A"
Output 2:

 "AB"


Example Explanation
Explanation 1:

 1 -> "A"
Explanation 2:

A  -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 


"""



class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        
        B = A[::-1]
        total = 0
        for i in range( 0, len( B ) ):
            total += ( ord( B[i] ) - 64 ) * pow( 26, i ) 
        return total
