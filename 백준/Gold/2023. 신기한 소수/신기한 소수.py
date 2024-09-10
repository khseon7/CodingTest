import sys
input=sys.stdin.readline

n=int(input())

start=[2,3,5,7]
back=[1,3,7,9]

def is_prime(n):
    if n==1: return False
    for i in range(2,int(n**0.5)+1):
        if not n%i:
            return False
    return True

def dfs(depth):
    if depth==n:
        print("".join(map(str,result)))
        return
    for i in back:
        result.append(i)
        if is_prime(int("".join(map(str,result)))):
            dfs(depth+1)
        result.pop()

for i in start:
    result=[i]
    dfs(1)