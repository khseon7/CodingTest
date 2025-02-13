import sys

input = sys.stdin.readline

# 1m^2당 참외 개수 입력
K = int(input())

# 방향과 길이 정보 저장
directions = []
lengths = []

for _ in range(6):
    d, l = map(int, input().split())
    directions.append(d)
    lengths.append(l)

# 가장 긴 가로, 세로 찾기
max_width = 0
max_height = 0
max_w_index = 0
max_h_index = 0

for i in range(6):
    if directions[i] in [1, 2] and lengths[i] > max_width:  # 동(1) or 서(2)
        max_width = lengths[i]
        max_w_index = i
    if directions[i] in [3, 4] and lengths[i] > max_height:  # 남(3) or 북(4)
        max_height = lengths[i]
        max_h_index = i

# 작은 직사각형의 가로, 세로 찾기 (큰 직사각형 기준으로 좌우/상하로 둘러싸인 내부)
small_width = abs(lengths[(max_w_index - 1) % 6] - lengths[(max_w_index + 1) % 6])
small_height = abs(lengths[(max_h_index - 1) % 6] - lengths[(max_h_index + 1) % 6])

# 전체 참외밭 면적 = 큰 직사각형 - 작은 직사각형
total_area = (max_width * max_height) - (small_width * small_height)

# 참외 개수 계산
result = K * total_area

print(result)
