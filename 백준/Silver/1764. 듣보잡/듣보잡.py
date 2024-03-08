import sys
n,m=map(int,sys.stdin.readline().split())
no_hear_set=set()
no_see_set=set()
for _ in range(n):
  no_hear_set.add(sys.stdin.readline().rstrip())
for _ in range(m):
  no_see_set.add(sys.stdin.readline().rstrip())
res=sorted(no_hear_set&no_see_set)
print(len(res))
for i in res:
  print(i)