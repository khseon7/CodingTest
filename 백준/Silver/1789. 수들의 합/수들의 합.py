# 1부터 차례대로 더하다가 입력받은 수 n을 넘었을 때 '마지막으로 더한 수-1' 값 출력
import sys
n=int(sys.stdin.readline()) # 입력받은 수
cnt=1 # 1부터 시작
sum=0 # 1부터의 합
while True:
  sum+=cnt # cnt 더해주고
  if sum>n: # 합이 n이상이면
    cnt-=1
    break # 멈추고
  elif sum==n:
    break
  else: # 합이 n보다 작으면
    cnt+=1 # cnt 하나 증가해서 다음 수로 넘어감
    continue # 다시 while문으로
print(cnt)