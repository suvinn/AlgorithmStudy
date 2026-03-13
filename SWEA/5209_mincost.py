def backtrack(row, cost):
    global min_cost
    if cost >= min_cost:
        return
    
    if row == n:
        min_cost = cost
        return
    
    for col in range(n):
        if not visited[col]:
            visited[col] = True
            backtrack(row + 1, cost + arr[row][col])
            visited[col] = False

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    min_cost = float('inf')
    backtrack(0, 0)
    print(f'#{tc}', min_cost)