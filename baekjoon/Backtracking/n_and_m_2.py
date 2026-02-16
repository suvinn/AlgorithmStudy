n, m = map(int, input().split())

# 1부터 n까지 자연수 중에서 중복 없이 m개를 고른 수열
# 고른 수열은 오름차순이어야 한다.
arr = []
def backtrack(start):
    if len(arr) == m:
        print(*arr)
        return
    
    for i in range(start, n+1):
        arr.append(i)
        backtrack(i+1)
        arr.pop()

backtrack(1)