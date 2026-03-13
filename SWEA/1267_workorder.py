from collections import deque

for tc in range(1, 11):
    v, e = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(v+1)]
    indegree = [0] * (v+1)
    for i in range(0, 2*e, 2):
        graph[arr[i]].append(arr[i+1])
        indegree[arr[i+1]] += 1
    queue = deque()
    for i in range(1, v+1):
        if indegree[i] == 0:
            queue.append(i)
    result = []
    while queue:
        now = queue.popleft()
        result.append(now)
        for nxt in graph[now]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    print(f'#{tc}', *result)