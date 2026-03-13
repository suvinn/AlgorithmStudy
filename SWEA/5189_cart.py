# 사무실에서 출발해 각 관리구역을 돌고 다시 사무실로 돌아와야 한다.
def backtrack(start, step, cost):
    global min_cost
    if step == n:
        cost += arr[start][0]
        min_cost = min(cost, min_cost)
        return
    # 가지 치기
    if cost > min_cost:
        return
    for i in range(n):
        if start == i:
            continue
        if not visited[i]:
            visited[i] = True
            cost += arr[start][i]
            backtrack(i, step+1, cost)
            cost -= arr[start][i]
            visited[i] = False

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    visited[0] = True
    min_cost = float('inf')
    backtrack(0, 1, 0)
    print(f'#{tc}', min_cost)  

    