# 피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
# 이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.
# n=17일때 까지 피보나치 수를 써보면 다음과 같다.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
# n과 m이 주어졌을 때, n번째 피보나치 수와 m번째 피보나치 수의 최대공약수를 구하는 프로그램을 작성하시오.

def power(arr_1, arr_2):
  size=int(len(arr_1)**(1/2))
  res=[0]*size**2
  for i in range(size):
    for j in range(size):
      for k in range(size):
        res[i*size+j]+=arr_1[i*size+k]*arr_2[k*size+j]
      res[i*size+j]%=1000000007
  return res

def fibo(n):
  if(n==0):
    return 0
  elif(n==1):
    return 1
  else:
    n-=1
    res=[1,0,0,1]
    mat=[1,1,1,0]
    while(n!=0):
      if(n%2==1):
        res=power(mat,res)
      mat=power(mat,mat)
      n//=2
    return res[0]

def gcd(a,b):
  while b!=0:
    a,b=b,a%b
  return a

n,m=map(int,input().split())
print(fibo(gcd(n,m)))