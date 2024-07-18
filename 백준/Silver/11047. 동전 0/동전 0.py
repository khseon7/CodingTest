n,k=map(int,input().split())
arr=[0]*1000000
cnt=0
for i in range(n):
  arr[i]=int(input())
for i in range(n-1,-1,-1):
  cnt+=k//arr[i]
  k%=arr[i]
print(cnt)