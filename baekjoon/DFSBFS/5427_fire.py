import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def escape(queue):
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < h and 0 <= ny < w and building[nx][ny] != '#':
                if building[nx][ny] == '.' or building[nx][ny] > abs(building[x][y]) + 1:
                    building[nx][ny] = building[x][y] - 1
                    queue.append((nx, ny))
            elif 0 > nx or nx >= h or 0 > ny or ny >=  w:
                return abs(building[x][y]) + 1
    return 'IMPOSSIBLE'

for _ in range(int(input())):
    w, h = map(int, input().split())
    building = [list(input()) for _ in range(h)]
    
    fires = deque()
    for i in range(h):
        for j in range(w):
            if building[i][j] == '@':
                start = (i, j)
                building[i][j] = 0
            elif building[i][j] == '*':
                fires.append((i, j))
                building[i][j] = 0
    
    while fires:
        x, y = fires.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < h and 0 <= ny < w and building[nx][ny] == '.':
                building[nx][ny] = building[x][y] + 1
                fires.append((nx, ny))

    queue = deque([start])
    ans = escape(queue)
    print(ans)