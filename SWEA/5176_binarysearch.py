def binary_search(k):
    global cnt
    if k > n:
        return
    binary_search(k*2)  # 왼쪽 자식
    cnt += 1
    tree[k] = cnt
    binary_search(k*2+1)  # 오른쪽 자식
 
for tc in range(1, int(input())+1):
    n = int(input())
    arr = [i+1 for i in range(n)]
    cnt = 0
    tree = [0] * (n+1)
    binary_search(1)
    print(f'#{tc}', tree[1], tree[n//2])