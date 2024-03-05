import sys
def GCD(A,B):
  if B%A==0:
      return A
  else:
    return GCD(B%A,A)
def LCM(A,B):
  return A*B//GCD(A,B)
nu1,de1=map(int,sys.stdin.readline().split())
nu2,de2=map(int,sys.stdin.readline().split())
nu=nu1*de2+nu2*de1
de=de1*de2
gcd=GCD(nu,de)
print(nu//gcd,de//gcd)