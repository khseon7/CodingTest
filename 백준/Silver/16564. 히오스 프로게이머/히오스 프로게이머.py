import sys
input=sys.stdin.readline
n,k=map(int,input().split())
arr=[int(input()) for _ in range(n)]
def binary_find(arr,target,left,right):
    res=0
    while left<=right:
        total_sum=0
        mid=(left+right)//2
        for i in arr:
            if i<mid:
                total_sum+=mid-i
        if total_sum<=target:
            res=mid
            left=mid+1
        else:
            right=mid-1
    return res
print(binary_find(arr,k,1,max(arr)+k))