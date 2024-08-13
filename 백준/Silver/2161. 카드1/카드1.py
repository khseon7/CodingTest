import sys
from collections import deque
n=int(input())
card_deque=deque(str(x) for x in range(1,n+1))
res=[]
while len(card_deque)!=1:
  res.append(card_deque.popleft())
  card_deque.append(card_deque.popleft())
res.append(card_deque.pop())
print(" ".join(res))