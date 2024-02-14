import sys
H,M=map(int, sys.stdin.readline().split())
time=H*60+M-45
if time<0:
  time+=1440
print(time//60, time%60)