def power(n,r,p):
  res=1
  while r!=0:
    if r%2:
      res=res*n%p
    n=n*n%p
    r//=2
  return res
n,m=map(int,input().split())
sum=1
p=1000000007
for i in range(2,int(n**0.5) + 1):
  if n%i==0:
    cnt=0
    while n%i==0:
      n//=i
      cnt+=1
    sum=sum*((power(i,cnt*m+1,p)-1+p)%p)*power(i-1,p-2,p)%p
if n>1:
  sum=sum*((power(n,m+1,p)-1)%p)*power(n-1,p-2,p)%p
print(sum)