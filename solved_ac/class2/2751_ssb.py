import sys
input = sys.stdin.readline

n = int(input())
data = list(set(int(input()) for _ in range(n)))
data.sort()

for d in data:
    print(d)