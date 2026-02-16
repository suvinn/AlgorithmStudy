for tc in range(1, int(input())+1):
    n = int(input())
    cards = input().split()
    left, right = cards[:(n+1)//2], cards[(n+1)//2:]
    deck = []
    if n % 2:
        for i, j in zip(left[:-1], right):
            deck.extend([i, j])
        deck.append(left[-1])
    else:
        for i, j in zip(left, right):
            deck.extend([i, j])
    print(f'#{tc}', *deck)