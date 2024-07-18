s=list(input())
t=list(input())
while(len(s)<len(t)):
  if(t[-1]=='A'):
    t.pop()
    # print(f"'A' : {t}")
  elif(t[-1]=='B'):
    t.pop()
    t.reverse()
    # print(f"'B' : {t}")
if(s==t):
  print(1)
else:
  print(0)