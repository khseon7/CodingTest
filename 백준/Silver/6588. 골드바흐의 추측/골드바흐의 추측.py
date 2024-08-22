import sys
input=sys.stdin.readline
arr=[1]*1000001
prime_dict={}
for i in range(2,1000001):
    if arr[i]:
        prime_dict[i]=arr[i]
        for j in range(2*i,1000001,i):
            arr[j]=0
while True:
    test=int(input())
    if not test:
        break
    cnt=0
    for i in prime_dict.keys():
        if test-i in prime_dict.keys():
            print(f"{test} = {i} + {test-i}")
            cnt+=1
            break
    if not cnt:
        print("Goldbach's conjecture is wrong.")