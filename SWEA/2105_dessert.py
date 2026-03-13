di = [1, 1]
dj = [1, -1]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def count(x, y, dir, is_start):
    if is_start:
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if dessert[nx][ny] in adj:
                return False
            adj.add(dessert[nx][ny])
        return True
    if dir == 0:
        for di, dj in [(1, 0), (0, 1)]:
            nx, ny = x + di, y + dj
            if dessert[nx][ny] in adj:
                return False
            adj.add(dessert[nx][ny])
        return True
    else:
        for di, dj in [(1, 0), (0, -1)]:
            nx, ny = x + di, y + dj
            if dessert[nx][ny] in adj:
                return False
            adj.add(dessert[nx][ny])
        return True


for tc in range(1, int(input())+1):
    n = int(input())
    dessert = [list(map(int, input().split())) for _ in range(n)]
    visited = set()
    max_cnt = -1
    for i in range(1, n-1):
        for j in range(1, n-1):
            for k in range(2):
                curr = [(i, j)]
                adj = set()
                if not count(i, j, k, True):
                    break
                max_cnt = max(len(adj), max_cnt)

                d = 1
                while True:
                    ni, nj = i + di[k] * d, j + dj[k] * d
                    if 1 <= ni < n-1 and 1 <= nj < n-1:
                        if not count(ni, nj, k, False):
                            break
                        # curr.append((ni, nj))
                        # if tuple(curr) in visited:
                        #     break
                        # visited.add(tuple(curr))
                        max_cnt = max(len(adj), max_cnt)
                        d += 1
                    else:
                        break
    print(f'#{tc}', max_cnt)