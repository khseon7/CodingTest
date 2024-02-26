import sys
n=int(sys.stdin.readline())
vpa_list=list()
for _ in range(n):
  x=list(input())
  ex_list=[]
  for j in x:
    if j=='(':
      ex_list.append(j)
    elif j==')':
      if len(ex_list)==0:
        ex_list.append(j)
        break
      elif ex_list[-1]=='(':
        ex_list.pop()
      else:
        ex_list.append(j)
        break
  if ex_list==[]:
    vpa_list.append('YES')
  else:
    vpa_list.append('NO')
for i in vpa_list:
  print(i)