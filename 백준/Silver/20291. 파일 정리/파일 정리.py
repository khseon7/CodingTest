import sys
n=int(input())
extent_dict=dict()
for _ in range(n):
  file_name=input().split('.')
  if file_name[1] in extent_dict.keys():
    extent_dict[file_name[1]]+=1
  else:
    extent_dict[file_name[1]]=1
for i in sorted(extent_dict.keys()):  print(i,extent_dict[i])