import sys
input=sys.stdin.readline

n,r,c=map(int,input().split())

def find(n,r,c):
    if n==2:
        return r*2+c
    semi=n//2
    if r<semi and c<semi:
        return find(semi,r,c)
    elif r<semi and c>=semi:
        return semi**2+find(semi,r,c-semi)
    elif r>=semi and c<semi:
        return (semi**2)*2+find(semi,r-semi,c)
    else:
        return (semi**2)*3+find(semi,r-semi,c-semi)

print(find(2**n,r,c))