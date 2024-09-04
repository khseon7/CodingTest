import sys
input=sys.stdin.readline
size=3000000
arr=[0,0]+[1]*(size-1)
prime_arr=[]
for i in range(2,size+1):
    if arr[i]==1:
        prime_arr.append(i)
        for j in range(2*i,size+1,i):
            arr[j]=0
t=int(input())
for _ in range(t):
    k=int(input())
    if arr[k]:
        print(0)
    else:
        left,right=0,len(prime_arr)-1
        res=0
        while left<=right:
            mid=(left+right)//2
            if prime_arr[mid]<k:
                res=mid
                left=mid+1
            elif prime_arr[mid]>k:
                right=mid-1
        print(prime_arr[res+1]-prime_arr[res])