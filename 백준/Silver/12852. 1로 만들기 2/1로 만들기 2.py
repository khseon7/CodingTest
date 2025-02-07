import sys
input=sys.stdin.readline

N=int(input())

arr=[0,0]+[i for i in range(2,N+1)]
res=[]

for i in range(2,N+1):
    arr[i]=arr[i-1]+1
    if i%2==0 and arr[i//2]+1<arr[i]:
        arr[i]=arr[i//2]+1
    if i%3==0 and arr[i//3]+1<arr[i]:
        arr[i]=arr[i//3]+1

print(arr[N])
res.append(str(N))
while N!=1:
    idx=N-1
    if N%2==0 and arr[N//2]+1==arr[N]:
        idx=N//2
    if N%3==0 and arr[N//3]+1==arr[N]:
        idx=N//3
    N=idx
    res.append(str(N))

print(" ".join(res))