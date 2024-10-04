import sys
input=sys.stdin.readline

n=int(input())
def find_five(num):
    cnt=0
    i=5
    while i<=num:
        cnt+=num//i
        i*=5
    return cnt

res=0
left,right=5,5*10**9
while left<=right:
    mid=(left+right)//2
    if find_five(mid)>=n:
        right=mid-1
        res=mid
    else:
        left=mid+1

if find_five(res)==n:
    print(res)
else:
    print(-1)