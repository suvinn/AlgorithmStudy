# Pn = 'IOI' + 'OI' * (n-1)
n = int(input())
m = int(input())
s = input()

cnt = 0
i = 0
while i < m-2:
    if s[i] == 'I' and s[i+1] == 'O' and s[i+2] == 'I':
        tmp = 1
        i += 2
        if tmp >= n:
            cnt += 1
        while i < m-2 and s[i+1] == 'O' and s[i+2] == 'I':
            tmp += 1
            i += 2
            if tmp >= n:
                cnt += 1
        i -= 1
    else:
        i += 1
print(cnt)


# n = int(input())
# m = int(input())
# s = input()

# target = 'IO'*n + 'I'
# k = 2*n + 1
# cnt = 0
# for i in range(m-k+1):
#     if s[i:i+k] == target:
#         cnt += 1
# print(cnt)