n = int(input())
arr = [list(input()) for _ in range(n)]

new_arr = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            new_arr[i][j] = 'R'
        else:
            new_arr[i][j] = arr[i][j]

visited1 = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]
def dfs(x, y, grid, visited):
    stack = [(x, y)]
    color = grid[x][y]
    if visited[x][y]:
        return 0
    visited[x][y] = True
    while stack:
        x, y = stack.pop()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == color:
                visited[nx][ny] = True
                stack.append((nx, ny))
    return 1

normal, abnormal = 0, 0
for i in range(n):
    for j in range(n):
        normal += dfs(i, j, arr, visited1)
        abnormal += dfs(i, j, new_arr, visited2)

print(normal, abnormal)