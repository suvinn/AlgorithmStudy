for tc in range(1, int(input())):
    n, m, l = map(int, input().split())
    tree = [0] * (n+1)
    for _ in range(m):
        node, num = map(int, input().split())
        tree[node] = num
    for i in range(n, 0, -1):
        p = i
        c = i*2
        if c <= n:
    print(f'#{tc}')