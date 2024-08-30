from collections import deque
import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    res=deque()
    arr=map(str,input().split())
    for i in arr:
        res.append(i) if not res else res.appendleft(i) if i<=res[0] else res.append(i)
    print("".join(res))