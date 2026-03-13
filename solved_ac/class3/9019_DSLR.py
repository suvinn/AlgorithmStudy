import sys
from collections import deque
input = sys.stdin.readline

case = 1
visited = [0] * 10000
prev = [0] * 10000
how = [''] * 10000

results = []
for _ in range(int(input())):
    a, b = map(int, input().split())

    queue = deque([a])
    visited[a] = case
    while queue:
        x = queue.popleft()
        if x == b:
            break

        d = 2*x % 10000
        if visited[d] != case:
            visited[d] = case
            prev[d] = x
            how[d] = 'D'
            queue.append(d)
        
        s = x - 1 if x > 0 else 9999
        if visited[s] != case:
            visited[s] = case
            prev[s] = x
            how[s] = 'S'
            queue.append(s)
        
        l = (x % 1000)*10 + (x // 1000)
        if visited[l] != case:
            visited[l] = case
            prev[l] = x
            how[l] = 'L'
            queue.append(l)
        
        r = (x % 10)*1000 + (x // 10)
        if visited[r] != case:
            visited[r] = case
            prev[r] = x
            how[r] = 'R'
            queue.append(r)
    now = b
    ans = []
    while now != a:
        ans.append(how[now])
        now = prev[now]
    results.append(''.join(reversed(ans)))
    case += 1

print('\n'.join(results))