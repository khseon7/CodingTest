import sys
arr=list(map(int,sys.stdin.readline().split()))
while arr[-1]!=0 or arr[-2]!=0:
  num1, num2=map(int, sys.stdin.readline().split())
  arr.append(num1)
  arr.append(num2)
for i in range(0,len(arr)-3,2):
  print(arr[i]+arr[i+1])