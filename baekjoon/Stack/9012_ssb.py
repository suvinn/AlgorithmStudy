import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    stack = []
    for l in input().strip():
        if l == '(':
            stack.append(l)
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if stack:
            print('NO')
        else:
            print('YES')