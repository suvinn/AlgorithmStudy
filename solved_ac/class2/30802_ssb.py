n = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

t = 0
for s in size:
    if s == 0:
        t += 0
    elif s%T == 0:
        t += s//T
    else:
        t += s//T + 1

p1, p2 = sum(size)//P, sum(size)%P


print(t)
print(p1, p2)