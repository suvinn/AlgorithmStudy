n, k = map(int, input().split())
arr = list(i+1 for i in range(n))
ans = []
idx = -1
while len(ans) < n:
    i = 0
    while i < k:
        idx = (idx + 1) % n
        if arr[idx]:
            i += 1
    ans.append(arr[idx])
    arr[idx] = 0
print('<' + ', '.join(map(str, ans)) + '>')