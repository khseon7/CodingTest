import sys
input=sys.stdin.readline

a,b=map(int,input().split())
mod=1000000007

def power(n, r, p):
    if n==1: return 1
    res = 1
    while r != 0:
        if r % 2:
            res = res * n % p
        n = n * n % p
        r //= 2
    return res
if a==1:
    print(b%mod)
elif b==1:
    print(1)
else:
    print((power(a,b,mod)-1+mod)%mod*(power((a-1),mod-2,mod))%mod)