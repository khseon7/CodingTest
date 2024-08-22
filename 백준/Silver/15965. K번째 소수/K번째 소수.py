import sys
input=sys.stdin.readline
size=8000001
arr=[1]*size
prime_list=[]
for i in range(2,int(size**0.5)+1):
    if arr[i]:
        prime_list.append(i)
        for j in range(2*i,size,i):
            arr[j]=0
for i in range((int(size**0.5)+1),size):
    if arr[i]:
        prime_list.append(i)
n=int(input())
print(prime_list[n-1])