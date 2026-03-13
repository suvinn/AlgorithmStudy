from collections import deque

n, k = map(int, input().split())
d = [-1] * 100001
c = [0] * 100001

queue = deque([n])
d[n], c[n] = 0, 1
while queue:
    size = len(queue)
    for _ in range(size):
        x = queue.popleft()
        for nx in [x-1, x+1, 2*x]:
            if 0 > nx or nx > 100000:
                continue
            if d[nx] == -1:
                d[nx] = d[x] + 1
                c[nx] = c[x]
                queue.append(nx)
            elif d[nx] == d[x] + 1:
                c[nx] += c[x]
    if d[k] != -1:
        break

print(d[k])
print(c[k])