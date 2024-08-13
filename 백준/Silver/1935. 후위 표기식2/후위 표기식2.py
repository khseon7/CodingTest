import sys
n=int(input())
s=sys.stdin.readline().rstrip()
num_stack=[]
for _ in range(n):
  num_stack.append(int(sys.stdin.readline()))
stack=[]
for i in s:
  if i>='A' and i<='Z':
    index=ord(i)-ord('A')
    stack.append(num_stack[index])
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
    stack.append(num_2/num_1)
print("{0:.2f}".format(stack.pop()))