import sys
heap = [0]  # dummy node to make heap 1-indexed
res = []
n = int(sys.stdin.readline())

for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap) == 1:
            res.append("0")
        else:
            # Extract max
            res.append(str(heap[1]))
            heap[1] = heap[-1]
            heap.pop()
            
            # Heapify down
            i = 1
            while True:
                left = 2 * i
                right = 2 * i + 1
                largest = i
                
                if left < len(heap) and heap[left] > heap[largest]:
                    largest = left
                if right < len(heap) and heap[right] > heap[largest]:
                    largest = right
                    
                if largest != i:
                    heap[i], heap[largest] = heap[largest], heap[i]
                    i = largest
                else:
                    break
    else:
        # Insert x
        heap.append(x)
        
        # Heapify up
        i = len(heap) - 1
        while i > 1 and heap[i] > heap[i // 2]:
            heap[i], heap[i // 2] = heap[i // 2], heap[i]
            i = i // 2

print("\n".join(res))
