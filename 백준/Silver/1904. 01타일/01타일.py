n=int(input())
bt=[1,2]+[0]*999998
for i in range(2,n):
  bt[i]=(bt[i-2]+bt[i-1])%15746
print(bt[n-1])