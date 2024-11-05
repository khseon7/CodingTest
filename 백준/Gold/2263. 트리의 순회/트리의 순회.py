import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
in_arr = list(map(int, input().split()))
post_arr = list(map(int, input().split()))

index_map = {value: i for i, value in enumerate(in_arr)}

def to_pre_by_index(start, end, post_start, post_end):
    if start > end:
        return
    if start == end:
        print(post_arr[post_end], end=" ")
        return

    root = post_arr[post_end]
    print(root, end=" ")

    idx = index_map[root]
    left_size = idx - start

    to_pre_by_index(start, idx - 1, post_start, post_start + left_size - 1)
    to_pre_by_index(idx + 1, end, post_start + left_size, post_end - 1)

to_pre_by_index(0, n - 1, 0, n - 1)
