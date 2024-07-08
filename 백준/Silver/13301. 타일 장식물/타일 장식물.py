n=int(input())
len=[0]*(n+1)
len[0]=1
len[1]=1
for i in range(2,n+1):
  len[i]=len[i-1]+len[i-2]
print(len[n]*2+len[n-1]*2)