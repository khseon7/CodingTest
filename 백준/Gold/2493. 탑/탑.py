import sys
input=sys.stdin.readline
n=map(int,input().split())
tower=list(map(int,input().split()))
tower_poss=[(tower[i],i+1) for i in range(len(tower))]
stack=[]
signal_stack=[0]*len(tower)
while tower_poss:
    while stack and tower_poss[-1][0]>stack[-1][0]:
        signal_stack[stack[-1][1]-1]=tower_poss[-1][1]
        stack.pop()
    stack.append(tower_poss.pop())
print(" ".join(map(str,signal_stack)))