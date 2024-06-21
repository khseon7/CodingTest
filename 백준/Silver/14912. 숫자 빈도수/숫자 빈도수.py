n,m=map(int,input().split())
cnt=0
for i in range(1,n+1):
  while(i):
    if(i%10==m):
      cnt+=1 
    i//=10
print(cnt)