import sys
n=int(sys.stdin.readline())
input_list=list(sys.stdin.readline().rstrip())
pre_skill={'L':0,'S':0}
cnt=0
for i in input_list:
  if i=='L':
    pre_skill['L']+=1
  elif i=='S':
    pre_skill['S']+=1
  elif i=='R':
    if pre_skill['L']>0:
      pre_skill['L']-=1
      cnt+=1
    else:
      break
  elif i=='K':
    if pre_skill['S']>0:
      pre_skill['S']-=1
      cnt+=1
    else:
      break
  elif i>='1' and i<='9':
    cnt+=1
print(cnt)