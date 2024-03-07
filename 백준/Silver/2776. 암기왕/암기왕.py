import sys
t=int(sys.stdin.readline())
res_list=[]
for i in range(t):
  n=int(sys.stdin.readline())
  n_set=set(map(int,sys.stdin.readline().split()))
  m=int(sys.stdin.readline())
  m_list=list(map(int,sys.stdin.readline().split()))
  for i in m_list:
    if i in n_set:
      res_list.append('1')
    else:
      res_list.append('0')
print('\n'.join(res_list))