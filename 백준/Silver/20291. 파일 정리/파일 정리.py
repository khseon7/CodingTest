import sys
n=int(input())
extent_dict=dict()
for _ in range(n):
  file_name=sys.stdin.readline().split('.')
  extent=file_name[1].rstrip()
  if extent in extent_dict.keys():
    extent_dict[extent]+=1
  else:
    extent_dict[extent]=1
for i in sorted(extent_dict.keys()):  print(i,extent_dict[i])