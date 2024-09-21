import sys
input=sys.stdin.readline

prime_arr=[]

size=4000000
arr=[0,0]+[1]*(size-1)
for i in range(2,size+1):
    if arr[i]:
        prime_arr.append(i)
        for j in range(2*i,size+1,i):
            arr[j]=0

n=int(input())

cnt=0
for i in range(len(prime_arr)):
    sum=0
    for j in range(i,len(prime_arr)):
        sum+=prime_arr[j]
        if sum>=n:
            break
    if sum==n:
        cnt+=1

print(cnt)