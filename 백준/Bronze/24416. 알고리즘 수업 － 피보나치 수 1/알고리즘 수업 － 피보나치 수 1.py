n=int(input())
count=0
def fibonacci(n):
    global count
    fibo=[1,1]+[0]*38
    for i in range(2,n):
        fibo[i]=fibo[i-1]+fibo[i-2]
        count+=1
    return fibo[n-1]
print(fibonacci(n),count)