n, m = map(int, input().split())
num = sorted(map(int, input().split()))

# n개의 자연수 중에서 m개를 고른 수열
used = [False] * n
arr = []
def backtrack():
    if len(arr) == m:
        print(*arr)
        return
    
    # 같은 depth에서 같은 숫자 다시 안 쓰게 막기
    prev = None
    for i in range(n):
        if not used[i] and num[i] != prev:
            used[i] = True
            arr.append(num[i])
            prev = num[i]
            backtrack()
            arr.pop()
            used[i] = False

backtrack()