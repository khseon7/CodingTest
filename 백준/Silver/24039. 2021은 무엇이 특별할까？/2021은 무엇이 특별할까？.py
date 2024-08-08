arr=[1 for _ in range(10001)]
prime_num=[]
for i in range(2,int(10001**0.5)+1):
  if arr[i]:
    prime_num.append(i)
    for j in range(i*2,10001,i):
      arr[j]=0
for i in range(int(10001**0.5)+1,10001):
  if arr[i]:
    prime_num.append(i)
n=int(input())
for i in range(len(prime_num)-1):
  if prime_num[i]*prime_num[i+1]>n:
    print(prime_num[i]*prime_num[i+1])
    break