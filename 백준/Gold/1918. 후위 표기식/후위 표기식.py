import sys
def prior(ch):
  if ch=='(' or ch==')':
    return 0
  elif ch=='*' or ch=='/':
    return 1
  elif ch=='+' or ch=='-':
    return 2
  else:
    return -1
infix_exp=sys.stdin.readline().rstrip()
stack=[]
postfix_exp=[]
for i in infix_exp:
  if prior(i)==-1:
    postfix_exp.append(i)
  elif i=='+' or i=='-' or i=='*' or i=='/':
    if len(stack)==0:
      stack.append(i)
    else:
      while stack and stack[-1]!='(' and prior(i)>=prior(stack[-1]):
        postfix_exp.append(stack.pop())
      stack.append(i)
  elif i=='(':
    stack.append(i)
  elif i==')':
    while stack and stack[-1]!='(':
      postfix_exp.append(stack.pop())
    stack.pop()
while stack:
  postfix_exp.append(stack.pop())
print("".join(postfix_exp))