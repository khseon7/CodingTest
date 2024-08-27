import sys
input=sys.stdin.readline
size=1000000
arr=[1]*(size+1)
res=[]
def sang(n):
    res=str(n)
    seen=set()
    while True:
        total_sum=0
        for i in res:
            total_sum+=int(i)**2
        if total_sum in seen:
            return False
        if total_sum==1:
            return True
        seen.add(total_sum)
        res=str(total_sum)

for i in range(2,size+1):
    if arr[i]:
        if sang(i):
            res.append(i)
        for j in range(2*i,size+1,i):
            arr[j]=0

n=int(input())
for i in range(len(res)):
    if res[i]<=n:
        print(res[i])
    else:
        break