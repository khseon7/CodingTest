def power(n, r, p):
  res = 1
  while r > 0:
      if r % 2:
          res = res * n % p
      n = n * n % p
      r //= 2
  return res
      
n,k=map(int,input().split())
p=1000000007
arr=[1 for _ in range(n+1)]
for i in range(2,n+1):
  arr[i]=arr[i-1]*i%p
print(arr[n]*power(arr[k]*arr[n-k]%p,p-2,p)%p)