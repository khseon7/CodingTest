import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
res = [-1] * n
stack = []
for i in range(n-1, -1, -1):
    while stack and stack[-1] <= arr[i]:
        stack.pop()
    if stack:
        res[i] = stack[-1]
    stack.append(arr[i])
print(" ".join(map(str, res)))
