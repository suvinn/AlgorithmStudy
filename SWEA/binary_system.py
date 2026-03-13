b = '1100'
d = int(b, 2)
h = hex(d)
print(b, d, h.upper()[2:])  # 1100 12 C

h = 'A'
d = int(h, 16)
b = bin(d)
print(h, d, b[2:])  # A 10 1010


grid = [list(map(int, input().split())) for _ in range(6)]
col = [list(colums) for colums in zip(*grid)]
print(grid, col)