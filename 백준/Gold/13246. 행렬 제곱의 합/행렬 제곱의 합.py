import sys
input=sys.stdin.readline
mod=1000
n,b=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        arr[i][j]%=mod

def mul_mat(arr_1,arr_2,mod=1000):
    n=len(arr)
    res=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j]=(res[i][j]+arr_1[i][k]*arr_2[k][j])%mod
    return res
    
def power(arr,n):
    res=[[0]*len(arr) for _ in range(len(arr))]
    for i in range(len(arr)):
        res[i][i]=1
    while n:
        if n%2:
            res=mul_mat(res,arr)
        arr=mul_mat(arr,arr)
        n//=2
    return res

def mat_plus(arr,arr_b=None,mod=1000):
    n=len(arr)
    if arr_b is None:
        arr_b=[[0 if i!=j else 1 for j in range(n)] for i in range(n)]
    return [[(arr[i][j]+arr_b[i][j])%mod for j in range(n)] for i in range(n)]
    
def solve(arr,b):
    if b==1:
        return arr
    left_mat=mat_plus(power(arr,b//2))
    right_mat=solve(arr,b//2)
    res=mul_mat(left_mat,right_mat)
    if b%2:
        res=mat_plus(res,power(arr,b))
    return res

for i in solve(arr,b):
    print(" ".join(map(str,i)))