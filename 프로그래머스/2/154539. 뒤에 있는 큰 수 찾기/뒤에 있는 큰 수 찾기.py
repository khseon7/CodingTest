from collections import deque

def solution(numbers):
    arr=deque(numbers)
    res=[-1]*len(arr)
    answer,idx = [],0
    while arr:
        answer.append((arr.popleft(),idx))
        if not arr:
            break
        idx+=1
        while answer and answer[-1][0]<arr[0]:
            val,loc=answer.pop()
            res[loc]=arr[0]
    return res