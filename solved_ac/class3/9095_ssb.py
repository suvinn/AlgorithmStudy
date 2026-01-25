import sys
input = sys.stdin.readline

t = int(input())
n_lst = list(int(input()) for _ in range(t))

dp = [0] * (max(n_lst)+1)
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, max(n_lst)+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for n in n_lst:
    print(dp[n])

"""
dp[1] = 1
dp[2] = 1+1 = 2
dp[3] = 1+2+1 = 4
dp[4] = 1+3+1+2 = 7
dp[5] = 1+4+3+3+2 = 13
"""