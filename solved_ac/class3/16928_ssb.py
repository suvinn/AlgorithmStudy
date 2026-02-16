import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
# ladder = [list(map(int, input().split())) for _ in range(n)]
# snake = [list(map(int, input().split())) for _ in range(m)]
data = [0] * 101
for _ in range(n+m):
    i, j = map(int, input().split())
    data[i] = j

dist = [-1] * 101
dist[1] = 0
queue = deque([1])
while queue:
    x = queue.popleft()
    for k in range(1, 7):
        nx = x + k
        if nx <= 100:
            # 사다리나 뱀이 있을 때
            if data[nx] and dist[data[nx]] == -1:
                dist[data[nx]] = dist[x] + 1
                queue.append(data[nx])
            # 사다리나 뱀이 없을 때
            elif not data[nx] and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                queue.append(nx)
    if dist[100] != -1:
        break

print(dist[100])