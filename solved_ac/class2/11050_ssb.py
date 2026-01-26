n, k = map(int, input().split())

mul1, mul2 = 1, 1
for i in range(k):
    mul1 *= (n-i)
    mul2 *= (i+1)

print(mul1//mul2)