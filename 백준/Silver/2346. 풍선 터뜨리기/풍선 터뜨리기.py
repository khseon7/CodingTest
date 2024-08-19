from collections import deque
import sys

input=sys.stdin.readline

n=int(input())
left_deque=deque()
arr=list(map(int,input().split()))
dq=deque((arr[i],i+1)for i in range(n))
res=[]

while len(dq)!=1:
    index,posit=dq.popleft()
    res.append(posit)
    if index>0:
        dq.rotate(-index+1)
    else:
        dq.rotate(-index)
res.append(dq[0][1])
print(' '.join(map(str,res)))