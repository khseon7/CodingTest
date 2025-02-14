def solution(sequence, k):
    left, right = 0, 0
    total = 0
    answer = []
    min_length = float('inf')

    while right < len(sequence):
        total += sequence[right]

        while total > k and left <= right:
            total -= sequence[left]
            left += 1

        if total == k:
            if right - left + 1 < min_length:
                min_length = right - left + 1
                answer = [left, right]

        right += 1

    return answer
