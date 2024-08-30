from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
res=deque([n])
for i in range(n-1,0,-1):
    res.appendleft(i)
    for _ in range(i):
        res.appendleft(res.pop())
print(" ".join(map(str,res)))