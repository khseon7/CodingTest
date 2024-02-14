import sys
n=int(sys.stdin.readline())
arr=list()
Q1,Q2,Q3,Q4,AXIS=0,0,0,0,0
for _ in range(n):
  x,y=map(int,sys.stdin.readline().split())
  arr.append(x)
  arr.append(y)
for i in range(0,len(arr),2):
  if arr[i]==0 or arr[i+1]==0:
    AXIS+=1
  elif arr[i]>0 and arr[i+1]>0:
    Q1+=1
  elif arr[i]<0 and arr[i+1]>0:
    Q2+=1
  elif arr[i]<0 and arr[i+1]<0:
    Q3+=1
  elif arr[i]>0 and arr[i+1]<0:
    Q4+=1
print("Q1:",Q1)
print("Q2:",Q2)
print("Q3:",Q3)
print("Q4:",Q4)
print("AXIS:",AXIS)