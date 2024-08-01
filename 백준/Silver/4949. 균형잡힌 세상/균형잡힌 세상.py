import sys
while 1:
  x=sys.stdin.readline().rstrip()
  if x=='.':
    break
  else:
    arr=[]
    flag=1
    for i in x:
      if i=='(' or i=='[':
        arr.append(i)
      elif i==')':
        if not arr or arr[-1]!='(':
          flag=0
          break
        else:
          arr.pop()
      elif i==']':
        if not arr or arr[-1]!='[':
          flag=0
          break
        else:
          arr.pop()
    if flag==1 and len(arr)==0:
      print('yes')
    else:
      print('no')