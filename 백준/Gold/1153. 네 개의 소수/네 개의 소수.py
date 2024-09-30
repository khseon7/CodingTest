import sys
input=sys.stdin.readline

size=1000000
n=int(input())
prime_arr=[]
arr=[0,0]+[1]*(size-1)
for i in range(2,size+1):
    if arr[i]:
        prime_arr.append(i)
        for j in range(2*i,size+1,i):
            arr[j]=0

if n<8:
    print(-1)
else:
    if not n%2:
        res=[2,2]
        pre=4
        
    else:
        res=[2,3]
        pre=5
    for i in range(len(prime_arr)):
            if arr[n-pre-prime_arr[i]]:
                res.append(prime_arr[i])
                res.append(n-pre-prime_arr[i])
                print(" ".join(map(str,res)))
                break