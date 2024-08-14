n,m=map(int,input().split())
arr=[1]*101
for i in range(2,n+1):
  arr[i]=i*arr[i-1]
print(arr[n]//arr[m]//arr[n-m])