import sys
input=sys.stdin.readline

N=int(input())
arr=list(map(int,input().split()))
dp=[1]*N

for i in range(N):
    for j in range(i):
        if arr[i]<arr[j] and dp[i]<dp[j]+1:
            dp[i]=dp[j]+1

print(max(dp))