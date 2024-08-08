n,k=map(int,input().split())
arr=[1 for _ in range(n+1)]
res=[]
for i in range(2,n+1):
  if arr[i]:
    res.append(i)
    arr[i]=0
    if len(res)==k:
      break
    for j in range(2*i,n+1,i):
      if arr[j]:
        res.append(j)
        arr[j]=0
        if len(res)==k:
          break
print(res[k-1])