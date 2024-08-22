import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
m=int(input())
test_arr=list(map(int,input().split()))
arr=sorted(arr)
res=[]
def binary_find(arr,target_value,left,right):
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target_value:
            return 1
        elif arr[mid]<target_value:
            left=mid+1
        else:
            right=mid-1
    return 0
for i in test_arr:
    res.append("1") if binary_find(arr,i,0,n-1) else res.append('0')
print(" ".join(res))