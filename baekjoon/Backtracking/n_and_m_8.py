n, m = map(int, input().split())
num = sorted(map(int, input().split()))

# n개의 자연수 중에서 m개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.
arr = []
def backtrack(start):
    if len(arr) == m:
        print(*arr)
        return
    
    for i in range(start, n):
        arr.append(num[i])
        backtrack(i)
        arr.pop()

backtrack(0)