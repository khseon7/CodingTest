import sys
n=int(sys.stdin.readline())
A_set=set(map(int, sys.stdin.readline().split()))
m=int(sys.stdin.readline())
B_list=list(map(int, sys.stdin.readline().split()))
res_list=[]
for i in B_list:
  if i in A_set: res_list.append(1)
  else: res_list.append(0)
for j in res_list:
  print(j)