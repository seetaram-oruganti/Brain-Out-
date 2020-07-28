"""

PreOrder InOrder to PostOrder

    Problem
    Submissions
    Leaderboard
    Discussions

Given the preorder and inorder traversals of a binary
tree with unique elements, print the PostOrder Traversals of the tree.

Input Format

First line of input contains T - number of test cases.
Its followed by 3T lines. First line of each test case contains N - number
of nodes in the BST. Second line contains N unique integers denoting
the preorder traversal of the tree. Third line contains N unique integers
denoting the inorder traversal of the tree.

Constraints

1 <= T <= 1000
1 <= N <= 1000
0 <= ar[i] <= 10000

Output Format

For each test case, print the PostOrder Traversal of the Binary Tree,
separated by newline.

Sample Input 0

3
7
1 2 4 5 3 6 7 
4 2 5 1 6 3 7 
10
8 5 9 7 1 12 2 4 11 3 
9 5 1 7 2 12 8 4 3 11 
9
2 7 3 6 8 11 5 9 4 
3 7 8 6 11 2 5 4 9 

Sample Output 0

4 5 2 6 7 3 1 
9 1 2 12 7 5 3 11 4 8 
3 8 11 6 7 4 9 5 2 


"""
def postorder(pre, ino):

    n = len(pre)
    if(n == 0):
        return 
    #print(*pre)
    #print(*ino)
    root = pre[0]
    #print(root)
    pos = ino.index(root)
    #print(pos)
    postorder(pre[1:pos+1], ino[:pos])
    postorder(pre[pos+1:], ino[pos+1:n])
    print(pre[0], end =" ")
    
    


for _ in range (int(input())):
    n = int(input())
    pre = list(map(int, input().split()))
    ino = list(map(int, input().split()))
    postorder(pre, ino)
    print()
    
