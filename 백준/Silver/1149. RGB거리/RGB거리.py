import sys
input=sys.stdin.readline

n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

for i in range(n-1):
    arr[i+1][0]=min((arr[i][1]+arr[i+1][0]),(arr[i][2]+arr[i+1][0]))
    arr[i+1][1]=min((arr[i][0]+arr[i+1][1]),(arr[i][2]+arr[i+1][1]))
    arr[i+1][2]=min((arr[i][0]+arr[i+1][2]),(arr[i][1]+arr[i+1][2]))

print(min(arr[n-1][0],arr[n-1][1],arr[n-1][2]))