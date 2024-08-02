def power(n,r,p):
  res=1
  while r!=0:
    if r%2:
      res=(res*n)%p
    n=n*n%p
    r//=2
  return res
n,k=map(int,input().split())
mod=10007
fact=[1]*(n+1)
for i in range(2, n+1):
  fact[i]=fact[i-1]*i%mod
print(fact[n]*power(fact[n-k]*fact[k]%mod,mod-2,mod)%mod)