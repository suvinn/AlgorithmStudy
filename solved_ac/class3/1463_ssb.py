n = int(input())

dp = [0] * max([n+1, 4])
dp[1], dp[2], dp[3] = 0, 1, 1
for i in range(4, n+1):
    if i % 3 == 0 and i % 2 == 0:
        dp[i] = 1 + min(dp[i//3], dp[i//2], dp[i - 1])
    elif i % 3 == 0:
        dp[i] = 1 + min(dp[i//3], dp[i - 1])
    elif i % 2 == 0:
        dp[i] = 1 + min(dp[i//2], dp[i - 1])
    else:
        dp[i] = 1 + dp[i - 1]

print(dp[n])

"""
dp[1] = 0
dp[2] = 1
dp[3] = 1
dp[4] = 1 + dp[2] = 2
dp[5] = 1 + dp[4] = 3
dp[6] = 1 + dp[2] = 2
dp[7] = 1 + dp[6] = 3
dp[8] = 1 + dp[4] = 3
dp[9] = 1 + dp[3] = 2
dp[10] = 1 + dp[5] = 4 (x) / dp[10] = 1 + dp[9] = 3 (o)
"""