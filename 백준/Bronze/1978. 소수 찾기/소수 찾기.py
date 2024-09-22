import sys
input=sys.stdin.readline

arr=[0,0]+[1]*999
for i in range(2,1001):
    if arr[i]:
        for j in range(2*i,1001,i):
            arr[j]=0

n=int(input())
array=map(int,input().split())
cnt=0
for i in array:
    if arr[i]:
        cnt+=1
print(cnt)