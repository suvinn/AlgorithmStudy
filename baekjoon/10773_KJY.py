K = int(input())
arr = []

for _ in range(K):
    arr.append(int(input()))

    stack = []

for i in range(K):
    if arr[i] != 0 :
        stack.append(arr[i])

    if arr[i] == 0 :
        stack.pop()

total = 0
if stack :
    for j in stack :
        total += j
    print(total)

else :
    print(0)