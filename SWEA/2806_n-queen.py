def backtrack(row):
    global cnt

    if row == n:
        cnt += 1
        return
    
    for col in range(n):
        if not column[col] and not diag_r[col+row] and not diag_l[n-1+col-row]:
            column[col], diag_r[col+row], diag_l[n-1+col-row] = True, True, True
            backtrack(row + 1)
            column[col], diag_r[col+row], diag_l[n-1+col-row] = False, False, False

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [[0] * n in range(n)]
    column = [False] * n
    diag_r = [False] * 2*n
    diag_l = [False] * 2*n
    cnt = 0
    backtrack(0)
    print(f'#{tc}', cnt)