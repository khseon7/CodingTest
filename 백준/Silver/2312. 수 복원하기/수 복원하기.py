import sys
input=sys.stdin.readline
arr=[1]*100001
prime_list=[]
for i in range(2,100001):
    if arr[i]:
        prime_list.append(i)
        for j in range(2*i,100001,i):
            arr[j]=0
n=int(input())
for _ in range(n):
    test=int(input())
    res_dict={}
    for i in prime_list:
        while not test%i:
            if i in res_dict:
                res_dict[i]+=1
            else:
                res_dict[i]=1
            test//=i
            if test==1:
                break
    for i in res_dict.keys():
        print(i,res_dict[i])