def solution(elements):
    result={}
    dp=elements.copy()
    l=len(elements)
    for i in elements:
        result[i]=0
    for r in range(1,l):
        for i in range(l):
            dp[i]+=elements[(i+r)%l]
            result[dp[i]]=0
    answer = len(result)
    return answer