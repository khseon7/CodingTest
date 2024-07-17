a,b,n=map(int,input().split())
arr=[0]*1000001
arr[0]=a%b
div=0
for i in range(0,n):
  div=arr[i]*10//b
  arr[i+1]=arr[i]*10%b
print(div)