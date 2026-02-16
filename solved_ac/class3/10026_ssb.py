import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
pic = [list(input().strip()) for _ in range(n)]
pic2 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if pic[i][j] == 'G':
            pic2[i][j] = 'R'
        else:
            pic2[i][j] = pic[i][j]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

queue1 = deque()
cnt1 = 0
def bfs1(x, y):
    global cnt1
    if pic[x][y]:
        color = pic[x][y]
        queue1.append((x, y))
        cnt1 += 1
    while queue1:
        x, y = queue1.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and pic[nx][ny] == color:
                queue1.append((nx, ny))
                pic[nx][ny] = 0

queue2 = deque()
cnt2 = 0
def bfs2(x, y):
    global cnt2
    if pic2[x][y]:
        color = pic2[x][y]
        queue2.append((x, y))
        cnt2 += 1
    while queue2:
        x, y = queue2.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and pic2[nx][ny] == color:
                    queue2.append((nx, ny))
                    pic2[nx][ny] = 0

for i in range(n):
    for j in range(n):
        bfs1(i, j)
        bfs2(i, j)
print(cnt1, cnt2)