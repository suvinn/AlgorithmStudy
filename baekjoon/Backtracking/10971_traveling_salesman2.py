n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
min_cost = float('inf')
def backtrack(start, step, cost):
    global min_cost

    # 모든 마을 순회
    if step == n:
        if not arr[start][0]:
            return
        cost += arr[start][0]
        min_cost = min(cost, min_cost)
        return

    # 가지치기
    if cost >= min_cost:
        return

    go = False
    for i in range(n):
        # 현재 마을 / 이미 방문한 마을 / 갈 수 없는 마을 건너뛰기
        if i == start or visited[i] or not arr[start][i]:
            continue

        go = True
        visited[i] = True
        cost += arr[start][i]
        backtrack(i, step+1, cost)
        cost -= arr[start][i]
        visited[i] = False
    
    # 다음 마을로 갈 수 없는 상태라면
    if not go:
        return

visited[0] = True
backtrack(0, 1, 0)
print(min_cost)