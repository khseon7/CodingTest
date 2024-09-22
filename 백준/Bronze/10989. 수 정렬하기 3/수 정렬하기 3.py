import sys
input=sys.stdin.readline

n=int(input())
arr=dict()
for _ in range(n):
    x=int(input())
    if x in arr.keys():
        arr[x]+=1
    else:
        arr[x]=1
        
for i in sorted(arr.keys()):
    for _ in range(arr[i]):
        print(i)