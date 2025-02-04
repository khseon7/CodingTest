import sys

input = sys.stdin.readline

n=int(input())
size=10**6
div=10**9+9
arr=[0]*(size+1)
arr[1]=1
arr[2]=2
arr[3]=4
for idx in range(4,10**6+1):
    arr[idx]=(arr[idx-1]%div+arr[idx-2]%div+arr[idx-3]%div)%div
for i in range(n):
    x=int(input())
    print(arr[x])