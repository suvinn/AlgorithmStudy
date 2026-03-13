import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())
n_lst = list(int(input()) for _ in range(t))

dp = defaultdict(list)
dp[0] = [1, 0]
dp[1] = [0, 1]
for i in range(2, max(n_lst)+1):
    dp[i] = [x+y for x, y in zip(dp[i-1], dp[i-2])]

for n in n_lst:
    print(*dp[n])

"""
fibo(6) = [5, 8]
fibo(5) = [3, 5]
fibo(4) = [2, 3]
fibo(3) = [1, 2]
fibo(2) = [1, 1]
fibo(1) = [0, 1]
fibo(0) = [1, 0]
"""