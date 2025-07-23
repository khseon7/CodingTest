n = int(input())
po = [0] * 10001
dp = [0] * 10001

for i in range(1,n+1):
    po[i] = int(input())

dp[1] = po[1]
dp[2] = po[1] + po[2]
for i in range(3, n+1):
    dp[i] = max(dp[i-2] + po[i], dp[i-3] + po[i-1] + po[i], dp[i-1])

print(dp[n])