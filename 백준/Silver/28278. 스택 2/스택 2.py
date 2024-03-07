import sys
n=int(input())
stack=[]
res=[]
for _ in range(n):
  a=list(map(int,sys.stdin.readline().split()))
  if a[0]==1:    stack.append(a[1])
  elif a[0]==2:  res.append(str(stack.pop())) if stack else res.append('-1')
  elif a[0]==3:  res.append(str(len(stack)))
  elif a[0]==4:  res.append('0') if stack else res.append('1')
  elif a[0]==5:  res.append(str(stack[-1])) if stack else res.append('-1')
print('\n'.join(res))