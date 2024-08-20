from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
dq=deque([x for x in range(1,n+1)])
arr=list(map(int,input().split()))
first=0
cnt=0
for i in arr:
    index=dq.index(i)
    if index>=len(dq)/2:
        index=len(dq)-index
        cnt+=index
    else:
        cnt+=index
        index*=-1
    dq.rotate(index)
    dq.popleft()
print(cnt)