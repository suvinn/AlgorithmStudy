import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            start = (i, j)
            graph[i][j] = 'X'

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

cnt = 0
stack = [start]
while stack:
    x, y = stack.pop()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 'X':
            if graph[nx][ny] == 'P':
                cnt += 1
            graph[nx][ny] = 'X'
            stack.append((nx, ny))

print(cnt if cnt else 'TT')