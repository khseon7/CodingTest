import sys
input=sys.stdin.readline

dp=[0,1,2]+[0]*998
div=10007
for i in range(3,1001):
    dp[i]=(dp[i-1]+dp[i-2])%div
n=int(input())
print(dp[n])