m,n=map(int,input().split())
size=n+1
arr=[1]*size
arr[1]=0
for i in range(2,int(n**(1/2))+1):
  if arr[i]==1:
    for j in range(2*i,size,i):
      arr[j]=0
for i in range(m,size):
  if arr[i]==1:
    print(i)