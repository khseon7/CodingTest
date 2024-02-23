import sys
sum_list=[]
while True:
  x,y=map(int,sys.stdin.readline().split())
  if x==0 and y==0: break
  else: sum_list.append(x+y)
for i in sum_list:
  print(i)