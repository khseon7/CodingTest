import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    n=int(input())
    pre_arr=list(map(int,input().split()))
    in_arr=list(map(int,input().split()))
    
    idx_in={value:i for i,value in enumerate(in_arr)}
    
    res=[]
    
    def to_post(start, end, in_start, in_end):
        if start>end:
            return
        if start==end:
            res.append(pre_arr[start])
            return
        root=pre_arr[start]
        res.append(root)
        idx=idx_in[root]
        left_size=idx-in_start
        
        to_post(start+left_size+1,end,idx+1,in_end)
        to_post(start+1,start+left_size,in_start,idx-1)
    
    to_post(0,n-1,0,n-1)
    print(" ".join(map(str,res[::-1])))