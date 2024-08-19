from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

# 인덱스와 값의 쌍을 저장하는 deque 생성
dq = deque((arr[i], i + 1) for i in range(n))
result = []

while len(dq) > 1:
    # 현재 위치에서 pop하고 결과에 추가
    index, pos = dq.popleft()
    result.append(pos)

    # 남은 요소들이 있을 때만 회전
    if index > 0:
        dq.rotate(-(index - 1))  # 시계 방향으로 이동
    else:
        dq.rotate(-index)  # 반시계 방향으로 이동

# 마지막 남은 요소의 위치 추가
result.append(dq[0][1])

# 결과 출력
print(' '.join(map(str, result)))
