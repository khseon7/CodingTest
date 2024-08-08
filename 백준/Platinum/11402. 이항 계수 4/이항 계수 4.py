def lucas(n,k):
  if n<k:
    return 0
  if n==k or k==0:
    return 1
  x=1
  for i in range(1,k+1):
    x=(x*(n-i+1))//i
  return x

def bino(n,k,m):
  arr_n=[]
  arr_k=[]
  while n or k:
    arr_n.append(n%m)
    arr_k.append(k%m)
    n//=m
    k//=m
  res=1
  for i in range(len(arr_n)):
    res=res*lucas(arr_n[i],arr_k[i])%m
  return res

import sys
n,k,m=map(int,sys.stdin.readline().split())
print(bino(n,k,m))