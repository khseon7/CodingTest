import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=list(map(int,input().split()))

left,right=1,max(arr)*m
res=0
while left<=right:
    mid=(left+right)//2
    cnt=0
    for i in arr:
        cnt+=mid//i
    if cnt>=m:
        right=mid-1
        res=mid
    else:
        left=mid+1
print(res)