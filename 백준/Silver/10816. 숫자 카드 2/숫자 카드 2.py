import sys
n_dict=dict()
n=int(sys.stdin.readline())
n_list=list(map(int,sys.stdin.readline().split()))
for i in n_list:
  if i in n_dict:
    n_dict[i]+=1
  else:
    n_dict[i]=1
m=int(sys.stdin.readline())
m_list=list(map(int,sys.stdin.readline().split()))
card_list=[]
for i in m_list:
  if i in n_dict:
    card_list.append(str(n_dict.get(i)))
  else:
    card_list.append("0")
print(' '.join(card_list))