import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
graph = defaultdict(list)
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            graph[i].append(j)

matrix = [[0]*n for _ in range(n)]
for i in range(n):
    stack = [i]
    visited = [False] * n
    while stack:
        s = stack.pop()
        if s in graph.keys():
            for k in graph[s]:
                if not visited[k]:
                    matrix[i][k] = 1
                    visited[k] = True
                    stack.append(k)

for row in matrix:
    print(*row)
            