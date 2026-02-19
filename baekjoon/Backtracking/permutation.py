n = 3
num = [1, 2, 3]
p = [0] * n
used = [False] * n  # num[i]를 사용했는지 여부

def permute(k):
    if k == n:
        print(p)
        return
    
    for i in range(n):
        if not used[i]:
            used[i] = True
            p[k] = num[i]
            permute(k+1)
            used[i] = False

permute(0)