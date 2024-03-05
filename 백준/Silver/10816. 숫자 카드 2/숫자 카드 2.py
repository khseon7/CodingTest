import sys
n_dict=dict()
n=int(sys.stdin.readline())
for i in list(map(int,sys.stdin.readline().split())):
    if i in n_dict.keys():
        n_dict[i]+=1
    else:
        n_dict[i]=1
m=int(sys.stdin.readline())
m_list=list(map(int,sys.stdin.readline().split()))
# 상근이가 어떤 카드를 몇개 가지고 있는지 나타내는 card_list 생성
card_list=[]
# m_list에서 각 항들이 n_dict의 key값 중 하나라면 해당 key의 value값을 str 문자형으로 바꿔서 card_list에 추가
for i in m_list:
    if i in n_dict.keys():
        card_list.append(str(n_dict.get(i)))
    else:
        card_list.append("0")
print(' '.join(card_list))