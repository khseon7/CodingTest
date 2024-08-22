import sys
input=sys.stdin.readline
k,n=map(int,input().split())
line=[int(input()) for _ in range(k)]
def binary_find(arr,count,left,right):
    res=0
    while left<=right:
        sum=0
        mid=(left+right)//2
        for i in arr:
            sum+=i//mid
        if sum>=count:
            res=mid
            left=mid+1
        elif sum>count:
            left=mid+1
        else:
            right=mid-1
    return res
print(binary_find(line,n,1,max(line)))