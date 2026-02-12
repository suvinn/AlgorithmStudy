N = int(input())
strick = list(map(int,input().split()))

left = 0
arr = [0]*10
kind = 0
max_val = 0
for right in range(N):
    if arr[strick[right]] == 0 :
        kind += 1
    arr[strick[right]] += 1

    while kind > 2 :
        t = strick[left]

        arr[t] -= 1
        if arr[t] == 0 :
            kind -= 1
        
        left += 1
    
    length = right-left + 1
    if length > max_val :
        max_val = length

    
print(max_val) 