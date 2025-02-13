import sys

input = sys.stdin.readline

K = int(input())

directions = []
lengths = []

for _ in range(6):
    d, l = map(int, input().split())
    directions.append(d)
    lengths.append(l)

max_width = 0
max_height = 0
max_w_index = 0
max_h_index = 0

for i in range(6):
    if directions[i] in [1, 2] and lengths[i] > max_width:
        max_width = lengths[i]
        max_w_index = i
    if directions[i] in [3, 4] and lengths[i] > max_height:
        max_height = lengths[i]
        max_h_index = i

small_width = abs(lengths[(max_w_index - 1) % 6] - lengths[(max_w_index + 1) % 6])
small_height = abs(lengths[(max_h_index - 1) % 6] - lengths[(max_h_index + 1) % 6])

total_area = (max_width * max_height) - (small_width * small_height)

result = K * total_area

print(result)
