n = int(input())
arr = [0]*10
max_value = 0
while n:
    res = n%10
    arr[res] += 1
    if res != 6 and res != 9:
        max_value = max(max_value, arr[res])
    else:
        max_value = max(max_value, (arr[6]+arr[9]+1)//2)
    n //= 10
print(max_value)