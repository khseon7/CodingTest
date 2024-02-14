import sys
arr=list(map(int,sys.stdin.readline().split()))
while arr[-1]!=0 or arr[-2]!=0:
  a,b=map(int,sys.stdin.readline().split())
  arr.append(a)
  arr.append(b)
for i in range(0,len(arr)-2,2):
  if arr[i]>arr[i+1]:
    print("Yes")
  else:
    print("No")