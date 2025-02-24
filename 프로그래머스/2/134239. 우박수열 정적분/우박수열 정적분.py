def solution(k, ranges):
    answer=[]
    prod=[k]
    while k!=1:
        if k%2==0:
            k//=2
        else:
            k=3*k+1
        prod.append(k)
    
    n=len(prod)-1
    area=[]
    for i in range(n):
        area.append((prod[i]+prod[i+1])/2)

    for a,b in ranges:
        b+=n
        if a>b or b<0 or a>n:
            answer.append(float(-1.0))
        elif a==b:
            answer.append(0.0)
        else:
            answer.append(sum(area[a:b]))
    return answer