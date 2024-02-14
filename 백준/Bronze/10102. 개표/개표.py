import sys
from collections import Counter
N=int(sys.stdin.readline())
arr=list(sys.stdin.readline())
A=arr.count('A')
B=arr.count('B')
if A>B:
  print('A')
elif A==B:
  print('Tie')
elif A<B:
  print('B')