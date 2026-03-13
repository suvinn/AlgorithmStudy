import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
end_day = [i + arr[i][0] for i in range(n)]

dp = [0] * (n+1)
for end in range(1, n+1):
    max_wage = dp[end-1]
    for start in range(n):
        if end_day[start] == end:
            max_wage = max(dp[end-arr[start][0]]+arr[start][1], max_wage)
    dp[end] = max_wage

print(max(dp))