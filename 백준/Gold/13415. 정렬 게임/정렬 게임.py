from collections import deque
import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
k=int(sys.stdin.readline())

stack=[]

for _ in range(k):
    a,b=map(int,sys.stdin.readline().split())
    for j,k in [(a-1,1),(b-1,-1)]:
        while stack and stack[-1][0]<=j:
            stack.pop()
        stack.append((j,k))
stack.append((-1,0))

sorted_arr=deque(sorted(arr[:stack[0][0]+1]))
for i in range(len(stack)-1):
    cur, type=stack[i]
    next, _=stack[i+1]
    for j in range(cur,next,-1):
        n=sorted_arr.pop() if type==1 else sorted_arr.popleft()
        arr[j]=n

arr=map(str,arr)
print(' '.join(arr))