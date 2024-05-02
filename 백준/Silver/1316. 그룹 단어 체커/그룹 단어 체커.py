import sys
n=int(input())
cnt=0
cnt_right=0
for i in range(n):
  a=list(sys.stdin.readline().rstrip())
  b=dict()
  flag=0
  for i in range(len(a)):
    if a[i] not in b.keys():
      if i>0:
        b[a[i-1]]=cnt
        cnt=0
      b[a[i]]=0
      cnt+=1
      flag=1
    elif not b[a[i]]:
      cnt+=1
      flag=1
    else:
      flag=0
      break
  if flag==1:
    cnt_right+=1
print(cnt_right)