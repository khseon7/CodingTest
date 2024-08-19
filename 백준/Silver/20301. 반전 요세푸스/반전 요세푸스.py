from collections import deque
import sys
input=sys.stdin.readline
n,k,m=map(int,input().split())
dq=deque(i+1 for i in range(n))
res=[]
flag=1
cnt=0
while len(dq)!=1:
    if flag==1:
        dq.rotate(-k+1)
    if flag==-1:
        dq.rotate(k)
    res.append(dq.popleft())
    cnt+=1
    if cnt==m:
        flag*=-1
        cnt=0
res.append(dq[0])
print('\n'.join(map(str,res)))