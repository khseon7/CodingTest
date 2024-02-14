import sys
N=int(sys.stdin.readline())
cute_list=list()
for _ in range(N):
  a=int(sys.stdin.readline())
  cute_list.append(a)
cute=cute_list.count(1)
not_cute=cute_list.count(0)
if cute>not_cute:
  print("Junhee is cute!")
elif cute<not_cute:
  print("Junhee is not cute!")