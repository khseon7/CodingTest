import sys
k=int(sys.stdin.readline())
zero_list=[]
for _ in range(k):
  n=int(sys.stdin.readline())
  if n==0:
    zero_list.pop()
  else:
    zero_list.append(n)
print(sum(zero_list))