import sys
x_val,y_val=0,0
x_list=[]
y_list=[]
for _ in range(3):
  x,y=map(int,sys.stdin.readline().split())
  x_list.append(x)
  y_list.append(y)
x_list.sort()
y_list.sort()
if x_list.count(x_list[0])<x_list.count(x_list[-1]):
  x_val=x_list[0]
else:
  x_val=x_list[-1]
if y_list.count(y_list[0])<y_list.count(y_list[-1]):
  y_val=y_list[0]
else:
  y_val=y_list[-1]
print(x_val, y_val)