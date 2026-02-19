# n x n 체스판에 n개의 퀸을 놓을 수 있는가?
# 상하좌우 방향, 대각선 방향에 다른 퀸이 없어야 한다.

# / 방향 대각선: [0, n-1], [1, n-2], .., [n-1, 0]
# i + j 일정 -> i + j
# \ 방향 대각선: [0, 0], [1, 1], [n-1, n-1]
# i - j 일정 -> 음수일 경우 보정 -> n - 1 + i - j

def n_queen(i):
    global cnt
    if i == n:
        cnt += 1
        return
    
    for j in range(n):
        if not col[j] and not diag1[i+j] and not diag2[n-1+i-j]:
            col[j], diag1[i+j], diag2[n-1+i-j] = True, True, True
            n_queen(i+1)
            col[j], diag1[i+j], diag2[n-1+i-j] = False, False, False


n = int(input())
col = [False] * n
diag1 = [False] * (2*n + 1)
diag2 = [False] * (2*n + 1)
cnt = 0
n_queen(0)
print(cnt)