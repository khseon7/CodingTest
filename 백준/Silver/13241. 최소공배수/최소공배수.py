import sys
def GCD(A,B):
  if B%A==0:
      return A
  else:
    return GCD(B%A,A)
def LCM(A,B):
  return A*B//GCD(A,B)
A,B=map(int,sys.stdin.readline().split())
print(LCM(A,B))