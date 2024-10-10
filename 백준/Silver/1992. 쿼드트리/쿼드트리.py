import sys
input=sys.stdin.readline

n=int(input())
arr=[list(input().strip()) for _ in range(n)]

def find_paper(array):
    res_str=''
    flat_arr=[x for row in array for x in row]
    if flat_arr.count('1')==len(flat_arr):
        return '1'
    if flat_arr.count('0')==len(flat_arr):
        return '0'
    semi_size=len(array)//2
    arr1=[array[i][:semi_size] for i in range(semi_size)]
    arr2=[array[i][semi_size:] for i in range(semi_size)]
    arr3=[array[i][:semi_size] for i in range(semi_size,len(array))]
    arr4=[array[i][semi_size:] for i in range(semi_size,len(array))]

    string='('+find_paper(arr1)+find_paper(arr2)+find_paper(arr3)+find_paper(arr4)+')'
    return res_str+string

print(find_paper(arr))