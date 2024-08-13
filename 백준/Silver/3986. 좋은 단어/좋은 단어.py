import sys
n=int(input())
cnt=0
for _ in range(n):
  s=sys.stdin.readline().rstrip()
  stack=[]
  for i in s:
    if not stack:
      stack.append(i)
    elif i=='A':
      if stack[-1]=='A':
        stack.pop()
      else:
        stack.append(i)
    elif i=='B':
      if stack[-1]=='B':
        stack.pop()
      else:
        stack.append(i)
  if not stack:
    cnt+=1
print(cnt)