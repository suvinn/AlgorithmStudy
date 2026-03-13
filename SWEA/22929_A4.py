import heapq

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cost = [[float('inf')] * n for _ in range(n)]
    pq = [(0, 0, 0)]
    cost[0][0] = 0
    while pq:
        c, x, y = heapq.heappop(pq)
        if cost[x][y] < c:
            continue
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == arr[x][y]:
                    nc = 1
                elif arr[nx][ny] > arr[x][y]:
                    nc = 2 * (arr[nx][ny] - arr[x][y])
                else:
                    nc = 0
                if cost[nx][ny] > cost[x][y] + nc:
                    cost[nx][ny] = cost[x][y] + nc
                    heapq.heappush(pq, (cost[nx][ny], nx, ny))
    print(f'#{tc}', cost[n-1][n-1])