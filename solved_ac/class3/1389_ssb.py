import sys
from collections import defaultdict, deque
input = sys.stdin.readline

n, m = map(int, input().split())
friends = defaultdict(list)
for _ in range(m):
    i, j = map(int, input().split())
    friends[i].append(j)
    friends[j].append(i)

kebin = [0] * (n+1)
for i in range(1, n+1):
    dist = [-1] * (n+1)
    queue = deque([i])
    dist[i] = 0
    while queue:
        now = queue.popleft()
        for next in friends[now]:
            if dist[next] == -1:
                dist[next] = dist[now] + 1
                queue.append(next)
    kebin[i] = sum(dist)+1

kebin = kebin[1:]
print(kebin.index(min(kebin)) + 1)


# import sys
# from collections import defaultdict, deque
# input = sys.stdin.readline

# n, m = map(int, input().split())
# friends = defaultdict(list)
# for _ in range(m):
#     i, j = map(int, input().split())
#     friends[i].append(j)
#     friends[j].append(i)

# kebin = []
# for i in range(1, n+1):
#     dist = [-1] * (n+1)
#     dist[i] = 0
#     queue = deque([i])
#     while queue:
#         s = queue.popleft()
#         for f in friends[s]:
#             if dist[f] == -1:
#                 dist[f] = dist[s] + 1
#                 queue.extend(friends[f])
#     kebin.append(sum(dist)+1)
# print(kebin)