def find(num,array):
    res=0
    start,end=0,len(array)-1
    while start<=end:
        mid=(start+end)//2
        if array[mid]<num:
            res=mid
            start=mid+1
        else:
            end=mid-1
    if array[res]<num:
        res+=1
    return res

import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    arr_a=list(map(int,input().split()))
    arr_b=sorted(list(map(int,input().split())))
    total=0
    for i in arr_a:
        total+=find(i,arr_b)
    print(total)