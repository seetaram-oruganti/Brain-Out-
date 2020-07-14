"""
Finding the Floor

    Problem
    Submissions
    Leaderboard
    Discussions

Given an array, you have to find the floor of a number x. The floor of a number x is nothing but the largest number in the array less than or equal to x.

Input Format

First line of input contains N - size of the array. The next line contains N integers, the elements of the array. The next line contains Q - number of queries. Each of the next Q lines contains a single integer X, for which you have to find the floor of X in the given array.

Constraints

30 points
1 <= N <= 105
1 <= Q <= 102
-108 <= ar[i] <= 108

70 points
1 <= N <= 105
1 <= Q <= 105
-108 <= ar[i] <= 108

Output Format

For each query, print the floor of X, separated by newline. If floor not found, print the value of "INT_MIN"

Sample Input 0

6
-6 10 -1 20 15 5 
5
-1
10
8
-10
-4

Sample Output 0

-1
10
5
-2147483648
-6



"""


def findfloor(ar, l, h, c,ans):
    m = (l+h)//2
    while(l<=h):
        if(ar[m]==c):
            ans = ar[m]
            return ans 
        if(ar[m]>c):
            return findfloor(ar, l, m-1, c, ans )
        if(ar[m]<c):
            ans = ar[m]
            return findfloor(ar, m+1, h, c, ans )
        return ans 
    return ans    
    
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
        if(ar[p1]>ar[p2]):
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


n = int(input())
ar = list(map(int, input().split()))
merges(ar, 0, n-1)
quer = int(input())
ans = -2147483648
for q in range(quer):
    c = int(input())
    val = findfloor(ar, 0, n-1, c,ans)
    print(val)
