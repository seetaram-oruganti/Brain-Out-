"""

Depth of Tree Nodes

    Problem
    Submissions
    Leaderboard
    Discussions

Given an array of unique elements, construct a Binary Search Tree and for every node, print the depth of that node.

Input Format

First line of input contains T - number of test cases. Its followed by 2T lines. First line of each test case contains N - number of nodes in the BST. The next line contains N unique integers - value of the nodes.

Constraints

For each test case, print the depth of every node of the Binary Search Tree, separated by newline.

1 <= T <= 1000
1 <= N <= 1000
0 <= ar[i] <= 10000

Output Format

For each test case, print N integers, where the ith integer denotes the depth of A[i] in the Binary Search Tree, separated by newline.

Sample Input 0

3
5
1 2 3 4 5 
5
3 2 4 1 5 
7
4 5 15 0 1 7 17 

Sample Output 0

0 1 2 3 4 
0 1 1 2 2 
0 1 2 1 2 3 3 


"""

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
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

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
       
'''
def search(r, key, v):
    t = r 
    if(t == None):
        return v
    if(t.info == key):
        return v
    if(t.info > key):
        v = v + 1
        return search(t.left, key, v)
    else:
        v = v + 1
        return search(t.right, key, v)
    

    
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    tree = BinarySearchTree()
    for i in l:
        tree.create(i)
    for i in range(n):
        d = search(tree.root, l[i], 0)
        print(d, end = " ")
    print()
        
        
