import sys
input = sys.stdin.readline

n = int(input())
data = [input().strip() for _ in range(n)]
data = list(set(data))
data.sort()
data.sort(key=len)

for d in data:
    print(d)