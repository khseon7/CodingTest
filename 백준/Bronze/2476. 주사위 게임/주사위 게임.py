import sys
N=int(sys.stdin.readline())
money_list=list()
for _ in range(N):
  a,b,c=map(int,sys.stdin.readline().split())
  if a==b==c:
    money=10000+a*1000
  elif a==b!=c or a==c!=b:
    money=1000+a*100
  elif a!=b==c:
    money=1000+b*100
  else:
    money=max(a,b,c)*100
  money_list.append(money)
print(max(money_list))