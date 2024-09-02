import sys
input=sys.stdin.readline
n,m=map(int,input().split())
arr=list(map(int,input().split()))
left,right=max(arr),sum(arr)
res=right
while left<=right:
    mid=(left+right)//2
    cnt=1
    total=0
    for i in arr:
        if total+i>mid:
            cnt+=1
            total=0
        total+=i
    if cnt<=m:
        res=mid
        right=mid-1
    else:
        left=mid+1
print(res)