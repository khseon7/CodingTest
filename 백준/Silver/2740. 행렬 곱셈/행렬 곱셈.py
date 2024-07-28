n,m=map(int,input().split())
arr_1=[list(map(int,input().split())) for _ in range(n)]
m,k=map(int,input().split())
arr_2=[list(map(int,input().split())) for _ in range(m)]
res = [[0] * k for _ in range(n)]
for i in range(n):
  for j in range(k):
    for l in range(m):
      res[i][j] += arr_1[i][l] * arr_2[l][j]
    if j!=k-1:
      print(res[i][j],end=" ")
    else:
      print(res[i][j])