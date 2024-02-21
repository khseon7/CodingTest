import sys
sent_list=[]
def composite_num(n):
  sent=str(n)+" = 1"
  sum=1
  for i in range(2,n):
    if n%i==0:
      sent=sent+" + "+str(i)
      sum+=i
  if sum==n:
    return str(sent)
  else:
    return str(n)+" is NOT perfect."

while True:
  x=int(sys.stdin.readline())
  if x==-1: break
  else:
    sent_list.append(composite_num(x))

for i in sent_list:
  print(i)