import sys
input=sys.stdin.readline

n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

def find_paper(array):
    mi,ze,on=0,0,0
    flat_arr=[x for row in array for x in row]
    if flat_arr.count(-1)==len(flat_arr):
        return 1,0,0
    if flat_arr.count(0)==len(flat_arr):
        return 0,1,0
    if flat_arr.count(1)==len(flat_arr):
        return 0,0,1
    semi_size=len(array)//3
    arr1=[array[i][:semi_size] for i in range(semi_size)]
    arr2=[array[i][semi_size:2*semi_size] for i in range(semi_size)]
    arr3=[array[i][2*semi_size:] for i in range(semi_size)]
    
    arr4=[array[i][:semi_size] for i in range(semi_size,2*semi_size)]
    arr5=[array[i][semi_size:2*semi_size] for i in range(semi_size,2*semi_size)]
    arr6=[array[i][2*semi_size:] for i in range(semi_size,2*semi_size)]
    
    arr7=[array[i][:semi_size] for i in range(2*semi_size,len(array))]
    arr8=[array[i][semi_size:2*semi_size] for i in range(2*semi_size,len(array))]
    arr9=[array[i][2*semi_size:] for i in range(2*semi_size,len(array))]
    
    m1,z1,o1=find_paper(arr1)
    m2,z2,o2=find_paper(arr2)
    m3,z3,o3=find_paper(arr3)
    m4,z4,o4=find_paper(arr4)
    m5,z5,o5=find_paper(arr5)
    m6,z6,o6=find_paper(arr6)
    m7,z7,o7=find_paper(arr7)
    m8,z8,o8=find_paper(arr8)
    m9,z9,o9=find_paper(arr9)
    
    mi,ze,on=m1+m2+m3+m4+m5+m6+m7+m8+m9,z1+z2+z3+z4+z5+z6+z7+z8+z9,o1+o2+o3+o4+o5+o6+o7+o8+o9
    return mi,ze,on

res_m,res_z,res_o=find_paper(arr)
print(res_m)
print(res_z)
print(res_o)