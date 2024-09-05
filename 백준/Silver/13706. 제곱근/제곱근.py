import sys
input=sys.stdin.readline
n=int(input())
left,right=1,n
res=0
while left<=right:
    mid=(left+right)//2
    if mid**2>n:
        right=mid-1
    elif mid**2<n:
        left=mid+1
    else:
        res=mid
        break
print(res)