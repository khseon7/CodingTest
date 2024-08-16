import sys
s=sys.stdin.readline().rstrip()
res_dict={}
for i in range(1,len(s)+1):
  j=0
  while j+i<=len(s):
    sub_str=s[j:i+j]
    if sub_str not in res_dict:
      res_dict[sub_str]=1
    j+=1
print(len(res_dict))