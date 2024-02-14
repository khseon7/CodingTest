import sys
arr=list(sys.stdin.readline())
length=10
for i in range(len(arr)-2):
  if arr[i]==arr[i+1]:
    length+=5
  else:
    length+=10
print(length)