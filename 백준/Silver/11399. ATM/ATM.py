n = int(input())
arr = list(map(int,input().split()))
arr = sorted(arr)
total = 0
for i in range(n):
    total += arr[i]*(n-i)
print(total)