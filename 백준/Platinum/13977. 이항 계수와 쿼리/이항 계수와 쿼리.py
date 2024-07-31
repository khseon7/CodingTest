import sys
def power(n, r, p):
  res = 1
  while r != 0:
      if r % 2:
          res = res * n % p
      n = n * n % p
      r //= 2
  return res

m=int(sys.stdin.readline())
p=1000000007
max=4000000
fact=[1 for _ in range(max+1)]
for i in range(2,max+1):
  fact[i]=fact[i-1]*(i%p)%p
for _ in range(m):
  n,k=map(int,sys.stdin.readline().split())
  print(fact[n]*(power(fact[n-k]*fact[k]%p,p-2,p)%p)%p)