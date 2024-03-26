import sys
n=int(sys.stdin.readline()) # 기술 개수
input_list=list(sys.stdin.readline().rstrip()) # 기술 받아서 리스트로 받기
pre_skill={'L':0,'S':0,'R':0,'K':0} # 사전 기술 및 본 기술 딕셔너리
cnt=0 # 기술 시전 횟수
for i in input_list:
  if i=='L': # 사전 기술 L이 들어오면 한번 카운트해서 저장
    pre_skill['L']+=1
  elif i=='S': # 사전 기술 S가 들어오면 한번 카운트해서 저장
    pre_skill['S']+=1
  elif i=='R': # 본 기술 R이 들어오면
    if pre_skill['L']>0: # 사전 기술 L이 카운트되어 있다면 하나 줄이고, 본 기술 R을 하나 카운트해서 저장
      pre_skill['L']-=1
      pre_skill['R']+=1
    else: # 사전 기술이 없다면 스크립트가 꼬여 후에 기술이 정상적으로 발동되지 않아 끝냄
      break
  elif i=='K': # 본 기술 K이 들어오면
    if pre_skill['S']>0: # 사전 기술 S가 카운트되어 있다면 하나 줄이고, 본 기술 K를 하나 카운트해서 저장
      pre_skill['S']-=1
      pre_skill['K']+=1
    else: # 사전 기술이 없다면 스크립트가 꼬여 후에 기술이 저상적으로 발동되지 않아 끝냄
      break
  elif i>='1' and i<='9': # 1~9에 해당하는 문자는 바로 발동하는 숫자이므로 cnt를 하나 카운트하여 저장
    cnt+=1
print(cnt+pre_skill['R']+pre_skill['K']) # 바로 발동한 기술의 수 cnt에 사전 준비가 필요한 기술 R과 K의 카운트 값을 더해서 출력import sys
n=int(sys.stdin.readline()) # 기술 개수
input_list=list(sys.stdin.readline().rstrip()) # 기술 받아서 리스트로 받기
pre_skill={'L':0,'S':0,'R':0,'K':0} # 사전 기술 및 본 기술 딕셔너리
cnt=0 # 기술 시전 횟수
for i in input_list:
  if i=='L': # 사전 기술 L이 들어오면 한번 카운트해서 저장
    pre_skill['L']+=1
  elif i=='S': # 사전 기술 S가 들어오면 한번 카운트해서 저장
    pre_skill['S']+=1
  elif i=='R': # 본 기술 R이 들어오면
    if pre_skill['L']>0: # 사전 기술 L이 카운트되어 있다면 하나 줄이고, 본 기술 R을 하나 카운트해서 저장
      pre_skill['L']-=1
      pre_skill['R']+=1
    else: # 사전 기술이 없다면 스크립트가 꼬여 후에 기술이 정상적으로 발동되지 않아 끝냄
      break
  elif i=='K': # 본 기술 K이 들어오면
    if pre_skill['S']>0: # 사전 기술 S가 카운트되어 있다면 하나 줄이고, 본 기술 K를 하나 카운트해서 저장
      pre_skill['S']-=1
      pre_skill['K']+=1
    else: # 사전 기술이 없다면 스크립트가 꼬여 후에 기술이 저상적으로 발동되지 않아 끝냄
      break
  elif i>='1' and i<='9': # 1~9에 해당하는 문자는 바로 발동하는 숫자이므로 cnt를 하나 카운트하여 저장
    cnt+=1
print(cnt+pre_skill['R']+pre_skill['K']) # 바로 발동한 기술의 수 cnt에 사전 준비가 필요한 기술 R과 K의 카운트 값을 더해서 출력
