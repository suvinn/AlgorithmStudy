n = int(input())
lst = list(map(int, input().split()))

lst.sort()
answer = sum(lst[i]*(len(lst)-i) for i in range(len(lst)))

print(answer)