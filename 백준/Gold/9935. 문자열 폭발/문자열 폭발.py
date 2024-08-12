import sys
str=sys.stdin.readline().rstrip()
explo_str=sys.stdin.readline().rstrip()
res=[]
stack=[]
for i in range(len(str)):
  res.append(str[i])
  if str[i]==explo_str[-1] and "".join(res[-len(explo_str):])==explo_str:
    for _ in range(len(explo_str)):
      res.pop()
if len(res):
  print("".join(res))
else:
  print("FRULA")