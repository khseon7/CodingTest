import sys
input=sys.stdin.readline
n,m=map(int,input().split())
arr=[int(input()) for _ in range(n)]
left,right=max(arr),sum(arr)
res=0
while left<=right:
    mid=(left+right)//2
    cnt=1
    total=mid
    for money in arr:
        if total>=money:
            total-=money
        else:
            cnt+=1
            if money>mid:
                mid=money
            total=mid-money
    if m<cnt:
        left=mid+1
    else:
        res=mid
        right=mid-1
print(res)