T = int(input())
for tc in range(1, T+1):
    n = int(input())
    carrot = list(map(int, input().split()))
    total = sum(carrot)
    left, right = 0, total
    val = []
    for i in range(n):
        left += carrot[i]
        right -= carrot[i]
        val.append((i+1, abs(left - right)))
    val.sort(key=lambda x: (x[1], x[0]))
    print(f'#{tc}', *val[0])