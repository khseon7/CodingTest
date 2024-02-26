import sys
global stack
stack=[]
def push(x):
  stack.append(x)
def pop():
  if stack==[]:
    return -1
  else:
    return stack.pop()
def size():
  return len(stack)
def empty():
  if len(stack)==0:
    return 1
  else:
    return 0
def top():
  if stack==[]:
    return -1
  else:
    return stack[-1]
n=int(sys.stdin.readline())
res_list=[]
for _ in range(n):
  cmd=sys.stdin.readline().split()
  if cmd[0]=='push':
    push(cmd[1])
  elif cmd[0]=='pop':
    res_list.append(pop())
  elif cmd[0]=='size':
    res_list.append(size())
  elif cmd[0]=='empty':
    res_list.append(empty())
  elif cmd[0]=='top':
    res_list.append(top())
for i in res_list:
  print(i)