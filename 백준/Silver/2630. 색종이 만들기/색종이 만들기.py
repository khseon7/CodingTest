import sys
input=sys.stdin.readline

n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

def find_paper(array):
    white,blue=0,0
    flat_arr=[x for row in array for x in row]
    if flat_arr.count(1)==len(flat_arr):
        return 0,1
    if flat_arr.count(0)==len(flat_arr):
        return 1,0
    semi_size=len(array)//2
    arr1=[array[i][:semi_size] for i in range(semi_size)]
    arr2=[array[i][:semi_size] for i in range(semi_size,len(array))]
    arr3=[array[i][semi_size:] for i in range(semi_size)]
    arr4=[array[i][semi_size:] for i in range(semi_size,len(array))]
    w1,b1=find_paper(arr1)
    w2,b2=find_paper(arr2)
    w3,b3=find_paper(arr3)
    w4,b4=find_paper(arr4)
    white,blue=w1+w2+w3+w4,b1+b2+b3+b4
    return white, blue

res_w,res_b=find_paper(arr)
print(res_w)
print(res_b)