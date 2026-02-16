# 누적합 이용
from collections import defaultdict

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    carrots = list(map(int, input().split()))
    carrots.sort()

    cnt = defaultdict(int)
    for carrot in carrots:
        cnt[carrot] += 1
    
    cnt_list = list(cnt.values())
    m = len(cnt_list)
    if m < 3:
        print(f'#{tc}', -1)
        continue
    
    prefix = [0] * (m+1)
    for i in range(m):
        prefix[i+1] = prefix[i] + cnt_list[i]  # prefix[i+1]: i번째 당근까지의 누적합
    
    ans = float('inf')
    for i in range(m-2):
        for j in range(i+1, m-1):
            small = prefix[i+1]
            middle = prefix[j+1] - prefix[i+1]
            large = n - prefix[j+1]
            ans = min(max(small, middle, large) - min(small, middle, large), ans)

    print(f'#{tc}', ans)


# 2/16 풀이
from collections import defaultdict

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    carrots = list(map(int, input().split()))
    carrots.sort()

    cnt = defaultdict(int)
    for carrot in carrots:
        cnt[carrot] += 1
    
    m = len(cnt)
    if m < 3:
        print(f'#{tc}', -1)
    else:
        cnt_list = list(cnt.values())
        ans = 1000
        small = 0
        for i in range(m-2):
            small += cnt_list[i]
            middle = 0
            for j in range(i+1, m-1):
                middle += cnt_list[j]
                # large = 0
                # for k in range(j+1, m):
                #     large += cnt_list[k]
                large = n - (small + middle)
                ans = min(max(small, middle, large) - min(small, middle, large), ans)
            
        print(f'#{tc}', ans)


# 2/9 풀이
from collections import defaultdict

for tc in range(1, int(input())+1):
    n = int(input())
    carrot = list(map(int, input().split()))
    carrot.sort()
    dct = defaultdict(int)
    for c in carrot:
        dct[c] += 1
    
    if len(dct) < 3:
        min_carrot = -1
    
    else:
        carrot_cnt = list(dct.values())
        m = len(carrot_cnt)
        small, middle, big = 0, 0, 0
        compare = []
        for i in range(m-2):
            small += carrot_cnt[i]
            for j in range(i+1, m-1):
                middle += carrot_cnt[j]
                for k in range(j+1, m):
                    big += carrot_cnt[k]
                compare.append((small, middle, big))
                big = 0
            middle = 0
        
        min_carrot = 1000
        for c in compare:
            curr_carrot = max(c) - min(c)
            if min_carrot > curr_carrot:
                min_carrot = curr_carrot

    print(f'#{tc}', min_carrot)