N = int(input())
stick = list(map(int,input().split()))
arr = [0]*10
left = 0
max_val = 0
kind = 0
for right in range(N):
    if arr[stick[right]] == 0 :
        kind += 1
    arr[stick[right]] += 1

    while kind > 2 :
        t = stick[left]

        arr[t] -= 1
        if arr[t] == 0 :
            kind -= 1
        
        left += 1
    
    length = right - left + 1
    if length > max_val :
        max_val = length
    
print(max_val)