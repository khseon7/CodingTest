n = int(input())
arr = sorted(list(map(int,input().split())))

total = 0
for i in range(n):
    total += arr[i]*(n-i)

print(total)