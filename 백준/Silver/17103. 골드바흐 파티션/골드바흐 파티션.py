import sys
input=sys.stdin.readline
size=1000000
arr=[0,0]+[1]*(size-1)
p_arr=[]
for i in range(2,size+1):
    if arr[i]:
        p_arr.append(i)
        for j in range(2*i,size+1,i):
            arr[j]=0

t=int(input())
res=[]
for _ in range(t):
    n=int(input())
    cnt=0
    for i in p_arr:
        if i>n//2:
            break
        else:
            if arr[n-i]:
                cnt+=1
    res.append(cnt)
print("\n".join(map(str,res)))