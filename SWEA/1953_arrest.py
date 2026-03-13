from collections import deque

# 해당 타입 구조물을 타고 이동할 수 있는 델타 값
type_delta = {1: [(1, 0), (0, 1), (-1, 0), (0, -1)],
              2: [(1, 0), (-1, 0)],
              3: [(0, 1), (0, -1)],
              4: [(-1, 0), (0, 1)],
              5: [(1, 0), (0, 1)],
              6: [(1, 0), (0, -1)],
              7: [(-1, 0), (0, -1)]}

# 해당 델타 값과 연결되는 타입 값
connect = {(1, 0): [1, 2, 4, 7],
           (0, 1): [1, 3, 6, 7],
           (-1, 0): [1, 2, 5, 6],
           (0, -1): [1, 3, 4, 5]}


for tc in range(1, int(input())+1):
    n, m, r, c, l = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(n)]
    dist = [[0] * m for _ in range(n)]
    queue = deque([(r, c)])
    dist[r][c] = 1
    cnt = 1
    while queue:
        x, y = queue.popleft()
        delta = type_delta[tunnel[x][y]]
        for dx, dy in delta:
            possible_type = connect[(dx, dy)]
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == 0:
                if tunnel[nx][ny] in possible_type:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
                    if dist[nx][ny] <= l:
                        cnt += 1
    print(f'#{tc}', cnt)