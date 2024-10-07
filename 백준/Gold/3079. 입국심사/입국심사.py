import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[int(input()) for _ in range(n)]

left,right=1,10e18
res=0
while left<=right:
    mid=int((left+right)//2)
    total=0
    for i in arr:
        total+=mid//i
    if total<m:
        left=mid+1
    else:
        right=mid-1
        res=mid
print(res)