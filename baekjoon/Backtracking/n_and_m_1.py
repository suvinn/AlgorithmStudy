n, m = map(int, input().split())

# 1부터 n까지 자연수 중에서 중복 없이 m 개를 고른 수열
def backtrack():
    if len(arr) == m:
        print(*arr)
        return
    
    for i in range(1, n+1):
        if not used[i]:
            used[i] = True
            arr.append(i)
            backtrack()
            arr.pop()
            used[i] = False


used = [False] * (n+1)
arr = []
backtrack()