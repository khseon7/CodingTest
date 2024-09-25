import sys
input=sys.stdin.readline

m,n=map(int,input().split())

arr=list(map(int,input().split()))

left,right=1,max(arr)
res=0
while left<=right:
    mid=(left+right)//2
    cnt=0
    for i in arr:
        cnt+=i//mid
    if cnt<m:
        right=mid-1
    else:
        left=mid+1
        res=mid
print(res)