"""Sums in a Triangle Problem Code: SUMTRIAN
Add problem to Todo list
Submit

 
Let's consider a triangle of numbers in which a number appears in the first line, two numbers appear in the second line, three in the third line, etc. Develop a program which will compute the largest of the sums of numbers that appear on the paths starting from the top towards the base, so that:

on each path the next number is located on the row below, more precisely either directly below or below and one place to the right;
the number of rows is strictly positive, but less than 100
all numbers are positive integers between 0 and 99.
Input
In the first line integer n - the number of test cases (equal to about 1000). Then n test cases follow. Each test case starts with the number of lines which is followed by their content.

Output
For each test case write the determined value in a separate line.

Example
Input:
2
3
1
2 1
1 2 3
4 
1 
1 2 
4 1 2
2 3 1 1 

Output:
5
9

Warning: large Input/Output data, be careful with certain languages
All submissions for this problem are available.
Author:	admin
Tags:	admin
Date Added:	1-12-2008
Time Limit:	3 secs
Source Limit:	5000 Bytes
"""

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    t = []      #triangle 
    for j in range(n):
        t.append(list(map(int, input().split())))
    for j in range(n-1, -1, -1):
        for k in range(0,j):
            t[j-1][k] = t[j-1][k] + max(t[j][k],t[j][k+1])
    print(t[0][0])
    
        
