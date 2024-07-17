min,max=map(int,input().split())
len_arr=max-min+1
arr=[1]*len_arr
for i in range(2,int(max**(1/2))+1):
  for j in range((i**2-min%(i**2))%i**2,len_arr,i**2):
    arr[j]=0
print(arr.count(1))