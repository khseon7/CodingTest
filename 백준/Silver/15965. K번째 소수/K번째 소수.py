import sys
input=sys.stdin.readline
arr=[1]*500001
prime_list=[]
for i in range(2,500001):
    if arr[i]:
        prime_list.append(i)
        for j in range(2*i,500001,i):
            arr[j]=0
n=int(input())
print(prime_list[n-1])