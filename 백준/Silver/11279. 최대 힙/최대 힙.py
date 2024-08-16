import sys
heap=[]
heap.append(0)
res=[]
n=int(sys.stdin.readline())
for _ in range(n):
  x=int(sys.stdin.readline())
  if x==0:
    if len(heap)==1:
      res.append(str(0))
    else:
      heap[1],heap[-1]=heap[-1],heap[1]
      res.append(str(heap.pop()))
      i=1
      while True:
        left=2*i
        right=2*i+1
        value=i
        if left<len(heap) and heap[left]>heap[value]:
          value=left
        if right<len(heap) and heap[right]>heap[value]:
          value=right
        if value!=i:
          heap[i],heap[value]=heap[value],heap[i]
          i=value
        else:
          break
  elif x>0:
    heap.append(x)
    i=len(heap)-1
    while i!=1 and heap[i//2]<heap[i]:
      heap[i//2],heap[i]=heap[i],heap[i//2]
      i=i//2
print("\n".join(res))