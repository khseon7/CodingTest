def gcd(a,b):
  if(a%b==0):
    return b
  else:
    return gcd(b, a%b)
a,b=map(int,input().split())
c=b//a
mul=int(c**(1/2))
r=c%mul
while(r!=0 or (gcd(c//mul,mul)!=1)):
  mul-=1
  r=c%mul
print(a*mul,a*(c//mul))