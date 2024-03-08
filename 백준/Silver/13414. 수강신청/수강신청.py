import sys
k,l=map(int,sys.stdin.readline().split())
success_dict=dict()
cnt=0
for _ in range(l):
  student=sys.stdin.readline().rstrip()
  if student not in success_dict.keys():
    success_dict[student]=cnt
  else:
    success_dict[student]=cnt
  cnt+=1
convert_success_dict={v:k for k,v in success_dict.items()}
for i in sorted(convert_success_dict.keys())[:k]:
  print(convert_success_dict[i])