def find(a,n,m):
    global num, result
    if a==n:
        if not num:
            return
        temp=1
        for i in num:
            temp*=i
        if len(num)%2:
            result+=m//temp
            return
        else:
            result-=m//temp
            return
    num.append(x[a])
    find(a+1,n,m)
    num.pop()
    find(a+1,n,m)

import sys
input=sys.stdin.readline
n,m=map(int,input().split())
x=list(map(int,input().split()))
num=[]
result=0
find(0,n,m)
print(result)