import sys
input=sys.stdin.readline
k,n=map(int,input().split())
line=list(map(int,input().split()))
def binary_find(arr,count,left,right):
    res=0
    while left<=right:
        sum=0
        mid=(left+right)//2
        for i in arr:
            if i>mid:
                sum+=(i-mid)
        if sum>=count:
            res=mid
            left=mid+1
        else:
            right=mid-1
    return res
print(binary_find(line,n,1,max(line)))