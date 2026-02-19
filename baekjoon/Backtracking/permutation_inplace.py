n = 3
num = [1, 2, 3]

def permute(k):
    if k == n:
        print(num)
        return
    
    for i in range(k, n):
        num[k], num[i] = num[i], num[k]  # swap
        permute(k+1)
        num[k], num[i] = num[i], num[k]  # 복구

permute(0)