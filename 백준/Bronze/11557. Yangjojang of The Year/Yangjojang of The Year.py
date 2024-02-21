import sys
t=int(sys.stdin.readline())
drink_list=[]
for _ in range(t):  
  n=int(sys.stdin.readline())
  coll=[]
  drink_num=[]
  for _ in range(n):
    name, drink=input().split()
    drink=int(drink)
    coll.append(name)
    drink_num.append(drink)
  drink_list.append(coll[drink_num.index(max(drink_num))])
for i in range(len(drink_list)):
  print(drink_list[i])