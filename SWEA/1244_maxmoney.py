def backtrack(step):
    global max_num

    if step == cnt:
        max_num = max(max_num, int(''.join(num)))
        return
    
    state = (step, int(''.join(num)))
    if state not in visited:
        visited.add(state)
    else:
        return
    
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if i == j:
                continue
            num[i], num[j] = num[j], num[i]
            backtrack(step+1)
            num[i], num[j] = num[j], num[i]

for tc in range(1, int(input())+1):
    num, cnt = input().split()
    num, cnt = list(num), int(cnt)
    max_num = -float('inf')
    visited = set()
    backtrack(0)
    print(f'#{tc}', max_num)