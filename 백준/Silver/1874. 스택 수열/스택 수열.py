import sys
n=int(sys.stdin.readline())
stack=[0]
op_list=[]
cnt=1
res=1
for _ in range(n):
  x=int(sys.stdin.readline())
  while True:
    if x>stack[-1]:
      stack.append(cnt)
      op_list.append('+')
      cnt+=1
    elif x==stack[-1]:
      stack.pop()
      op_list.append('-')
      break
    elif x<stack[-1]:
      stack.pop()
      op_list.append('-')
    if x>stack[-1] and x<cnt:
      res=0
      break
if res==1:
  print('\n'.join(op_list))
else:
  print('NO')