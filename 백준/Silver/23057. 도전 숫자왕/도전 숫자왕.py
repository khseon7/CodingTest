from itertools import combinations
import sys
input=sys.stdin.readline
n=int(input())
card=list(map(int,input().split()))
res=set()
for i in range(1,n+1):
    for j in combinations(card,i):
        res.add(sum(j))
print(sum(card)-len(res))