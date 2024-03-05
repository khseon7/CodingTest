import sys
n_dict=dict()
n=int(sys.stdin.readline())
for i in list(map(int,sys.stdin.readline().split())):
    if i in n_dict.keys():
        n_dict[i]+=1
    else:
        n_dict[i]=1
m=int(sys.stdin.readline())
card_list=[]
for i in list(map(int,sys.stdin.readline().split())):
    if i in n_dict.keys():
        card_list.append(str(n_dict.get(i)))
    else:
        card_list.append("0")
print(' '.join(card_list))