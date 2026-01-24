import sys
input = sys.stdin.readline

m = int(input())

s = set()
for _ in range(m):
    lst = list(input().split())
    if len(lst) == 1:
        word = lst[0]
    else:
        word, x = lst
        x = int(x)
    if word == 'add':
        s.add(x)
    elif word == 'remove' and x in s:
        s.remove(x)
    elif word == 'check':
        print(1 if x in s else 0)
    elif word == 'toggle':
        s.add(x) if x not in s else s.remove(x)
    elif word == 'all':
        s = set(i+1 for i in range(20))
    elif word == 'empty':
        s.clear()