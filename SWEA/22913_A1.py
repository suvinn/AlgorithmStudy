dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    apple = [0] * 11
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                apple[arr[i][j]] = (i, j)
    start = (0, 0)
    dir, rotate = 0, 0
    for i in range(1, 11):
        if not apple[i]:
            break
        end = apple[i]
        x, y = end[0] - start[0], end[1] - start[1]
        while True:
            if dir % 2 != 0 and x // dx[dir] > 0:
                x = 0
            elif dir % 2 == 0 and y // dy[dir] > 0:
                y = 0
            if x == 0 and y == 0:
                break
            dir = (dir + 1) % 4
            rotate += 1
        start = end
    print(f'#{tc}', rotate)