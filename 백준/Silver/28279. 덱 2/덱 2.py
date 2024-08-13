import sys
from collections import deque
n=int(input())
res_deque=deque()
for _ in range(n):
  cmd=sys.stdin.readline().split()
  if cmd[0]=='1':
    res_deque.appendleft(int(cmd[1]))
  elif cmd[0]=='2':
    res_deque.append(int(cmd[1]))
  elif cmd[0]=='3':
    print(res_deque.popleft()) if res_deque else print(-1)
  elif cmd[0]=='4':
    print(res_deque.pop()) if res_deque else print(-1)
  elif cmd[0]=='5':
    print(len(res_deque))
  elif cmd[0]=='6':
    print(0) if res_deque else print(1)
  elif cmd[0]=='7':
    print(res_deque[0]) if res_deque else print(-1)
  elif cmd[0]=='8':
    print(res_deque[-1]) if res_deque else print(-1)