import sys
x,y=map(int,sys.stdin.readline().split())
prev=int(y*100/x)
if x==y or prev==99:
  print(-1)
else:
  if ((prev+1)*x-100*y)%(99-prev):
    print(((prev+1)*x-100*y)//(99-prev)+1)
  else:
    print(((prev+1)*x-100*y)//(99-prev))