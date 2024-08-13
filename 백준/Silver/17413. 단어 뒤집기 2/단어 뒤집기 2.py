import sys
s=sys.stdin.readline().rstrip()
stack=[]
res=[]
flag=0
for i in s:
  if i=='<':
    res.append("".join(stack[::-1]))
    stack=[]
    flag=1
    stack.append(i)
  elif flag and i!='>':
    stack.append(i)
  elif i=='>':
    stack.append(i)
    res.append("".join(stack))
    stack=[]
    flag=0
  elif flag==0:
    if i==' ':
      res.append("".join(stack[::-1]))
      res.append(" ")
      stack=[]
    else:
      stack.append(i)
if stack:
  res.append("".join(stack[::-1]))
print("".join(res))