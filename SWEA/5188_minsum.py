for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = arr[0][0]
    for k in range(1, n):
        dp[0][k] = arr[0][k] + dp[0][k-1]
        dp[k][0] = arr[k][0] + dp[k-1][0]
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = arr[i][j] + min(dp[i-1][j], dp[i][j-1])
    print(f'#{tc}', dp[n-1][n-1])