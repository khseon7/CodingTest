fibo=[0]*2000000
fibo[0]=0
fibo[1]=1
n=int(input())
if (n>0):
  for i in range(2,n+1):
    fibo[i]=(fibo[i-1]+fibo[i-2])%1000000000
else:
  for i in range(-1,n-1,-1):
    res=abs(fibo[i+2]-fibo[i+1])%1000000000
    fibo[i]=res if(fibo[i+2]-fibo[i+1])>0 else -res
if(fibo[n]>0):
  print(1)
elif(fibo[n]==0):
  print(0)
else:
  print(-1)
print(abs(fibo[n]))