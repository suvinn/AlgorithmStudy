import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nlisten, nseen = set(), set()
for _ in range(n):
    nlisten.add(input().strip())
for _ in range(m):
    nseen.add(input().strip())

answer = nlisten & nseen
answer = sorted(answer)
print(len(answer))
for name in answer:
    print(name)