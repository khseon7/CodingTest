import sys
input=sys.stdin.readline
n=int(input())
money=list(map(int,input().split()))
total=int(input())
def binary_find(arr,target,left,right):
    res=0
    while left<=right:
        total_sum=0
        mid=(left+right)//2
        total_sum=sum(min(i,mid) for i in arr)
        if total_sum<=target:
            left=mid+1
            res=mid
        else:
            right=mid-1         
    return res
print(binary_find(money,total,1,max(money)))