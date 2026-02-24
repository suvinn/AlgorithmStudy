import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(m)]

blue, white = 0, 0
def dfs(x, y):
    global blue, white
    stack = [(x, y)]
    color = arr[x][y]
    if not color:
        return
    cnt = 1
    arr[x][y] = 0
    while stack:
        x, y = stack.pop()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == color:
                cnt += 1
                arr[nx][ny] = 0
                stack.append((nx, ny))
    if color == 'B':
        blue += cnt ** 2
    else:
        white += cnt ** 2

for i in range(m):
    for j in range(n):
        dfs(i, j)

print(white, blue)