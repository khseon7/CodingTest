import sys
input=sys.stdin.readline

s,c=map(int,input().split())
arr=[int(input()) for _ in range(s)]

left,right=1,max(arr)
res=0
while left<=right:
    cnt=0
    mid=(left+right)//2
    for i in arr:
        cnt+=i//mid
    if cnt<c:
        right=mid-1
    else:
        left=mid+1
        res=mid
pa=0
cnt=0
for i in arr:
    while cnt!=c and i!=0:
        i-=res
        cnt+=1
    pa+=i
print(pa)