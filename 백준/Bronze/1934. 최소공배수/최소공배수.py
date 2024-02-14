import sys
num=int(sys.stdin.readline())
list=list()
for _ in range(num):
  a,b=map(int, sys.stdin.readline().split())
  c=a*b
  while b!=0:
    a,b=b,a%b
  list.append(int(c/a))
for i in range(len(list)):
  print(list[i])