from collections import deque
import sys
input=sys.stdin.readline
n,k=map(int,input().split())
dq=deque([x for x in range(1, n+1)])
while len(dq)>1:
    dq.rotate(-1)
    if len(dq)>k:
        for _ in range(k-1):
            dq.popleft()
    else:
        for _ in range(len(dq)-1):
            dq.popleft()
    dq.rotate(1)
    if len(dq)>=2:
        dq.rotate(-1)
print(dq[0])