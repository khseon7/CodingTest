import sys
input=sys.stdin.readline
class Node:
    def __init__(self,key=None):
        self.key=key
        self.left=None
        self.right=None

class Tree(Node):
    def __init__(self):
        self.root=None
    def search(self,start_node=None,target_val=None):
        if(start_node is None):
            return None
        if(start_node.key==target_val):
            return start_node
        left_result = self.search(start_node.left, target_val)
        if left_result is not None:
            return left_result
        return self.search(start_node.right, target_val)
    
    def insert(self):
        a,b,c=input().strip().split()
        if(self.root==None):
            self.root=Node(a)
            node=self.root
        else:
            node=self.search(self.root,a)
        if(b!='.'):
            node.left=Node(b)
        if(c!='.'):
            node.right=Node(c)

def preorder_find(t):
    if t is None:
        return
    print(t.key, end="")
    preorder_find(t.left)
    preorder_find(t.right)

def inorder_find(t):
    if t is None:
        return
    inorder_find(t.left)
    print(t.key, end="")
    inorder_find(t.right)

def postorder_find(t):
    if t is None:
        return
    postorder_find(t.left)
    postorder_find(t.right)
    print(t.key, end="")

n=int(input())
T=Tree()
for _ in range(n):
    T.insert()
preorder_find(T.root)
print()
inorder_find(T.root)
print()
postorder_find(T.root)