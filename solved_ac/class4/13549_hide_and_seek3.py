from collections import deque

n, k = map(int, input().split())
d = [-1] * 100001

queue = deque([n])
d[n] = 0
while queue:
    x = queue.popleft()
    if 0 <= 2*x <= 100000 and d[2*x] == -1:
        d[2*x] = d[x]
        queue.append(2*x)
    for nx in [x-1, x+1]:
        if 0 <= nx <= 100000 and d[nx] == -1:
            d[nx] = d[x] + 1
            queue.append(nx)
    if d[k] != -1:
        print(d[k])
        break