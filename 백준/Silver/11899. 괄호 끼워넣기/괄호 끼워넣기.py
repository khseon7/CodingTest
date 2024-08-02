import sys
x=sys.stdin.readline().rstrip()
arr=[]
for i in x:
  if i=='(' or i=='[':
    arr.append(i)
  elif i==')':
    if len(arr)==0 or arr[-1]!='(':
      arr.append(i)
    else:
      arr.pop()
  elif i==']':
    if len(arr)==0 or arr[-1]!='[':
      arr.pop()
    else:
      arr.append(i)
print(len(arr))