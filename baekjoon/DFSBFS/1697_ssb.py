from collections import deque

n, k = map(int, input().split())

queue = deque([(n, 0)])
visited = [False] * 100001

visited[n] = True
def bfs(x):
    while queue:
        x, depth = queue.popleft()
        nx = [x - 1, x + 1, 2*x]
        for x in nx:
            if x == k:
                return depth+1 if n != k else 0
            if 0 <= x <= 100000 and not visited[x]:
                queue.append((x, depth+1))
                visited[x] = True

print(bfs(n))