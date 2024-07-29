def power(arr_1,arr_2):
  res=[0,0,0,0]
  for i in range(2):
    for j in range(2):
      for k in range(2):
        res[i*2+j]+=arr_1[i*2+k]*arr_2[k*2+j]
      res[i*2+j]%=1000000007
  return res

def fibo(n):
    front=[1,1,1,0]
    res=[1,0,0,1]

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        n -= 1
        while n != 0:
            if n % 2 == 1:
                res = power(res, front)
            front = power(front, front)
            n//=2
        return res[0]

n=int(input())
print((fibo(n)*fibo(n+1))%1000000007)