import sys
from collections import deque
n=int(input())
card_deque=deque(x for x in range(1,n+1))
while len(card_deque)!=1:
  card_deque.popleft()
  card_deque.append(card_deque.popleft())
print(card_deque[0])