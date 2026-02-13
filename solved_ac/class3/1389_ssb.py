import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n, m = map(int, input().split())
friends = defaultdict(list)
for _ in range(m):
    i, j = map(int, input().split())
    friends[i].append(j)
    friends[j].append(i)

kebin = []
for i in range(1, n+1):
    dist = [-1] * (n+1)
    dist[i] = 0
    queue = deque([i])
    while queue:
        s = queue.popleft()
        for f in friends[s]:
            if dist[f] == -1:
                dist[f] = dist[s] + 1
                queue.extend(friends[f])
    kebin.append(sum(dist)+1)
print(kebin)