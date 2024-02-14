import sys
price, num, money=list(map(int,sys.stdin.readline().split()))
if price*num-money<0:
  print(0)
else:
  print(price*num-money)