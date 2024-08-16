import sys
n=int(input())
res_dict={}
for _ in range(n):
  num=int(input())
  if num in res_dict:
    res_dict[num]+=1
  else:
    res_dict[num]=1
max_val=max(res_dict.values())
for i in sorted(list(res_dict.keys())):
  if res_dict[i]==max_val:
    print(i)
    break