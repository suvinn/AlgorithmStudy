import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, list(input().strip()))) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

cnt = 0
queue = deque()
def bfs(x, y):
    global cnt, homes
    home = 0
    if arr[x][y]:
        cnt += 1
        queue.append((x, y))
        arr[x][y] = 0
        home += 1
    while queue:
        sx, sy = queue.popleft()
        for k in range(4):
            nx, ny = sx + dx[k], sy + dy[k]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny]:
                home += 1
                arr[nx][ny] = 0
                queue.append((nx, ny))
    if home:
        homes.append(home)

homes = []
for i in range(n):
    for j in range(n):
        bfs(i, j)
homes.sort()

print(cnt)
for home in homes:
    print(home)