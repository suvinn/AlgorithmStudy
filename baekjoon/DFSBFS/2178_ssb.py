import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

graph[0][0] = 1
queue = deque([(0, 0)])
while queue:
    sy, sx = queue.popleft()
    for k in range(4):
        ny, nx = sy + dy[k], sx + dx[k]
        if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == '1':
            graph[ny][nx] = graph[sy][sx] + 1
            queue.append((ny, nx))

print(graph[n-1][m-1])