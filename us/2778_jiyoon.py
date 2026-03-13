for _ in range(int(input())):
    arr = [list(map(int, input().split())) for _ in range(3)]
    arr += [arr[0]]
    points = []
    flag = False
    for i in range(3):
        A, B, C = (arr[i][0], arr[i+1][0]), (arr[i][1], arr[i+1][1]), (arr[i][2], arr[i+1][2])
        rA, rB = (arr[i+1][0], -arr[i][0]), (arr[i+1][1], -arr[i][1])
        cy = sum(i * j for i, j in zip(C, rA))
        py = sum(i * j for i, j in zip(B, rA))
        cx = sum(i * j for i, j in zip(C, rB))
        px = sum(i * j for i, j in zip(A, rB))
        if py == 0 or px == 0:
            print(f"{0:.4f}")
            flag = True
            break
        points.append((cy/py, cx/px))
    if flag:
        continue
    points.append(points[0])
    right, left = 0, 0
    for i in range(3):
        right += points[i][0] * points[i+1][1]
        left += points[i+1][0] * points[i][1]
    ans = abs(right-left) * .5
    print(f"{ans:.4f}")