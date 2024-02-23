import sys
T=int(sys.stdin.readline())
credit_list=[]
GPA_list=[]
for _ in range(T):
  n=int(sys.stdin.readline())
  credits_sum=0
  GPA_avg=0.0
  for _ in range(n):
    x,y=sys.stdin.readline().split()
    x=int(x)
    y=float(y)
    credits_sum+=x
    GPA_avg+=x*y
  credit_list.append(credits_sum)
  GPA_list.append(round(GPA_avg/credits_sum,1))
for i in range(T):
  print(credit_list[i],GPA_list[i])