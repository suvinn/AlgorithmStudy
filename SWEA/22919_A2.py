from itertools import combinations

for tc in range(1, int(input())+1):
    n = int(input())
    arr = list(map(int, input().split()))
    max_score = 0
    for combi in combinations(range(n), 4):
        a, b, c, d = combi
        if abs(a-b) == 1 or abs(b-c) == 1 or abs(c-d) == 1 or abs(n-(d-a)) == 1:
            continue
        score1 = (arr[a] + arr[b]) ** 2 + (arr[c] + arr[d]) ** 2
        score2 = (arr[a] + arr[d]) ** 2 + (arr[b] + arr[c]) ** 2
        max_score = max(score1, score2, max_score)
    print(f'#{tc}', max_score)


# for tc in range(1, int(input())+1):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     max_line = 0
#     for i in range(n):
#         for j in range(i+2, n):
#             for k in range(j+2, n):
#                 for l in range(k+2, n-i-1):
#                     line1 = (arr[i] + arr[j]) ** 2
#                     line2 = (arr[k] + arr[l]) ** 2
#                     max_line = max(line1 + line2, max_line)
#     print(f'#{tc}', max_line)