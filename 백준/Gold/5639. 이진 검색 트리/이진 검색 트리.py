import sys
input=sys.stdin.readline

sys.setrecursionlimit(20000)

class Node:
    def __init__(self,key=None):
        self.key=key
        self.left=None
        self.right=None

class Tree(Node):
    def __init__(self):
        self.root=None
    def insert(self,arr):
        for idx,key in enumerate(arr):
            if idx==0:
                self.root=Node(key)
            else:
                node=self.root
                while node:
                    if key<node.key:
                        if node.left is None:
                            node.left=Node(key)
                            break
                        node=node.left
                    else:
                        if node.right is None:
                            node.right=Node(key)
                            break
                        node=node.right

def postorder_find(t):
    if t is None:
        return
    postorder_find(t.left)
    postorder_find(t.right)
    print(t.key)

T=Tree()
arr=[]
while 1:
    try:
        arr.append(int(input().strip()))
    except:
        break
T.insert(arr)
postorder_find(T.root)