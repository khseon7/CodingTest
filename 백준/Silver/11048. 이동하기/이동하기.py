import sys
input=sys.stdin.readline

N,M=map(int,input().split())

arr=[list(map(int,input().split())) for _ in range(N)]
dp=arr.copy()

for r in range(N):
    if r==0:
        for c in range(M-1):
            dp[r][c+1]=dp[r][c]+arr[r][c+1]
    else:
        for c in range(M):
            if c==0:
                dp[r][c]=dp[r-1][c]+arr[r][c]
            else:
                dp[r][c]=max(dp[r-1][c],dp[r][c-1],dp[r-1][c-1])+arr[r][c]

print(dp[N-1][M-1])