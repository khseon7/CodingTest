a,b,c=map(int,input().split())
res=1
while(b!=0):
  if(b%2==1):
    res*=a
  a*=a
  a%=c
  b//=2
print(res%c)