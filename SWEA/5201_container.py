for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    weight = sorted(map(int, input().split()), reverse=True)
    ton = sorted(map(int, input().split()), reverse=True)
    total = 0

    print(f'#{tc}', total)