import sys
word=list(input())
count=0
if len(word)%2==1:
  for i in range(len(word)//2):
    if word[i]==word[-i-1]:
      count+=1
    else:
      print(0)
      break
else:
  for i in range(len(word)//2):
    if word[i]==word[-i-1]:
      count+=1
    else:
      print(0)
      break
if count==len(word)//2:
  print(1)