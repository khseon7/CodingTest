from collections import deque
n,k=map(int,input().split())
res=[]
left_queue=deque()
right_queue=deque([str(x) for x in range(1,n+1)])
cnt=0
while left_queue or right_queue:
  for _ in range(len(right_queue)):
    cnt+=1
    if cnt==k:
      res.append(right_queue.popleft())
      cnt=0
    else:
      left_queue.append(right_queue.popleft())
  right_queue=left_queue
  left_queue=deque()
print("<"+", ".join(res)+">")