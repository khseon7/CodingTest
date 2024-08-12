import sys
n=int(input())
arr=[0]*10000
front=rear=-1
for _ in range(n):
  param=sys.stdin.readline().split()
  if param[0]=="push":
    rear+=1
    arr[rear]=int(param[1])
  elif param[0]=="pop":
    if front==rear:
      print(-1)
    else:
      front+=1
      print(arr[front])
  elif param[0]=='empty':
    if front==rear:
      print(1)
    else:
      print(0)
  elif param[0]=='size':
    print(rear-front)
  elif param[0]=='front':
    if front==rear:
      print(-1)
    else:
      print(arr[front+1])
  elif param[0]=='back':
    if front==rear:
      print(-1)
    else:
      print(arr[rear])