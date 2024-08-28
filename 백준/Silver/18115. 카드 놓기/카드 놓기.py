from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
arr=list(reversed(list(map(int,input().split()))))
res=deque()
for i in range(len(arr)):
    value=i+1
    if arr[i]==1 or len(res)<1:
        res.appendleft(value)
    elif arr[i]==2:
        temp=res.popleft()
        res.appendleft(value)
        res.appendleft(temp)
    elif arr[i]==3:
        res.append(value)
print(" ".join(map(str,res)))