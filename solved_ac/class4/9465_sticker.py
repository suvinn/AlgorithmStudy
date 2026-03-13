import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    score = [[0] * n for _ in range(2)]
    for i in range(0, n-2, 2):
        sticker[0][i+2] += max(sticker[0][i] + sticker[1][i+1], sticker[1][i])
        sticker[1][i+2] += max(sticker[1][i] + sticker[0][i+1], sticker[0][i])
    if n % 2 == 0:
        sticker[0][n-1] += sticker[1][n-2]
        sticker[1][n-1] += sticker[0][n-2]
    print(max(sticker[0][n-1], sticker[1][n-1]))