def power(arr_1,arr_2,n):
  res=[0]*n**2
  for i in range(n):
    for j in range(n):
      for k in range(n):
        res[i*n+j]+=arr_1[n*i+k]*arr_2[n*k+j]
      res[i*n+j]%=1000
  return res

n,b=map(int,input().split())
arr=[0]*n**2
for i in range(n):
  x=input().split()
  for j in range(len(x)):
    arr[i*n+j]=int(x[j])

arr_i=[0]*n**2
for i in range(n):
  arr_i[i*n+i]=1

while(b!=0):
  if(b%2==1):
    arr_i=power(arr_i,arr,n)
  arr=power(arr,arr,n)
  b//=2
for i in range(n**2):
  if(i!=0 and i%n==n-1):
    print(arr_i[i])
  else:
    print(arr_i[i],end=" ")