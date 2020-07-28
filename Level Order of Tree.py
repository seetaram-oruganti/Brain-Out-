"""

Level Order of Tree

    Problem
    Submissions
    Leaderboard
    Discussions

Given an array of unique elements, construct a
Binary Search Tree and print the Level Order of the tree.

Input Format

First line of input contains T - number of test cases.
Its followed by 2T lines. First line of each test case contains
N - number of nodes in the BST. The next line contains N unique
integers - value of the nodes.

Constraints

For each test case, print the Level Order of the Binary Search Tree,
separate each level by newline. Separate the output of different test
cases with an extra newline.

Output Format

1 <= T <= 1000
1 <= N <= 1000
0 <= ar[i] <= 10000

Sample Input 0

3
5
1 2 3 4 5 
5
3 2 4 1 5 
7
4 5 15 0 1 7 17 

Sample Output 0

1 
2 
3 
4 
5 

3 
2 4 
1 5 

4 
0 5 
1 15 
7 17 




"""

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def _str_(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
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
          
    while q: 
        count = len(q) 
        while count > 0: 
            temp = q.pop(0) 
            print(temp.info, end = ' ') 
            if temp.left: 
                q.append(temp.left) 
            if temp.right: 
                q.append(temp.right) 
  
            count -= 1
        print(' ') 

for _ in range(int(input())):
    n = int(input())
    tree = BinarySearchTree()
    ar = list(map(int, input().split()))
    for i in ar:
        tree.create(i)
    levelor(tree.root)
    print()
