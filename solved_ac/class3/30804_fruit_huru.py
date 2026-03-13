n = int(input())
fruits = list(map(int, input().split()))
v = [0] * 10
left = 0
kind = 0
max_val = 0
for right in range(n):
    if not v[fruits[right]]:
        kind += 1
    v[fruits[right]] += 1

    while kind > 2:
        v[fruits[left]] -= 1
        if not v[fruits[left]]:
            kind -= 1
        
        left += 1
    
    length = right - left + 1
    if max_val < length:
        max_val = length

print(max_val)