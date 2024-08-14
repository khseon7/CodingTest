import sys
from collections import deque
n=int(input())
left_deque=deque()
right_deque=deque(x for x in range(1,n+1))
cnt=1
while len(left_deque+right_deque)!=1:
  mod=cnt**3%len(left_deque+right_deque)
  if mod:
    for _ in range(mod):
      left_deque.append(right_deque.popleft())
  else:
    for _ in range(len(left_deque+right_deque)):
      left_deque.append(right_deque.popleft())
  left_deque.pop()
  right_deque=right_deque+left_deque
  left_deque=deque()
  cnt+=1
print(right_deque[0])