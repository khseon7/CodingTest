import sys
input=sys.stdin.readline

k=int(input())
arr=[0]+list(map(int,input().split()))

for i in range(k-1,-1,-1):
    step=2**i
    for j in range(step,2**k,step*2):
        print(arr[j],end=" ")
    print()
