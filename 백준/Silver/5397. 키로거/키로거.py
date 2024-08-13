import sys
from collections import deque
n=int(input())
for _ in range(n):
  L=sys.stdin.readline().rstrip()
  left_deque=deque()
  right_deque=deque()
  for i in L:
    if i=='<':
      if left_deque:
        right_deque.appendleft(left_deque.pop())
    elif i=='>':
      if right_deque:
        left_deque.append(right_deque.popleft())
    elif i=='-':
      if left_deque:
        left_deque.pop()
    else:
      left_deque.append(i)
  print("".join(left_deque+right_deque))