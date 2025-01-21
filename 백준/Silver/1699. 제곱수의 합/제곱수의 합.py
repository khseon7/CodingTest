import sys
input=sys.stdin.readline

n=int(input())
arr=[i for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,int(i**(1/2))+1):
        arr[i]=min(arr[i],arr[i-(j*j)]+1)
print(arr[n])