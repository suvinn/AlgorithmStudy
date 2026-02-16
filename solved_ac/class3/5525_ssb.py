n = int(input())
m = int(input())
s = input()

target = 'IO'*n + 'I'
k = 2*n + 1
cnt = 0
for i in range(m-k+1):
    if s[i:i+k] == target:
        cnt += 1
print(cnt)