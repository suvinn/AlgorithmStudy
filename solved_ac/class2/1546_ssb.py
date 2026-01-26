n = int(input())
data = list(map(int, input().split()))

m = max(data)
print(sum(map(lambda x: x/m*100, data))/n)