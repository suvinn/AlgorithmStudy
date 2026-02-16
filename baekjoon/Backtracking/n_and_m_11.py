n, m = map(int, input().split())
num = sorted(set(map(int, input().split())))

# n개의 자연수 중에서 m개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
arr = []
def backtrack():
    if len(arr) == m:
        print(*arr)
        return
    
    for i in range(len(num)):
        arr.append(num[i])
        backtrack()
        arr.pop()

backtrack()