def gcd(a,b):
  if a == 0:
      return b
  return gcd(b%a,a)

def power(n,r):
  res=1
  while r>0:
    if r%2==1:
      res=res*n%1000000007
    n=n*n%1000000007
    r//=2
  return res

def mod_inv(n):
  return power(n,1000000005)

m=int(input())
den=1 # 분모
mol=0 # 분자
res=0
for _ in range(m):
  n,s=map(int,input().split())
  tmp=gcd(s,n)
  if tmp!=1:
    s//=tmp
    n//=tmp
  res+=s*mod_inv(n)%1000000007
  res%=1000000007
print(res)