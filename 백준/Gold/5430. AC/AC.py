import sys
t = int(input())
for _ in range(t):
  p = sys.stdin.readline().rstrip()
  n = int(input())
  s = sys.stdin.readline().rstrip()[1:-1].split(',')
  k=1
  if(n==0):
    s=[]
  r=1
  for i in p:
    if(i=='R'):
      r*=-1
    elif(i=='D' and len(s)==0):
      print('error')
      k=0
      break
    else:
      del s[(r==-1)*(-1)]
  if(k==1):
    if(r==-1):
      s.reverse()
    print("["+",".join(s)+"]")