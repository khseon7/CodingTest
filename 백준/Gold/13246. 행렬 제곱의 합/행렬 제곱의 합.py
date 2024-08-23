import sys
input=sys.stdin.readline
n,b=map(int,input().split())
mat=[list(map(int,input().split())) for _ in range(n)]
mod=1000
for i in range(n):
    for j in range(n):
        mat[i][j]%=mod

def mul_mat(arr_1,arr_2,mod=1000):
    n=len(arr_1)
    res=[[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j]=(res[i][j]+arr_1[i][k]*arr_2[k][j])%mod
    return res

def pow_mat(A,B):
    res=[[0 if i!=j else 1 for j in range(n)] for i in range(n)]
    while B:
        if B%2:
            res=mul_mat(res,A)
        A=mul_mat(A,A)
        B//=2
    return res

def sum_mat(mat_1,mat_2=None,mod=1000):
    n=len(mat_1)
    if mat_2 is None:
        mat_2=[[0 if i!=j else 1 for j in range(n)] for i in range(n)]
    return [[(mat_1[i][j]+mat_2[i][j])%mod for j in range(n)] for i in range(n)]

def solve(A,B):
    if B==1:
        return A
    left_mat=sum_mat(pow_mat(A,B//2))
    right_mat=solve(A,B//2)
    res=mul_mat(left_mat,right_mat)
    if B%2:
        res=sum_mat(res,pow_mat(A,B))
    return res

for row in solve(mat,b):
    print(" ".join(map(str,row)))