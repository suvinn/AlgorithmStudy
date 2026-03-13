from collections import deque

n, k = map(int, input().split())
d = [-1] * 100001

queue = deque([n])
d[n] = 0
while queue:
    x = queue.popleft()
    for dx in [-1, 1, x]:
        nx = x + dx
        if 0 <= nx <= 100000 and d[nx] == -1:
            d[nx] = d[x] + 1
            queue.append(nx)
    if d[k] != -1:
        print(d[k])
        break