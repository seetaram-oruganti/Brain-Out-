"""
Largest Concatenated Number
Problem
Submissions
Leaderboard
Discussions
Given an array of integers, find the largest number that can be constructed by concatenating all the elements of the given array.

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines. First line of each test case contains N - size of the array and the second line contains N integers - elements of the array.

Constraints

1 <= T <= 1000
1 <= N <= 1000
0 <= ar[i] <= 1000

Output Format

For each test case, print the largest number that can be constructed by concatenating all the elements of the given array, separated by newline.

Sample Input 0

3
8
49 73 58 30 72 44 78 23 
4
69 9 57 60 
2
40 4 
Sample Output 0

7873725849443023
9696057
440



"""


def merges(ar,l,h):
    if(l==h):
        return
    mid=(l+h)//2
    merges(ar,l,mid)
    merges(ar,mid+1,h)
    merge(ar,l,mid,h)
    
def merge(ar,l,mid,h):
    p1 = l
    p2 = mid+1
    k = 0
    size = h-l+1
    temp = [0]*size
    while((p1<=mid) and (p2<=h)):
        s1 = str(ar[p1])+str(ar[p2])
        s2 = str(ar[p2])+str(ar[p1])
        if(int(s2)>int(s1)):
            temp[k] = ar[p2]
            k = k+1
            p2 = p2+1
        else:
            temp[k] = ar[p1]
            k = k+1
            p1 = p1+1
            
    while(p1<=mid):
        temp[k] = ar[p1]
        k = k+1
        p1 = p1+1
        
    while(p2<=h):
        temp[k] = ar[p2]
        k = k+1
        p2 = p2+1
    for i in range(l,h+1):
        ar[i] = temp[i-l]
for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    merges(A, 0 ,n-1)
    s = ''
    for i in A:
        s += str(i)
    if(int(s)==0):
        print(0)
    else:
        print(str(s))
