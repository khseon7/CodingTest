t=int(input())
for _ in range(t):
  n=int(input())
  arr=[1]*n
  for i in range(3,n):
    arr[i]=arr[i-2]+arr[i-3]
  print(arr[n-1])