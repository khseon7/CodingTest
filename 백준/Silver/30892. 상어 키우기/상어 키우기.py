import sys
n,k,t=map(int,sys.stdin.readline().split())
#n은 존재하는 상어 마릿수
#k는 샼이 먹을 수 있는 상어의 최대 마릿수
#t는 샼의 최초 크기
shark_list=sorted(map(int,sys.stdin.readline().split()))
for _ in range(k):
    # 앞바다에 있는 상어 중 가장 작은 상어의 크기가 샼보다 크거나 같을 때는 샼의 크기를 출력하고 종료
    if t<=shark_list[0]:
        break
    # 앞바다에 있는 상어 중 가장 작은 상어의 크기가 샼보다 작을 때
    else:
        cnt=-1
        while shark_list[cnt]>=t:
            cnt-=1
        shark=shark_list[cnt]
        t+=shark_list.pop(cnt)
print(t)