"""
Xor-sequence

1337.43 more points to get your next star!
Rank: 126652|Points: 862.57/2200
Problem Solving
Your Xor-sequence submission got 40.00 points.  
You are now 1337.43 points away from the 6th star for your problem solving badge.
Try the next challenge | Try a Random Challenge
Problem
Submissions
Leaderboard
Discussions
Editorial
An array, , is defined as follows:

 for , where  is the symbol for XOR
You will be given a left and right index . You must determine the XOR sum of the segment of  as .

For example, . The segment from  to  sums to .

Print the answer to each question.

Function Description

Complete the xorSequence function in the editor below. It should return the integer value calculated.

xorSequence has the following parameter(s):

l: the lower index of the range to sum
r: the higher index of the range to sum
Input Format

The first line contains an integer , the number of questions.
Each of the next  lines contains two space-separated integers,  and , the inclusive left and right indexes of the segment to query.

Constraints



Output Format

On a new line for each test case, print the XOR-Sum of 's elements in the inclusive range between indices  and .

Sample Input 0

3
2 4
2 8
5 9
Sample Output 0

7
9
15
Explanation 0

The beginning of our array looks like this: 

Test Case 0:



Test Case 1:



Test Case 2:



Sample Input 1

3
3 5
4 6
15 20
Sample Output 1

5
2
22

"""


def f(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    n -= 2
    if n % 8 == 0 or n % 8 == 1:
        return 2
    if n % 8 == 4 or n % 8 == 5:
        return 0
    if n % 8 == 2 or n % 8 == 3:
        return n + 4
    if n % 8 == 6 or n % 8 == 7:
        return n + 2
    assert False

q = int(input())
assert 1 <= q <= 10 ** 5
for i in range(q):
    l, r = map(int, input().split())
    assert 1 <= l <= r <= 10 ** 15
    print (f(r) ^ f(l - 1))
