import sys
input=sys.stdin.readline
size=10003001
arr=[1]*(size+1)
res=[]
def palindrome(n):
    cnt=0
    int_to_srt=str(n)
    for i in range(len(int_to_srt)//2):
        if int_to_srt[i]==int_to_srt[-i-1]:
            cnt+=1
    if cnt==len(int_to_srt)//2:
        return True
    else:
        return False
for i in range(2,size+1):
    if arr[i]:
        if palindrome(i):
            res.append(i)
        for j in range(2*i,size+1,i):
            arr[j]=0
n=int(input())
for i in range(len(res)-1):
    if res[0]>=n:
        print(res[0])
        break
    elif res[i]<n and res[i+1]>=n:
        print(res[i+1])
        break