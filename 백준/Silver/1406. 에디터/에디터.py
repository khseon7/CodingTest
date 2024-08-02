import sys

left_stack = list(sys.stdin.readline().rstrip())
right_stack = []
m = int(sys.stdin.readline())

for _ in range(m):
    command = sys.stdin.readline().split()
    if command[0] == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())
    elif command[0] == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
    elif command[0] == 'B':
        if left_stack:
            left_stack.pop()
    elif command[0] == 'P':
        left_stack.append(command[1])
      
result = ''.join(left_stack) + ''.join(reversed(right_stack))
print(result)