import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(y, x):
    graph[y][x] = 0
    stack = [(y, x)]
    area = 1

    while stack:
        sy, sx = stack.pop()
        
        for k in range(4):
            ny, nx = sy + dy[k], sx + dx[k]
            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 1:
                stack.append((ny, nx))
                graph[ny][nx] = 0
                area += 1
    return area

cnt, max_area = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            cnt += 1
            max_area = max(dfs(i, j), max_area)

print(cnt)
print(max_area)

# pic = []
# for i in range(n):
#     row = list(map(int, input().split()))
#     for j in range(m):
#         if row[j]:
#             pic.append((i, j))

# pic = set(pic)
# cnt = 0
# areas = [0]
# while pic:
#     sx, sy = pic.pop()
#     stack = [(sx, sy)]
#     cnt += 1

#     area = 0
#     while stack:
#         sx, sy = stack.pop()
#         area += 1

#         for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#             nx, ny = sx + dx, sy + dy
#             if (nx, ny) in pic:
#                 pic.remove((nx, ny))
#                 stack.append((nx, ny))
#     areas.append(area)
    
# print(cnt)
# print(max(areas))