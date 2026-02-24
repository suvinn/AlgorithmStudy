import sys
from collections import deque
input = sys.stdin.readline

# 나이트: 세로 2칸+가로 1칸 / 가로 2칸+세로 1칸
dx = [2, 2, 1, 1, -1, -1, -2, -2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

for _ in range(int(input())):
    l = int(input())
    arr = [[-1] * l for _ in range(l)]
    dist = []
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    x, y = start
    ex, ey = end
    queue = deque([start])
    arr[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < l and 0 <= ny < l and arr[nx][ny] == -1:
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx, ny))
        if arr[ex][ey] != -1:
            break
    print(arr[ex][ey])