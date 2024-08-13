import sys
s=sys.stdin.readline().rstrip()
stack=[]
for i in s:
  if i>='0' and i<='9':
    stack.append(int(i))
  elif i=='+':
    num_1=stack.pop()
    num_2=stack.pop()
    stack.append(num_1+num_2)
  elif i=='-':
    num_1=stack.pop()
    num_2=stack.pop()
    stack.append(num_2-num_1)
  elif i=='*':
    num_1=stack.pop()
    num_2=stack.pop()
    stack.append(num_1*num_2)
  elif i=='/':
    num_1=stack.pop()
    num_2=stack.pop()
    stack.append(int(num_2/num_1))
print(stack.pop())