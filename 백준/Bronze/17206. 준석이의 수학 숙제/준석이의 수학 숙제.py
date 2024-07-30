n=int(input())
arr=[int(x) for x in input().split()]
for i in arr:
  num_3=i//3
  num_7=i//7
  num_21=i//21
  print(3*num_3*(num_3+1)//2+7*num_7*(num_7+1)//2-21*num_21*(num_21+1)//2)