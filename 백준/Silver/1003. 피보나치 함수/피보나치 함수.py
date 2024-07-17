t=int(input())
fibo_arr=[0,0]*41
fibo_arr[0]=1,0
fibo_arr[1]=0,1
for _ in range(t):
  n=int(input())
  for i in range(2,n+1):
    a=fibo_arr[i-1][0]+fibo_arr[i-2][0]
    b=fibo_arr[i-1][1]+fibo_arr[i-2][1]
    fibo_arr[i]=a,b
  print(fibo_arr[n][0],fibo_arr[n][1])