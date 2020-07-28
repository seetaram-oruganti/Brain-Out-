"""

Left View of Tree

    Problem
    Submissions
    Leaderboard
    Discussions

Given an array of unique elements, construct a Binary Search Tree and print the left-view of the tree. Left view of a Tree is the set of nodes visible when tree is viewed from left side.

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines. First line of each test case contains N - number of nodes in the BST. The next line contains N unique integers - value of the nodes.

Constraints

1 <= T <= 1000
1 <= N <= 1000
0 <= ar[i] <= 10000

Output Format

For each test case, print the left-view of the Binary Search Tree, separated by newline.

Sample Input 0

3
5
1 2 3 4 5
5
3 2 4 1 5
7
4 5 15 0 1 7 17

Sample Output 0

1 2 3 4 5 
3 2 1 
4 0 1 7 




"""

class Node:
    def _init_(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def _str_(self):
        return str(self.info) 

class BinarySearchTree:
    def _init_(self): 
        self.root = None

    def create(self, val):  
        if (self.root == None):
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
def levelor(root):
    if root is None: 
        return
    q = [] 
    q.append(root)
    
    while(len(q)>0):
        k=len(q)
        temp=[]
        for i in range(0,k):
            x = q.pop(0)
            temp.append(x)
            if(x.left != None):
                q.append(x.left)
            if(x.right != None):
                q.append(x.right)
        print(temp[0].info,end=" ")
    # print()

for _ in range(int(input())):
    n = int(input())
    tree = BinarySearchTree()
    ar = list(map(int, input().split()))
    for i in ar:
        tree.create(i)
    levelor(tree.root)
    print()
