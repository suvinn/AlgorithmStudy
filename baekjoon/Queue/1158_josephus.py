from collections import deque

n, k = map(int, input().split())
queue = deque(list(i+1 for i in range(n)))
ans = []
i = 1
while queue:
    if i == k:
        ans.append(queue.popleft())
        i = 1
    else:
        queue.append(queue.popleft())
        i += 1
print('<' + ', '.join(map(str, ans)) + '>')