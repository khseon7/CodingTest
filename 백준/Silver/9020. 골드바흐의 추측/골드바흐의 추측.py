import sys
input=sys.stdin.readline

size=10000
arr=[0,0]+[1]*(size-1)
prime=[]

for i in range(2,size+1):
    if arr[i]:
        prime.append(i)
        for j in range(2*i,size+1,i):
            arr[j]=0

t=int(input())
for _ in range(t):
    n=int(input())
    one,two=0,0
    for i in prime:
        if i<=n//2 and arr[n-i]:
            one,two=i,n-i
    print(one, two)