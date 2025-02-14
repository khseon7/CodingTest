def solution(board, h, w):    
    n=len(board)
    h,w=int(h),int(w)
    target=board[h][w]
    count=0
    
    if h>0 and target==board[h-1][w]:
        count+=1
    if h<n-1 and target==board[h+1][w]:
        count+=1
    if w>0 and target==board[h][w-1]:
        count+=1
    if w<n-1 and target==board[h][w+1]:
        count+=1
    return count