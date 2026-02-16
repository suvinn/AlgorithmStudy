n, m = map(int, input().split())

# 1부터 n까지 자연수 중에서 m개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
arr = []
def backtrack():
    if len(arr) == m:
        print(*arr)
        return
    
    for i in range(1, n+1):
        arr.append(i)
        backtrack()
        arr.pop()

backtrack()