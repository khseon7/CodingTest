n,m=map(int,input().split())
arr1={}
arr2={}
for i in range(n):
  name=input()
  arr1[i+1]=name
  arr2[name]=i+1
for _ in range(m):
  answer=input()
  if answer.isdigit():
    print(arr1[int(answer)])
  else:
    print(arr2[answer])