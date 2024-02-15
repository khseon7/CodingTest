import sys
case_num=int(sys.stdin.readline())
res_list=list()
for _ in range(case_num):
  x=list(input())
  sum=0
  count=1
  for i in range(len(x)):
    if x[i]=='O':
      sum=sum+count
      count+=1
    elif x[i]=='X':
      count=1
  res_list.append(sum)
for i in range(len(res_list)):
  print(res_list[i])