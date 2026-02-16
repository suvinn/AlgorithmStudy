dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for tc in range(1, int(input())+1):
    n = int(input())
    grid = [[0] * 10 for _ in range(10)]
    for _ in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                grid[r][c] += color
                if grid[r][c] == 3:
                    grid[r][c] = 0
    ans = 0
    for i in range(10):
        for j in range(10):
            if grid[i][j] != 0:
                cnt = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < 10 and 0 <= ny < 10 and grid[nx][ny] == grid[i][j]:
                        cnt += 1
                ans += (4 - cnt)
    print(f'#{tc}', ans)