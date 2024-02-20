import sys
n=int(sys.stdin.readline())
a_point=100
b_point=100
for _ in range(n):
  a,b=map(int,sys.stdin.readline().split())
  if a>b:
    b_point=b_point-a
  elif a<b:
    a_point=a_point-b
print(a_point)
print(b_point)