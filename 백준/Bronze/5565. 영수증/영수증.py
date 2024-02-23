import sys
all_price=int(sys.stdin.readline())
sum=0
for _ in range(9):
  price=int(sys.stdin.readline())
  sum+=price
print(all_price-sum)