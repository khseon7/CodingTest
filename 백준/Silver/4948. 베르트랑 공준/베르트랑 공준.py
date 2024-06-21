while(True):
  n=int(input())
  if(n==0):
    break
  arr=[1 for _ in range(2*n+1)]
  for i in range(2,2*n+1):
    if(arr[i]==1):
      for j in range(2*i,2*n+1,i):
        arr[j]=0
  arr=arr[n+1:]
  print(arr.count(1))