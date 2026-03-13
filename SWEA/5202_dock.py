for tc in range(1, int(input())+1):
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda x: (x[1]-x[0], x[0]))
    dp = [0] * 25
    start, cnt = 0, 0
    for i in range(n):
        s, e = arr[i]
        if sum(dp[s:e]) == 0:
            for time in range(s, e):
                dp[time] = 1
            cnt += 1
    print(f'#{tc}', cnt)