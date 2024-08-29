from itertools import combinations
import sys
def sep_prime(n):
    res=[]
    for div in range(2,int(n**0.5)+1):
        if not n%div:
            res.append(div)
            while not n%div:
                n//=div
    if n!=1:
        res.append(n)
    return res

input=sys.stdin.readline
t=int(input())
for k in range(t):
    a,b,n=map(int,input().split())
    result_a,result_b=a-1,b
    prime=sep_prime(n)
    for i in range(1,len(prime)+1):
        for comb in combinations(prime,i):
            temp=1
            for j in comb:
                temp*=j
            if i%2:
                result_a-=(a-1)//temp
                result_b-=b//temp
            else:
                result_a+=(a-1)//temp
                result_b+=b//temp
    print(f"Case #{k+1}: {result_b-result_a}")