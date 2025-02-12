import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# 초기 설정
idx, cnt = 0, 0

while idx < N - 1:
    if arr[idx] == 0:  # 현재 위치에서 이동 불가능하면 -1 출력
        print('-1')
        exit()

    if idx + arr[idx] >= N - 1:  # 마지막 위치 도달 가능하면 점프 후 종료
        cnt += 1
        break

    # 현재 위치에서 점프 가능한 범위 내에서 최적의 다음 위치 찾기
    best_idx = idx + 1  # 일단 다음 위치로 설정
    max_reach = best_idx + arr[best_idx]  # 해당 위치에서 갈 수 있는 최대 거리

    for i in range(idx + 1, min(idx + arr[idx] + 1, N)):  # 가능한 범위 탐색
        if i + arr[i] > max_reach:  # 더 멀리 갈 수 있다면 갱신
            max_reach = i + arr[i]
            best_idx = i

    # 최적의 위치로 이동
    idx = best_idx
    cnt += 1

print(cnt)
