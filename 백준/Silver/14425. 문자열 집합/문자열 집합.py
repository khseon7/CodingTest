import sys
n,m=map(int, sys.stdin.readline().split())
tuple_list={}
cnt=0
for _ in range(n):
  x=sys.stdin.readline().rstrip()
  tuple_list[x]=1
for _ in range(m):
  x=sys.stdin.readline().rstrip()
  if (tuple_list.get(x)==1): cnt+=1
print(cnt)