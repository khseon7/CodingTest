import sys
n=int(input())
arr=[x for x in map(int,sys.stdin.readline().split())]
for i in arr:
  if i==int(i**0.5)**2:
    print(1,end=' ')
  else:
    print(0,end=' ')