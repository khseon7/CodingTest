import sys
input=sys.stdin.readline

n,k=map(int,input().split())

arr=[]
for _ in range(n):
    x=int(input())
    if x:
        arr.append(x)

res=0

if arr:
    left,right=1,max(arr)
    while(left<=right):
        mid=(left+right)//2
        cnt=0
        for i in arr:
            cnt+=i//mid
        if cnt<k:
            right=mid-1
        else:
            left=mid+1
            res=mid
print(res)