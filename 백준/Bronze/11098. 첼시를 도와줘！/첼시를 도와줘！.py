import sys
n=int(sys.stdin.readline())
name_list=[]
for _ in range(n):
  p=int(sys.stdin.readline())
  player_price=[]
  player_name=[]
  for _ in range(p):
    price,name=sys.stdin.readline().split()
    price=int(price)
    player_name.append(name)
    player_price.append(price)
  name_list.append(player_name[player_price.index(max(player_price))])
for i in name_list:
  print(i)