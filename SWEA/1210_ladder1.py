# 역방향
for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    for j in range(100):
        if ladder[99][j] == 2:
            i = 99
            while i > 0:
                if 0 <= j+1 < 100 and ladder[i][j+1] == 1:
                    while 0 <= j+1 < 100 and ladder[i][j+1] == 1:
                        j += 1
                elif 0 <= j-1 < 100 and ladder[i][j-1] == 1:
                    while 0 <= j-1 < 100 and ladder[i][j-1] == 1:
                        j -= 1
                i -= 1
            break
    print(f'#{tc}', j)


# 정방향
for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    for j in range(100):
        if ladder[0][j] == 1:
            x, y = 1, j
            while x < 100:
                if 0 <= y+1 < 100 and ladder[x][y+1] == 1:
                    while 0 <= y+1 < 100 and ladder[x][y+1] == 1:
                        y = y+1
                elif 0 <= y-1 < 100 and ladder[x][y-1] == 1:
                    while 0 <= y-1 < 100 and ladder[x][y-1] == 1:
                        y = y-1
                x += 1
            if ladder[99][y] == 2:
                break
    print(f'#{tc}', j)