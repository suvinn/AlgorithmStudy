for tc in range(1, int(input())+1):
    e, n = map(int, input().split())
    arr = list(map(int, input().split()))
    parent = [0] * (e+2)
    child1 = [0] * (e+2)
    child2 = [0] * (e+2)
    for i in range(e):
        p, c = arr[i*2], arr[i*2+1]
        parent[c] = p
        if child1[p] == 0:
            child1[p] = c
        else:
            child2[p] = c
    stack = [n]
    cnt = 1
    while stack:
        root = stack.pop()
        if not child1[root] and not child2[root]:
            continue
        if child1[root]:
            stack.append(child1[root])
            cnt += 1
        if child2[root]:
            stack.append(child2[root])
            cnt += 1
    print(f'#{tc}', cnt)