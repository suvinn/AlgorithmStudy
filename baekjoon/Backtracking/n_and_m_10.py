n, m = map(int, input().split())
num = sorted(map(int, input().split()))

# n개의 자연수 중에서 m개를 고른 수열
# 고른 수열은 비내림차순이어야 한다.
used = [False] * n
arr = []
def backtrack(start):
    if len(arr) == m:
        print(*arr)
        return
    
    prev = None
    for i in range(start, n):
        if not used[i] and num[i] != prev:
            used[i] = True
            arr.append(num[i])
            prev = num[i]
            backtrack(i)
            arr.pop()
            used[i] = False

backtrack(0)