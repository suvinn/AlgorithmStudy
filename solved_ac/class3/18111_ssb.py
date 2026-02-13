import sys
from collections import defaultdict
input = sys.stdin.readline

n, m, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dct = defaultdict(int)
for i in range(n):
    for j in range(m):
        dct[arr[i][j]] += 1

min_h, max_h = min(dct.keys()), max(dct.keys())
ans = []
for goal_h in range(min_h, max_h+1):
    time, curr_b = 0, b
    for k, v in dct.items():
        if k == goal_h:
            continue
        elif k < goal_h:
            curr_b -= (goal_h - k)*v
            time += (goal_h - k)*v
        else:
            curr_b += (k - goal_h)*v
            time += 2*(k - goal_h)*v
    if curr_b >= 0:
        ans.append((time, goal_h))
ans.sort(key=lambda x: (x[0], -x[1]))
print(*ans[0])

# import sys
# input = sys.stdin.readline

# n, m, b = map(int, input().split())
# arr = []
# for _ in range(n):
#     row = list(map(int, input().split()))
#     arr.extend(row)
# arr.sort()

# min_h, max_h = arr[0], arr[-1]
# ans = []
# for goal_h in range(min_h, max_h+1):
#     curr_b = b + sum(map(lambda x: x-goal_h, arr))
#     time = sum(map(lambda x: abs(x-goal_h), arr)) + sum(map(lambda x: max(x-goal_h, 0), arr))
#     if curr_b >= 0:
#         ans.append((time, goal_h))

# ans.sort(key=lambda x: (x[0], -x[1]))
# print(*ans[0])


# import sys
# input = sys.stdin.readline

# n, m, b = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]

# min_h, max_h = 256, 0
# for row in arr:
#     curr_min, curr_max = min(row), max(row)
#     if curr_min < min_h:
#         min_h = curr_min
#     if curr_max > max_h:
#         max_h = curr_max

# ans = []
# for goal_h in range(min_h, max_h+1):
#     time = 0
#     curr_b = b
#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] == goal_h:
#                 continue
#             elif arr[i][j] > goal_h:
#                 curr_b += arr[i][j] - goal_h
#                 time += 2*(arr[i][j] - goal_h)
#             elif arr[i][j] < goal_h:
#                 curr_b -= goal_h - arr[i][j]
#                 time += goal_h - arr[i][j]
#     if curr_b >= 0:
#         ans.append((time, goal_h))

# ans.sort(key=lambda x: (x[0], -x[1]))
# print(*ans[0])