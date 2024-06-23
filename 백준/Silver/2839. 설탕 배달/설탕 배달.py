n=int(input())
num=[]
for i in range(n//5+1):
  for j in range((n-5*i)//3+1):
    if(5*i+3*j==n):
      num.append(i+j)
if(len(num)==0): print(-1)
else: print(min(num))