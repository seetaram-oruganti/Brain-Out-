"""
Print pyramid pattern
Problem
Submissions
Leaderboard
Discussions
Print pyramid pattern. See example for more details.

Input Format

First line of input contains a single integer N - the size of the pyramid.

Constraints

1 <= N <= 50

Output Format

For the given integer, print pyramid pattern.

Sample Input 0

5
Sample Output 0

    *
   ***
  *****
 *******
*********

"""


n = int(input())
l = n-1
i = 1
for j in range(n):
    print(" "*l,"*"*i," "*l,sep="")
    l=l-1
    i=i+2
