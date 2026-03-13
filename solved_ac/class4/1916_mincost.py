import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
m = int(input())
info = defaultdict(list)
for _ in range(m):
    s, e, c = map(int, input().split())
    info[s].append((e, c))
start, end = map(int, input().split())

cost = [float('inf')] * (n+1)
def dijkstra(start):
    arr = []
    heapq.heappush(arr, (0, start))
    cost[start] = 0
    while arr:
        c, x = heapq.heappop(arr)
        if c > cost[x]:
            continue
        for nx, nc in info[x]:
            if cost[nx] > cost[x] + nc:
                cost[nx] = cost[x] + nc
                heapq.heappush(arr, (cost[nx], nx))
dijkstra(start)
print(cost[end])