import sys
a,b=map(int, sys.stdin.readline().split())
c=a*b
while b!=0:
  a,b=b,a%b
print(a)
print(int(c/a))