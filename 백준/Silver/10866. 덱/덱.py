import sys
from collections import deque
n=int(sys.stdin.readline())
res=deque()
for _ in range(n):
  cmd=sys.stdin.readline().split()
  if cmd[0]=='push_front':
    res.appendleft(cmd[1])
  elif cmd[0]=='push_back':
    res.append(cmd[1])
  elif cmd[0]=='pop_front':
    if res:
      print(res.popleft())
    else:
      print(-1)
  elif cmd[0]=='pop_back':
    if res:
      print(res.pop())
    else:
      print(-1)
  elif cmd[0]=='size':
    print(len(res))
  elif cmd[0]=='empty':
    if res:
      print(0)
    else:
      print(1)
  elif cmd[0]=='front':
    if res:
      print(res[0])
    else:
      print(-1)
  elif cmd[0]=='back':
    if res:
      print(res[-1])
    else:
      print(-1)