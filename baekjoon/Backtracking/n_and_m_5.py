n, m = map(int, input().split())
num = sorted(map(int, input().split()))

# n개의 자연수 중에서 m개를 고른 수열
used = [False] * n
arr = []
def backtrack():
    if len(arr) == m:
        print(*arr)
        return
    
    for i in range(n):
        if not used[i]:
            used[i] = True
            arr.append(num[i])
            backtrack()
            arr.pop()
            used[i] = False

backtrack()