import sys
sys.setrecursionlimit(10**8)

input = sys.stdin.readline

def total_sum(r,n,mod):
    if n==1:
        return 1
    else:
        if n%2==0:
            return (1+pow(r,n//2,mod))*total_sum(r,n//2,mod)%mod
        else:
            return (total_sum(r,n-1,mod) + pow(r,n-1,mod))%mod

a, r, n, mod = map(int, input().split())

total=(total_sum(r,n,mod)*a)%mod

print(total)