import sys
T=int(sys.stdin.readline())
for _ in range(T):
  a_point,b_point=0,0
  for _ in range(9):
    a,b=map(int,sys.stdin.readline().split())
    a_point=a_point+a
    b_point=b_point+b
  if a_point>b_point:
    print("Yonsei")
  elif a_point==b_point:
    print("Draw")
  else:
    print("Korea")