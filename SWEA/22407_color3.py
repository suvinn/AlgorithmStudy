for tc in range(1, int(input())+1):
    r1, c1, r2, c2 = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    w = max(min(c2, y2) - max(c1, y1) + 1, 0)
    h = max(min(r2, x2) - max(r1, x1) + 1, 0)
    if w == 0 or h == 0:
        print(f'#{tc}', 0, 0)
    else:
        print(f'#{tc}', w, h)